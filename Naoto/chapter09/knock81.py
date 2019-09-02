'''
81. 複合語からなる国名への対処
英語では，複数の語の連接が意味を成すことがある．例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と表現されるが，"United"や"States"，"Kingdom"という単語だけでは，指し示している概念・実体が曖昧である．そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，複合語の意味を推定したい．しかしながら，複合語を正確に認定するのは大変むずかしいので，ここでは複合語からなる国名を認定したい．

インターネット上から国名リストを各自で入手し，80のコーパス中に出現する複合語の国名に関して，スペースをアンダーバーに置換せよ．例えば，"United States"は"United_States"，"Isle of Man"は"Isle_of_Man"になるはずである．
'''


in_file = "out80.txt"
out_file = "out81_2.txt"
d = {}

with open("countries.txt", "r") as f_countries:
    for name in f_countries:
        name = name.rstrip()
        if ' ' in name:
            d[name] = name.replace(' ', '_')

with open(in_file, "r") as f_in, open(out_file, "w") as f_out:
    for line in f_in:
        for src, tgt in d.items():
            line = line.replace(src, tgt)
        f_out.write(line)
