# Declare and initialize a list (acts like an array)
numbers = [10, 20, 30, 40, 50]

# Access elements using index
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Traverse the list using a loop
print("\nArray Elements:")
for i in range(len(numbers)):
    print("Index", i, "->", numbers[i])

# Update an element
numbers[2] = 99
print("\nAfter updating index 2:")
for num in numbers:
    print(num, end=" ")
