# NLP-Toolbox
Personal NLP Little Toolbox

### baidu_translate.py

use baidu translate's api to translate a sentence

### cut_sentence.py

use regular expression to cut Chinese sentences

### find_no_zh_char.py

use regular expression to find all the none Chinese characeters in the datasets

#### ngramLM.py

You can use this file to train a Chinese NGram Language Model.

How to use?
```
python ngramLM.py --data_path xxx.txt --N 3 --save_model xxx.pkl
```
Requirements:
```
nltk
jieba
dill
```
