num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

count = 0

for index, num in enumerate(num_list):
    if num == 36:
        print("Number found at position:", index)
        count += 1
        break
    count += 1

print("Total count of number 36:", count)