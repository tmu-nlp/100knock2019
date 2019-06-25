'''
81. 複合語からなる国名への対処
英語では，複数の語の連接が意味を成すことがある．
例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と表現されるが，
"United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が曖昧である．
そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，
複合語の意味を推定したい．しかしながら，複合語を正確に認定するのは大変むずかしいので，
ここでは複合語からなる国名を認定したい．

インターネット上から国名リストを各自で入手し，
80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．
例えば，"United States"は"United_States"，
"Isle of Man"は"Isle_of_Man"になるはずである．
'''
import yaml

f_in_name = "out80.txt"
f_out_name = "out81.txt"
json_path = "./country-json/src/country-by-name.json"

d = {}
with open(json_path) as json_file:
    for name in map(lambda x: x['country'], yaml.safe_load(json_file)):
        if ' ' in name:
            d[name] = name.replace(' ', '_')

with open(f_out_name, 'w') as f_out:
    for line in open(f_in_name):
        for tgt, repl in d.items():
            line = line.replace(tgt, repl)
        f_out.write(line)


'''
* country
https://github.com/samayo/country-json
Usage - Python で yaml を使っていた
'''
