lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

result = []

for x in lst:
    if x < 5:
        result.append(x)

print("Numbers less than 5:", result)
