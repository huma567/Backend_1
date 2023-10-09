num_list = [70, 60, 50, 40, 36, 30, 20, 10]


count = 0

for index, num in enumerate(num_list):
    if num == 36:
        print("Number found at position:", index)

print("Total count of number 36:", count)