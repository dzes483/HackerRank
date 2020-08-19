import textwrap

def merge_the_tools(string, k):
    for segment in textwrap.wrap(string, k):
        print(''.join(dict.fromkeys(segment)))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
