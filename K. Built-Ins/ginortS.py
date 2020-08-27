s = list(input())
lc = sorted([i for i in s if i.islower()])
uc = sorted([i for i in s if i.isupper()])
odds = sorted([i for i in s if i.isdigit() and int(i) % 2 != 0])
evens = sorted([i for i in s if i.isdigit() and int(i) %2 == 0])


print(''.join(lc + uc + odds + evens))
