class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        result = 0
        for el in tokens:
            if len(el) == 1 and el in '+*-/':
                num2 = s.pop()
                num1 = s.pop()
                match el:
                    case '+':
                        result = num1 + num2
                    case '-':
                        result = num1 - num2
                    case '/':
                        result = int(num1/num2)
                    case '*':
                        result = num1 * num2
                s.append(result)
            else:
                s.append(int(el))
        return s[-1]