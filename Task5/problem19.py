# Merge the Tools!
#   https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        substring = s[i:i+k]
        result = ""

        for char in substring:
            if char not in result:
                result += char

        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
