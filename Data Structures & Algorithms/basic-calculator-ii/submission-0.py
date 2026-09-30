class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        num = 0
        op = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if not char.isdigit() or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop()/num))
                op = char
                num = 0

        return sum(stack)
