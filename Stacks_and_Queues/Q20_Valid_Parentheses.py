# using deque O(1)
class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        correctPair = dict(('()', '[]', '{}'))
        stack = deque() # deque
        for i in s:
            if i in "([{":
                stack.append(i)
            elif len(stack) == 0 or i != correctPair[stack.pop()]:
                return False
        return len(stack) == 0

#using list O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        correctPair = dict(('()', '[]', '{}'))   # {'(': ')', '[': ']', '{': '}'}
        stack = []. # list
        for i in s:
            if i in "([{":
                stack.append(i)
            elif len(stack) == 0 or i != correctPair[stack.pop()]:
                return False
        return len(stack) == 0

#using queue
class Solution:
    def isValid(self, s: str) -> bool:
        import queue
        correctPair = dict(('()', '[]', '{}'))
        stack = queue.LifoQueue()
        for i in s:
            if i in "([{":
                stack.put(i)
            elif stack.qsize() == 0 or i != correctPair[stack.get()]:
                return False
        return stack.qsize() == 0
