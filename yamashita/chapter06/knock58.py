import xml.etree.ElementTree as ET

tree = ET.parse('nlp.txt.xml')

for sentence in tree.iterfind('.//sentences/sentence'):
    for nsubj in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep[@type="nsubj"]'):
        for dobj in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep[@type="dobj"]'):
            if nsubj.find('governor').get('idx') != dobj.find('governor').get('idx'):
                continue
            subject = nsubj.find('dependent').text
            predicate = nsubj.find('governor').text
            object_ = dobj.find('dependent').text
            print(f'{subject}\t{predicate}\t{object_}')
