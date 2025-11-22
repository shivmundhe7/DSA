
numbers = [10, 20, 30, 40, 50]


print("First element:", numbers[0])
print("Last element:", numbers[-1])


print("\nArray Elements:")
for i in range(len(numbers)):
    print("Index", i, "->", numbers[i])


numbers[2] = 99
print("\nAfter updating index 2:")
for num in numbers:
    print(num, end=" ")
