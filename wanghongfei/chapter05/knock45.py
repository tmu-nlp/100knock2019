from knock41 import get_chunk

if __name__ == "__main__":
    file_name = "./neko.txt.cabocha"
    sentences = get_chunk(file_name)
    verb_case = {}
    particle_list = []
    for sentence in sentences[:10]:
        for chunk in sentence:
            for verb in [i for i in chunk.morphs]:
                if "動詞" in verb[2]:
                    verb_case.setdefault(verb[1],particle_list)
                    for particle in [i for i in sentence[int(chunk.dst)].morphs]:
                        if "助詞" in particle[2]:
                            verb_case[verb[1]].append(particle[1])
    print(verb_case)




