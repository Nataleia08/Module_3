def f1():
    set1 = {1, 2, 3}
    set1.add(4)
    print(set1)


def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)


def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')


def count_items(item_list):
    """Recursion function count items from list"""
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_items(list)
        else:
            count += 1
    return count


def is_palindrome_1(word: str):
    """Return True if word is palindrom"""

    return word == word[::-1]


def is_palindrome_2(string):
    return string == ''.join(reversed(string))


def is_palindrome_3(word: str):
    """Return True if word is palindrom"""

    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_3(word[1:-1])


if __name__ == '__main__':
    print("You imported function.py")
    # f1()
