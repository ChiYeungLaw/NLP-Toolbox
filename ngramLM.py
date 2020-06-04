import re
import time
import nltk
import jieba
import argparse
import dill as pickle
from nltk.lm import Laplace
from nltk.lm.preprocessing import padded_everygram_pipeline

parser = argparse.ArgumentParser(description='Ngram model training')

parser.add_argument('--data_path', default='all_zhenhuan.txt', type=str, help='data path')
parser.add_argument('--N', default=2, type=int, help='N-gram')
parser.add_argument('--save_model', default='zhenhuan_ngram_model.pkl', type=str, help='model saving path')

config = parser.parse_args()

# read data
print(f"Reading text data from {config.data_path}.")
datas = []
with open(config.data_path, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if line != '':
            datas.append(line)
print("Reading finish.")

# remove all the non Chinese words
def remove_no_zh_char(sent):
    new_sent, no_zh_re = [], r'^[\u4e00-\u9fa5]+$'
    for word in sent:
        new_word = []
        for char in word:
            if re.search(no_zh_re, char):
                new_word.append(char)
        if new_word:
            new_sent.append(''.join(new_word))
    return new_sent

# tokenization
print(f"Tokenization and remove non Chinese Character.")
tok_datas = []
for i, line in enumerate(datas):
    i += 1
    line = list(jieba.cut(line))
    tok_datas.append(remove_no_zh_char(line))
    if i % 200 == 0:
        print(f"#{i} sentences process.")
print(f"Tokenization finish.")

# NGram model training
print(f"Start training Ngram model.")
start = time.time()
train, vocab = padded_everygram_pipeline(config.N, tok_datas)
model = Laplace(config.N) # N-gram model
model.fit(train, vocab)
print(f"Training Ngram model finish. Time: {time.time()-start:.3f}s.")

print(f"Save Ngram model in {config.save_model}.")
with open(config.save_model, 'wb') as fout:
    pickle.dump(model, fout)
print("Save complete.")
