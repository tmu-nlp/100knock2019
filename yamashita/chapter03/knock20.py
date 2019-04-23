import gzip
import sys
import json

with gzip.open(sys.argv[1],'rt',encoding='utf-8') as input_file:
    for line in input_file:
        json_input = json.loads(line)
        if json_input['title'] == 'イギリス':
            print(json_input['text'])
            with open('Britain.txt','w',encoding='utf-8') as output_file:
                output_file.write(json_input['text'])
