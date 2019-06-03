import xml.etree.ElementTree as ET
from collections import defaultdict


def main():
    root = ET.parse('nlp.txt.xml')

    for dependencies in root.iterfind('./document/sentences/sentence/dependencies[@type="collapsed-dependencies"]'):
        dep_dict = defaultdict()
        for dep in dependencies.iterfind('dep'):
            dep_type = dep.get('type')
            # dep_type == 'nsubj' の場合dependentが主語
            # dep_type == ''dobj' の場合dependentが目的語
            # governorは述語
            if dep_type == 'nsubj' or dep_type == 'dobj':
                governor = dep.findall('governor')[0]  # 係り元、述語
                idx = governor.get('idx')  # 述語のidxはnusnjもdobjも同じ

                if idx not in dep_dict:
                    dep_dict[idx] = [governor.text]  # 配列として述語を挿入

                if dep_type == 'nsubj':
                    # 0番目に主語を挿入
                    dep_dict[idx].insert(0, dep.findall('dependent')[0].text)
                else:
                    # 2番目に目的語を挿入
                    dep_dict[idx].append(dep.findall('dependent')[0].text)

        for key, value in dep_dict.items():
            if len(value) == 3:
                print('\t'.join(value))


if __name__ == '__main__':
    main()

# understanding   enabling        computers
# others  involve generation
# Turing  published       article
# experiment      involved        translation
# ELIZA   provided        interaction
# patient exceeded        base
# ELIZA   provide response
# which   structured      information
# underpinnings   discouraged     sort
# that    underlies       approach
# Some    produced        systems
# which   make    decisions
# systems rely    which
# that    contains        errors
# implementations involved        coding
# algorithms      take    set
# Some    produced        systems
# which   make    decisions
# models  have    advantage
# they    express certainty
# Systems have    advantages
# Automatic       make    use
# that    make    decisions
