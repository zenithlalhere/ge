class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

# Evaluate a postfix expression
def evaluate_postfix(expression):
    stack = Stack()
    for char in expression.split():
        if char.isdigit():
            stack.push(int(char))
        else:
            right = stack.pop()
            left = stack.pop()
            if char == '+':
                stack.push(left + right)
            elif char == '-':
                stack.push(left - right)
            elif char == '*':
                stack.push(left * right)
            elif char == '/':
                stack.push(left / right)
    return stack.pop()

# Evaluate a prefix expression
def evaluate_prefix(expression):
    stack = Stack()
    for char in reversed(expression.split()):
        if char.isdigit():
            stack.push(int(char))
        else:
            left = stack.pop()
            right = stack.pop()
            if char == '+':
                stack.push(left + right)
            elif char == '-':
                stack.push(left - right)
            elif char == '*':
                stack.push(left * right)
            elif char == '/':
                stack.push(left / right)
    return stack.pop()

# Example usage
postfix = "5 6 2 + *"     # Equivalent to 5 * (6 + 2) = 40
prefix = "* 5 + 6 2"      # Same expression

print("Postfix Evaluation:", evaluate_postfix(postfix))
print("Prefix Evaluation:", evaluate_prefix(prefix))
