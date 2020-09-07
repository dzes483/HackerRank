def count_substring(string, sub_string):
    count = 0
    start = 0
    end = len(sub_string)
    for i in range(len(string)):
        result = string.find(sub_string, start, end)
        if result != -1:
            count += 1
        start += 1
        end += 1
    return count



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
