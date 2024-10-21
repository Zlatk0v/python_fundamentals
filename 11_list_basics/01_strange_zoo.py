# input
tail = input()
body = input()
head = input()

# logic
meerkat = [tail, body, head]

# swapping
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

# output
print(meerkat)
