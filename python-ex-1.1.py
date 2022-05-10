
defuser = 'magician'
defpassword = 'lovesbirds'
while(True):
    user = input('user name:')
    password = input('password: ')
    if((username == defuser) and (password == defpassword)):
        print('hosgeldiniz', username)
        break
    elif ((username != defuser) and (defpassword == password)):
        print('wrong user name')
    elif((username == defuser) and (password != defpassword)):
        print('did you forgot your passord?')
        print('do you want to update your password?')
        answer = input()
        if(answer == 'E'):
            newpassword = input('new password: ')
            print('wait....')
            defparola = newpassword
            print('your password has been updated...')
    else:
        print('try eagain....')
###########################

factorial =1
while True:
    number = int(input('enter a positive number '))
    if(number <= 0 ):
        print('enter a positive number, please')
    else: 
        for i in range(1, number+1):

            factorial *=i
        print('factorial', factorial)
        break
###########################

def geometry(shape):
    if len(shape) == 3:
        a = shape[0]
        b = shape[1]
        c = shape[2]

        if (a+b) > c and (a+c) > b and (b+c) > a:
            if (a == b) and (a == c) and (b == c):
                print('It is an equilateral triangle.....')
            elif (a == b) and (a == c):
                print('It is an isosceles triangle.....')
            else:
                  print('It is a scalene triangle.....')  
                
    elif len(shape) == 4:
        x = shape[0]
        y = shape[1]
        z = shape[2]
        k = shape[3]

        if (x == y) and (y == z) and (z == k) and (k == x):
            print('It is a square...')
        elif (x == z) and (y == k):
            print('It is a rectangle.....')
        else:
            print('It is a regular quadrilateral.....')

    else:
        print('It is not any shape.....')


while True:
    number_of_elements = int(input('enter the number of elements: '))
    if (shape == 3):
        a = int(input('a: '))
        b = int(input('b: '))
        c = int(input('c: '))
        geometry([a, b, c])

    elif (shape == 4):
        x = int(input('x: '))
        y = int(input('y: '))
        z = int(input('z: '))           
        k = int(input('k: ')) 
        geometry([x, y, z, k])

    else:
        print('please re-enter...')


