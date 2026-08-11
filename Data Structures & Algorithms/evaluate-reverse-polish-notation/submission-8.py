class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        result = 0
        for el in tokens:
            if el in '+*-/':
                num2 = int(s.pop())
                num1 = int(s.pop())
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
                s.append(el)
        return int(s[0])