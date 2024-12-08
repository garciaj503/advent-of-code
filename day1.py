import math

with open("day1_input.txt") as file:
    data = file.read()
# Process the data to create two lists
first_column = []
second_column = []

# Split the data into lines and then into columns
for line in data.strip().split("\n"):
    col1, col2 = line.split()
    first_column.append(int(col1))
    second_column.append(int(col2))

first_column.sort()
second_column.sort()

total_sum = 0
i = 0
while i < len(first_column):
    total_sum += abs(first_column[i] - second_column[i])
    i += 1

print(total_sum)

similarity = 0
for value in first_column:
    how_many_times = second_column.count(value)
    similarity += value * how_many_times

print(similarity)




   

