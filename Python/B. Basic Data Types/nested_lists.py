if __name__ == '__main__':
    students = []

    # Add the students' names and their scores to the list.
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Add the scores to a list, then change this into a set, to get rid of
    # duplicates.
    scores = []
    for i in students:
        for name, score in students:
            scores.append(score)
    score_set = set(scores)

    # Remove the lowest score from the set.
    score_set.remove(min(score_set))
    # Retrieve the second lowest score from the set.
    second_lowest = min(score_set)

    # Add the names of those with the second-lowest scores to a set, sort it,
    # then print the names.
    second_lowest_scores = []
    for i in students:
        for name, score in students:
            if score == second_lowest:
                second_lowest_scores.append(name)
    sorted_set = sorted(set(second_lowest_scores))
    for i in sorted_set:
        print(i)
