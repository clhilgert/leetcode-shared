class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) >= 2:
                if stack[-2] < 0 or stack[-1] > 0:
                    break
                right, left = stack.pop(), stack.pop()
                if left > abs(right):
                    stack.append(left)
                elif left < abs(right):
                    stack.append(right)
        return stack

        # time O(n)
        #space O(n)