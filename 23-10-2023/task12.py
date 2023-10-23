menu = [1,2,3,4,5]

def find_number(num):
    
        return num*2
    
filter_number = map(find_number,menu)
print(filter_number)
for x in filter_number:
    print(x)