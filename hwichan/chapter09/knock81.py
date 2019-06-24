from collections import defaultdict


def countries_dict():
    countries = defaultdict()
    with open('countries.txt', 'r') as f:
        for line in f:
            country = line.strip()
            if len(country.split(' ')) > 1:  # Commonwealth of Australia, Niue
                countries[country] = '_'.join(country.split(' '))

    return countries


def main():
    countries = countries_dict()

    with open('out.txt', 'r') as input_file, \
         open('out_rename.txt', 'w') as out_file:
         text = []
         for line in input_file:
             line = line.strip()
             for country, country_ in countries.items():
                 if country in line:
                     line = (line.replace(country, country_))
             text.append(line)

         out_file.write('\n'.join(text))


if __name__ == "__main__":
    main()
