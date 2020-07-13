import calendar

date = [int(i) for i in input().split()]

print(list(calendar.day_name)[calendar.weekday(date[-1],
                                               date[0],
                                               date[1])].upper())
