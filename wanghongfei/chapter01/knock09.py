import random


def typog(x):
    typog = ''
    word_list = x.split(' ')
    for word in word_list:
        if len(word) < 4:
            typog = typog + word + ' '
        else:
            random_list = random.sample(word[1:-1], len(word)-2)
            turn2str = ''
            for alphab in random_list:
                turn2str = turn2str + alphab
            typog = typog + word[0] + turn2str + word[-1] + ' '

    print(typog)


x = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
typog(x)
