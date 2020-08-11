from collections import namedtuple

num_students = int(input())
total = 0
Row = namedtuple('Row', (i for i in (input().split())))

for n in range(num_students):
    student_marks = [i for i in (input().split())]
    fill = Row(student_marks[0], student_marks[1], student_marks[2], student_marks[3])
    total += int(fill.MARKS)
    
print('{:.2f}'.format(total/num_students))
