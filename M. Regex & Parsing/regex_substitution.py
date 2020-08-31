import re

pipe_regex = re.compile(r"(?<!\|)(?<=\s)\|\|(?=\s)(?!\|)")
ampersand_regex = re.compile(r"(?<!&)(?<=\s)&&(?=\s)(?!&)")

n = int(input())
for _ in range(n):
    s = input()
    s = re.sub(pipe_regex, 'or', s)
    s = re.sub(ampersand_regex, 'and', s)
    print(s)
