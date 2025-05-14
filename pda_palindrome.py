class PDA:
    def accepts(self, input_string: str) -> bool:
        n = len(input_string)
        if n % 2 == 0:
            return False  # Must be odd length

        stack = []
        mid = n // 2

        # Push first half onto stack
        for i in range(mid):
            stack.append(input_string[i])

        # Skip middle character
        for i in range(mid + 1, n):
            if not stack or stack.pop() != input_string[i]:
                return False

        return len(stack) == 0
