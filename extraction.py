from pypinyin import pinyin, lazy_pinyin, Style

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
cover_limit = 385

for corpus_pair in sorted_corpus:
    print(corpus_pair[0], len(corpus_pair[1]))
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
        if cover_count >= cover_limit:
            break
    if cover_count >= cover_limit:
        break

print(len(extraction_set))

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
    