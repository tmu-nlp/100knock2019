sentences_file = open("./nlp_sentences.txt","r").readlines()
with open("./words.txt","w") as f:
    for line in sentences_file:
        words_list = line.split(" ")
        for index, value in enumerate(words_list):
            print(value,file = f)

