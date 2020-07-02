import string

alphabet = string.ascii_lowercase

def print_rangoli(size):
    rows = []
    for num in range(size):
        # Create chunks of the alphabet from max-size to smallest.
        chunk = '-'.join(alphabet[num:size])
        # Combine the chunks, slicing out the extra letter & append them to rows.
        rows.append(chunk[::-1] + chunk[1:])
        # The maximum width of the figure will be the longest chunk in rows.
        max_width = len(rows[0])
    for num in range(size-1, 0, -1): # backwards/top half
        print(rows[num].center(max_width, '-'))
    for num in range(size):          # forwards/ bottom half
        print(rows[num].center(max_width, '-'))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
