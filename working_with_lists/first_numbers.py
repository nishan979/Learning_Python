#1 numbers
for value in range(1, 6):
    print(value)

#2 making list using range
numbers = list(range(1,6))
print(numbers)

#3 even numbers
even_numbers  = list(range(2, 11, 2))
print(even_numbers)

#4 square numbers
squares = []
for value1 in range(1,11):
    # square = value1**2
    # squares.append(square)
    squares.append(value1**2)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))