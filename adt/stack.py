
# funktional - python
# push and pop take a
# stack as parameter and return
# a new stack
# run with pytest


def pop(stack):
    new_stack = []
    for x in stack[1:]:
        new_stack.append(x)
    return new_stack


def push(stack, e):
    new_stack = []
    new_stack.append(e)
    for x in stack:
        new_stack.append(x)
    return new_stack


def top(stack):
    return stack[0]


def test_push():
    stack = [1, 2, 3, 4]
    assert [5, 1, 2, 3, 4] == push(stack, 5)


def test_pop():
    stack = [1, 2, 3, 4]
    assert [2, 3, 4] == pop(stack)


def test_top():
    stack = [1, 2, 3, 4]
    assert 1 == top(stack)
