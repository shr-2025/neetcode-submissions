class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for el in tokens:
            if el in '+*-/':
                num2 = s.pop()
                num1 = s.pop()
                match el:
                    case '+':
                        s.append(num1 + num2)
                    case '-':
                        s.append(num1 - num2)
                    case '/':
                        s.append(int(num1/num2))
                    case '*':
                        s.append(num1 * num2)
            else:
                s.append(int(el))
        return s[-1]