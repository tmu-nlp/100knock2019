import re

def sentence_spliter(file_name):
    input_text = re.sub(r"^\n", "", open(file_name, encoding="utf8").read())
    chr_list = list(input_text)
    s_start = 0
    for match in re.finditer(r"([.;:?!]) ([A-Z])", input_text):
        s_end = match.start()
        edit_text = chr_list[s_start:s_end+1] + ["\n"]
        s_start = s_end + 2
        yield "".join(edit_text)

if __name__ == "__main__":
    for sentence in sentence_spliter("nlp.txt"):
        print(sentence)