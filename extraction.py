from pypinyin import pinyin, lazy_pinyin, Style
import json
import random

commandfilename = 'commandSet.json'
f = open(commandfilename, 'r', encoding='utf8')
command_dict = json.loads(f.read(), encoding='utf8')
f.close()
command_set = []
general_class = command_dict.keys()
for general_command in general_class:
    print(general_command)
    specific_class = command_dict[general_command].keys()
    for specific_command in specific_class:
        commands = command_dict[general_command][specific_command]['commands']
        # exit(0)
        if len(commands) > 5:
            command_set.extend(random.sample(list(commands), 5))
        else:
            command_set.extend(commands)

print('command set count: ', len(command_set))    

filename = 'corpus_new.txt'
f = open(filename, 'r', encoding='utf8')
lines = f.readlines()
f.close()

corpus_dict = {}
corpus_cover = {}
sentences = []

for line in lines:
    line = line.replace('\n', '')
    chac = line[0]
    if not (chac >= '\u4e00' and chac <= '\u9fa5'):
        corpus_dict[line] = []
        corpus_cover[line] = 0
    else:
        sentences.append(line)

corpus = corpus_dict.keys()
corpus_dict['zhua'] = []
corpus_dict['chai'] = []
corpus_dict['nve'] = []
corpus_dict['shei'] = []
corpus_cover['zhua'] = 0
corpus_cover['chai'] = 0
corpus_cover['nve'] = 0
corpus_cover['shei'] = 0
print(len(corpus))

count = 0
for sentence in sentences:
    # count = count + 1
    # if count == 3:
    #     break
    pinyins = lazy_pinyin(sentence)
    for py in pinyins:
        if py in corpus:
            if not sentence in corpus_dict[py]:
                corpus_dict[py].append(sentence)
        else:
            print('error ', py, sentence, pinyins)

sorted_corpus = sorted(corpus_dict.items(), key=lambda d: len(d[1]))

extraction_set = []

cover_count = 0
cover_limit = 385#397

for corpus_pair in sorted_corpus:
    # print(corpus_pair[0], len(corpus_pair[1]))
    sentences = corpus_pair[1]
    for sentence in sentences:
        if sentence in extraction_set:
            continue
        extraction_set.append(sentence)
        pinyins = lazy_pinyin(sentence)
        for py in pinyins:
            corpus_cover[py] = corpus_cover[py] + 1
            if corpus_cover[py] == 10:
                cover_count = cover_count + 1
        if len(extraction_set) == 2000:
            break
    if len(extraction_set) == 2000:
        break

print(len(extraction_set))

extraction_set.extend(command_set)

print(len(extraction_set))

outputfilename = 'output.txt'
f = open(outputfilename, 'w', encoding='utf8')
for sentence in extraction_set:
    f.write(sentence)
    f.write('\n')
f.close()

# print(corpus_pair[0], len(corpus_pair[1]))


# yinjiefilename = 'yinjie.txt'
# f = open(yinjiefilename, 'r', encoding='utf8')
# lines = f.readlines()
# yinjies = []
# for line in lines:
#     segments = line.split(' ')
#     for segment in segments:
#         segment = segment.replace('\n', '')
#         if len(segment) != 0:
#             yinjies.append(segment)
# print(yinjies)

# for yinjie in yinjies:
#     if not yinjie in corpus:
#         print(yinjie)
'''
pinyin not in index:
chai
chua
dei
den
dia
ei
eng
fiao
kei
lo
lue
nou
nue
nun
o
rua
shei
tei
yo
zhei
zhua
'''
    