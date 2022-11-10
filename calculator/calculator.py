import sys
input1 = input('Choose a number:' )
input2 = input('Choose another number: ')
operand = input('Choose an operator: ')


try:
    float(input1)
except ValueError:
    print("First number invalid. Choose a number next time.")
    sys.exit()

try:
    float(input2)
except ValueError:
    print("Second number invalid. Choose a number next time.")
    sys.exit()

num1 = float(input1)
num2 = float(input2)

def add(num1, num2):
    answer = num1 + num2
    return answer

def sub(num1, num2):
    answer = num1 - num2
    return answer

def mult(num1, num2):
    answer = num1 * num2
    return answer

def div(num1, num2):
    answer = num1 / num2
    return answer

if (operand == '+'):
    print(mult(num1, num2))
elif (operand == '-'):
    print(sub(num1, num2))
elif (operand == "*"):
    print(mult(num1, num2))
elif (operand == "/"):
    print(div(num1, num2))
else:
    print('Invalid operator chosen. Choose either +, -, /, or *.')
