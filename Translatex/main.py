import os
from argparse import ArgumentParser
from tqdm import tqdm
from xml.etree.ElementTree import *
import time

from define import BlockType, SingleType, InlineType, dic_block_begin, dic_block_end, dic_single, dic_inline, TlUnit

#   main
def main(args):
    # input
    path_text   = args.filename
    path_md     = f"tl_{os.path.splitext(path_text)[0]}.md"

    # load text
    list_text: list[str] = []
    with open(path_text, mode="rt", encoding="utf-8") as f:
        list_text = f.readlines()

    # get translation list
    result = ""
    block_type = None
    list_tl = []
    for text in tqdm(list_text, desc="Parsing", leave=False):
        # Check block
        if block_type == None:    # 始点捜索
            for type in BlockType:
                if text.startswith(dic_block_begin[type]):
                    block_type = type
                    break
            if block_type != None:
                result += text
                continue
        if block_type != None:
            result += text
            if text.startswith(dic_block_end[block_type]):  # 終点捜索
                block_type = None
            continue
        
        # Check single
        is_single = False
        for type in SingleType:
            if text.startswith(dic_single[type]):
                is_single = True
                break
        if is_single:
            result += text
            continue
        
        # Check inline
        ignore_list = []
        import copy
        translate_text = copy.deepcopy(text)
        temp = ""
        current = None
        for c in text:
            if current == None:
                for type in InlineType:
                    if c == dic_inline[type]:
                        temp = c
                        current = type
                        break
            else:
                temp += c
                if c == dic_inline[type]:
                    current = None
                    translate_text = translate_text.replace(temp, f"x{len(ignore_list):02}x")
                    ignore_list.append(temp)

        result += f"t{len(list_tl):02}t"
        unit = TlUnit(translate_text, ignore_list, option.api)
        unit.start()
        time.sleep(0.01)
        
        list_tl.append(unit)
    
    # wait thread
    for i, unit in tqdm(enumerate(list_tl), desc="Translating", leave=False):
        unit: TlUnit
        unit.join()
        result = result.replace(f"t{i:02}t", unit.result)

    # save text
    result.replace("\End{multicolpar}\Begin{multicolpar}{2} ", "")
    with open(path_md, mode="wt", encoding="utf-8") as f:
        f.write(result)

    print("\rComplete translation")

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("filename", help=".txt filename")
    parser.add_argument("--api", "-a", action="store_true", help="Use API(DeepL) for advanced translation")
    option = parser.parse_args()

    main(option)
