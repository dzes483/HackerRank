
num_students, num_subjects = [int(i) for i in (input().split())]

subject_scores = []
for num in range(num_subjects):
    subject_scores.append([float(i) for i in (input().split())])

for i in zip(*subject_scores):
    print(sum(i)/num_subjects)
