from enum import Enum
import threading
from function import get_translation_google, get_translation_deepl

# 単一行
class SingleType(Enum):
    SECTION = 0
    IMAGE   = 1
    URL     = 2
    LATEX   = 3
    TABLE   = 4
    LIST    = 5
    AST     = 6     # asterisk = LIST
dic_single: dict = {        # 行頭で確認
    SingleType.SECTION  : "#",
    SingleType.IMAGE    : "![",
    SingleType.URL      : "[",
    SingleType.LATEX    : "\\",     # ex. \newpage
    SingleType.TABLE    : "|",
    SingleType.LIST     : "- ",
    SingleType.AST      : "* ",
}

# 複数行
class BlockType(Enum):
    HEAD    = 0     # YAMLヘッダ
    FORMULA = 1     # 数式
    TABLE   = 2     # table
    CODE    = 3     # コード
    COMMENT = 4     # Comment
    LATEX   = 5     # LaTeX
dic_block_begin: dict = {         # 挟まれている範囲をブロックとし，翻訳対象外とする
    BlockType.HEAD      : "---",    # 初回のみ等の制限が必要?
    BlockType.FORMULA   : "$$",
    BlockType.TABLE     : "\\begin{tabular}",
    BlockType.CODE      : "```",
    BlockType.COMMENT   : "<!--",
    BlockType.LATEX     : "\\Begin",
}
dic_block_end: dict = {         # 優先度順に
    BlockType.HEAD      : "---",
    BlockType.FORMULA   : "$$",
    BlockType.TABLE     : "\\end{tabular}",
    BlockType.CODE      : "```",
    BlockType.COMMENT   : "-->",
    BlockType.LATEX     : "\\End",
}

# 行内
class InlineType(Enum):
    FORMULA = 0     # 数式
    CODE    = 1     # コード
ptn_inline: dict = {        # パターン一致箇所を一時的に置換し，翻訳を実行する
    InlineType.FORMULA  : "(?<=\$).*(?=\$)",
    InlineType.CODE     : "(?<=\`).*(?=\`)",
}
dic_inline: dict = {
    InlineType.FORMULA  : "$",
    InlineType.CODE     : "`",
}

# 翻訳単位
import copy
class TlUnit(threading.Thread):
    def __init__(self, text:str, ignore_list:list, use_api=False):
        threading.Thread.__init__(self)

        self.text: str          = text.replace("\n", "")
        self.ignore_list: list  = ignore_list
        self.use_api: bool      = use_api

    def run(self):
        if len(self.text) == 0:
            self.result = "\n"
            return
        
        result = ""

        # Translate and replace formula part
        if self.use_api:
            result = get_translation_deepl(self.text)       # DeepL API
        else:
            result = get_translation_google(self.text)        # Deep translator

        if result == None:
            print("Error: Translation result is None")
            self.result = ""
            return

        # Replace ignore list
        for i, text in enumerate(self.ignore_list):
            self.text   = self.text.replace(f"x{i:02}x", text)
            result      = result.replace(f"x{i:02}x", text)

        # 数字リスト対策
        result = result.replace(". ", "．")

        # アルファベットリスト対策
        for i in range(26):
            alphabet = chr(ord("a")+i)
            result = result.replace(f"({alphabet})", f"（{alphabet}）")
        
        # Build result
        #   対訳
        self.result = "\Begin{multicolpar}{2}" + f"{self.text}\n\n" + f"{result}\n" + "\End{multicolpar}\n\n"

        # 訳が同じ場合そのまま
        if self.text == result:
            self.result = f"{self.text}\n\n"

        # インライン対策(単一行)
        if self.text.startswith("$") and (self.text.endswith("$") or self.text.endswith("$.")) and self.text.count("$")==2:
            self.text = self.text.replace("$", "")
            self.result = f"$$\n{self.text}\n$$\n\n"
