#!/usr/bin/env python3

message = 'Test your moral character! '

# wrap connection in a float() to accept decimals as numbers
character = float(input("What is your moral chracter? Select 1 , 2 , 3"))

# if input value was higher or equal to 25
if character  == 1:
    message = message + 'you are Simon Cowell'
elif character == 2:
    message = message + 'you are Taylor Swift'
elif character == 3:
    message = message + 'you are Kanye West'
elif character >= 4:
    message = message + '...you have no moral character'
else:
    message = message + 'You surely failed this quiz'
print(message)
