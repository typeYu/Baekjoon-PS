import sys

input = sys.stdin.readline

n = int(input().strip())
a = input().strip()
b = input().strip()

vowels = set("aeiou")

def remove_vowels(s):
    return ''.join(ch for ch in s if ch not in vowels)

if (
    sorted(a) == sorted(b)
    and a[0] == b[0]
    and a[-1] == b[-1]
    and remove_vowels(a) == remove_vowels(b)
):
    print("YES")
else:
    print("NO")