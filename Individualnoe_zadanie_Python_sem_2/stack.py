class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0


def evaluate(expr):
    stack = Stack()
    i = 0
    while i < len(expr):
        c = expr[i]
        if c in 'mM':
            stack.push(c)
            i += 1
        elif c.isdigit():
            num = ''
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            stack.push(int(num))
        elif c == ')':
            b = stack.pop()
            a = stack.pop()
            op = stack.pop()
            stack.push(min(a, b) if op == 'm' else max(a, b))
            i += 1
        else:
            i += 1
    return stack.pop()