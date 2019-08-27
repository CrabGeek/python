from Stackpy import Stack
from atexit import register







def balance_parent(data):
    stack = Stack(len(data))

    for i in data:
        if i == '(':
            stack.push(i)
        elif i == ')':
            if stack.is_empty():
                return False
            stack.pop()

    return stack.is_empty()


def main():
    data = ['((()))', '((())']

    for i in data:
        print(i + ': ' + str(balance_parent(i)))



if __name__ == '__main__':
    main()