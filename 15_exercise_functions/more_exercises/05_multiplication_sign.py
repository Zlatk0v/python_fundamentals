def check_sign(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "zero"
    negative_count = 0
    if a < 0:
        negative_count += 1
    if b < 0:
        negative_count += 1
    if c < 0:
        negative_count += 1
    if negative_count % 2 == 1:
        return "negative"
    else:
        return "positive"


first = int(input())
second = int(input())
third = int(input())
print(check_sign(first, second, third))
