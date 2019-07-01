def main():
    families = []
    family = False
    with open('questions-words.txt', 'r') as input_f, \
            open('family.txt', 'w') as out_f:

        for line in input_f:
            line = line.strip()
            if line == ': family':
                family = True
                continue
            elif line[0] == ':' and family is True:
                family = False

            if not family:
                continue

            families.append(line)

        out_f.write('\n'.join(families))


if __name__ == "__main__":
    main()
