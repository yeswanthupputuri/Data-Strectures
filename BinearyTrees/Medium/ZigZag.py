from collections import deque
class Solution:
    def zigZaglevelorder(self, root):
        result = []
        if not root:
            return result 
        q = deque([root])
        direction = True
        while q:
            size = len(q)
            row = [0] * size
            for i in range(size):
                node = q.popleft()
                index = i if direction else (size - 1 - i)
                row[index] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            direction = not direction
            result.append(row)
        return result
