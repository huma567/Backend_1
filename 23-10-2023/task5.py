def divide_by(a,b):
    return a/b
try:
 print(divide_by(40,0))
except Exception as e:
    print("something wenk wrong!",e)