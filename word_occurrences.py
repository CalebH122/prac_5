WORD_DIC = {}
line = input("Enter your line: ")
words = line.split()
for word in words:
    WORD_DIC[word] = WORD_DIC.get(word, 0) + 1

length = len(max(words))
sorted_dic = sorted(WORD_DIC)

for word in sorted_dic:
    print(f"{word:{length}} : {WORD_DIC[word]}")
