def find_all(sent, char):
    start = 0
    while True:
        start = sent.find(char, start)
        if start == -1: return
        yield start
        start += len(char)

def cut_sentence(sentence):
    endsyms, preidx = [], 0
    for i in range(len(sentence)):
        if sentence[i] == '。' or sentence[i] == '！' or sentence[i] == '？':
            if i+1 < len(sentence) and sentence[i+1] == '”':
                endsyms.append(sentence[preidx:i+2])
                preidx = i + 2
            else:
                endsyms.append(sentence[preidx:i+1])
                preidx = i + 1

    # 根据句子长度cut句子
    cuts = []
    for line in endsyms:
        if len(line) >= 5:
            if len(line) >= 30:
                list_punct = list(find_all(line, '，'))
                if list_punct != [] and list_punct[0] != -1:
                    cut_idx = list_punct[len(list_punct) // 2]
                    cuts.append(line[:cut_idx])
                    cuts.append(line[cut_idx+1:])
                else:
                    cuts.append(line)
            else:
                cuts.append(line)

    # 处理双引号不平衡现象
    res = []
    for line in cuts:
        if "：“" in line and "”" not in line:
            idx = line.find("“")
            line = line[idx+1:]
        elif "”" == line[-1] and "“" not in line:
            line = line[:-1]
        if "。" == line[-1] or "！" == line[-1]:
            line = line[:-1]
        if len(line) >= 4:
            res.append(line)
    
    return res
