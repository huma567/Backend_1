message= "A kong string with a silly typo"
message[2]= "l"

Traceback (most recent call last):
File "<stdin>", line 1, in <module>

TypeError: 'str' object does not support item assignment
new_message = message[0:2] + "l" + message[3:]
print(new_message)