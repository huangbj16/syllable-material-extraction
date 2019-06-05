from pypinyin import pinyin, lazy_pinyin, Style

print(lazy_pinyin('咋了？这是什么情况'))

# obj >= '\u4e00' and obj <= '\u9fa5' 
filename = 'corpus.txt'
newfilename = 'corpus_new.txt'
f = open(filename, 'r', encoding='utf8')
lines = f.readlines()
f.close()
g = open(newfilename, 'w', encoding='utf8')
for line in lines:
    for chac in line:
        if chac >= '\u4e00' and chac <= '\u9fa5':
            g.write(chac)
        elif chac >= 'a' and chac <= 'z':
            g.write(chac)
        elif chac >= 'A' and chac <= 'Z':
            g.write(str.lower(chac))
        else:
            print(chac)
    g.write('\n')

g.close()