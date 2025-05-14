class PDA:
    def accepts(self, input_string: str) -> bool:
        n = len(input_string)
        if n % 2 == 0:
            return False  

        stack = []
        mid = n // 2

        
        for i in range(mid):
            stack.append(input_string[i])

        
        for i in range(mid + 1, n):
            if not stack or stack.pop() != input_string[i]:
                return False

        return len(stack) == 0
