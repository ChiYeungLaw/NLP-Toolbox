import re
def no_zh_char(lines):
    no_zh_re, no_zh = r'^[\u4e00-\u9fa5]+$', []
    for line in lines:
        for char in list(line):
            if not re.search(no_zh_re, char):
                no_zh.append(char)
    no_zh = list(set(no_zh))
    return no_zh
