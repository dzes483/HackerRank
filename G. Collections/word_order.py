from collections import OrderedDict, Counter

n = int(input())
word_list = []
for _ in range(n):
    word_list.append(input())

word_dict = OrderedDict(Counter(word_list))

print(len(word_dict))
for k, v in word_dict.items():
    print(v, end=' ')
