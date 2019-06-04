def main():
    # with open('country.fix.txt', 'w') as f:
    #     for country in open('country.txt', 'r'):
    #         f.write(country.replace(u"\xa0",u""))


    with open('knock81.100.txt', 'w') as f:
        for line in open('knock80.100.txt', 'r'):
            for country in open('country.fix.txt', 'r'):
                country = country.strip('\n')
                line = line.replace(country, country.replace(' ', '_'))

            f.write(line)


if __name__ == '__main__':
    main()
