"""
Analyze LINE Pay log (Talk log with LINE wallet)
"""

import os
from argparse import ArgumentParser
import copy
import re
import csv

PATTERN_DAY     = r"(\w{4})/(\w{2})/(\w{2})\(.\)"
PATTERN_TIME    = r"(\w{2}):(\w{2})\t"
PATTERN_PLACE   = r"加盟店|銀行名"
PATTERN_CANCEL  = r"キャンセルしました"

TYPE_FOOD       = r"出前館|Uber Eats|マクドナルド|富士薬品グループ|オリジン|松屋|西友"
TYPE_HOME       = r"東京都水道局|東京電力"
TYPE_UNKNOWN    = r"Visa加盟店"


def main(option):
    input_path   = option.filepath
    output_path = os.path.join(os.path.dirname(input_path), os.path.basename(input_path)+".csv")

    # Read file
    with open(option.filepath, "rt", encoding="utf-8") as f:
        list_text = [line.replace("\n", "") for line in f.readlines()]
    list_text = list_text[3:] # Trim 3 lines

    # 日付区切り
    temp_day = DayData()
    list_day_data = []
    for text in list_text:
        if re.search(PATTERN_DAY, text):
            if len(temp_day.list_text) > 0:
                list_day_data.insert(-1, copy.deepcopy(temp_day))
            temp_day = DayData()
        temp_day.append(text)
    list_day_data.pop()
    list_day_data.append(temp_day)

    # 時刻区切り
    results = []
    for day in list_day_data:
        results += day.get_results()

    # 書き込み
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(results)

class DayData:
    def __init__(self):
        self.list_text = []

    def append(self, text:str):
        self.list_text.append(text)

    def get_results(self) -> list:
        day = self.list_text[0]
        temp_time = TimeData(day)
        list_time = []
        for text in self.list_text[1:]:
            if re.search(PATTERN_TIME, text):
                items = text.split("\t")
                time = items[0]
                try:
                    int(items[-1].split(" ")[-2].replace(",", ""))
                except (ValueError, IndexError):
                    temp_time.list_text.clear()
                    continue
                if len(temp_time.list_text) > 1:
                    list_time.append(copy.deepcopy(temp_time))
                temp_time = TimeData(day)
            if len(temp_time.list_text) > 0:
                temp_time.append(text)
        if len(temp_time.list_text) > 1:
            list_time.append(copy.deepcopy(temp_time))

        results = []
        for time in list_time:
            results.append(time.get_result())
        return results

class TimeData:
    def __init__(self, day):
        self.list_text = [day]
        self.debug = 0
    
    def append(self, text:str):
        self.list_text.append(text)

    def get_result(self):
        day     = self.list_text[0]
        data    = self.list_text[1].split("\t")
        time    = data[0]
        price   = data[-1].split(" ")[-2].replace(",", "")
        purpose = data[-1].split(" ")[-3]
        place   = ""
        type    = 0     # 0:OTHER 1:FOOD 2:HOME
        for text in self.list_text:
            if re.search(PATTERN_PLACE, text):
                place = text.split(": ")[-1]
            if re.search(PATTERN_CANCEL, text):
                price = f"-{price}"
        if re.search(TYPE_FOOD, place):
            type = 1
        if re.search(TYPE_HOME, place):
            type = 2
        if re.search(TYPE_UNKNOWN, place):
            type = 3

        return [day, time, price, purpose, place, type]

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("filepath", help="Target to analyze")
    option = parser.parse_args()
    try:
        main(option)
    except:
        print('error: invalid args')