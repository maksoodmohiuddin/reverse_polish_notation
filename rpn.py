def answer(str):
    rpn = ''
    numbers = []
    add = []
    multi = []

    for s in str:
        if s == '+':
            add.append(s)
        elif s == '*':
            multi.append(s)
        else:
            numbers.append(s)

        if len(numbers) > 1 and s == '+' and len(multi) > 0:
            rpn += ''.join(numbers)
            numbers[:] = []
            rpn += ''.join(multi)
            multi[:] = []

    if len(numbers) > 0:
        rpn += ''.join(numbers)
        numbers[:] = []

    if len(multi) > 0:
        rpn += ''.join(multi)
        multi[:] = []

    if len(add) > 0:
        rpn += ''.join(add)
        add[:] = []

    return rpn

test1 = "2+3*2"
print answer(test1)
# "232*+"

test2 = "2*4*3+9*3+5"
print answer(test2)
# "243**93*5++"