class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                item_2 = stack.pop()
                item_1 = stack.pop()

                if token == "+":
                    output = item_1 + item_2
                    stack.append(output)
                elif token == "-":
                    output = item_1 - item_2
                    stack.append(output)
                elif token == "*":
                    output = item_1 * item_2
                    stack.append(output)
                else:
                    output = int(item_1 / item_2)
                    stack.append(output)

                continue
                
            stack.append(int(token))

                    
        return stack[0]

