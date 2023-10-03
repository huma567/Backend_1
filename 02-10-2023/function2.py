my_global = 10

def fn1():
    local_v = 5
    print('Access to global', my_global)

print('Cant access local', my_global)