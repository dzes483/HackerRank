
num_students, num_subjects = [int(i) for i in (input().split())]

subject_scores = []
for num in range(num_subjects):
    subject_scores.append([float(i) for i in (input().split())])

z = zip(*subject_scores)
for i in z:
    print(sum(i)/num_subjects)
