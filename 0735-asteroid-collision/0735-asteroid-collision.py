class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack=[]
        for ch in asteroids:
            while stack and  stack[-1]>0 and ch<0:
                if stack [-1]< abs(ch):
                    stack.pop()

                elif stack[-1]==abs(ch):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(ch)
        return stack