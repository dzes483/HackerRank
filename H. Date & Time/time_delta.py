import datetime

for _ in range(int(input())):
    t_1 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    t_2 = datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    diff = abs(t_1 - t_2)
    print(int(divmod(diff.total_seconds(), 1)[0]))
