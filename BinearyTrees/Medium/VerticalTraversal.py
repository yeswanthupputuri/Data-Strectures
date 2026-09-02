from collections import deque, defaultdict
class Solution:
    def verticaltraversal(self, root):
        if not root:
            return []
        nodes_map = defaultdict(lambda: defaultdict(list))
        queue = deque([root, 0, 0])
        while queue:
            node, x, y = queue.popleft()
            nodes_map[x][y].append(node.data)
            if node.left:
                queue.append((node.left, x - 1, y + 1))
            if node.right:
                queue.append((node.right, x + 1, y + 1))
        
        result = []
        
        for x in sorted(nodes_map):
            col = []
            for y in sorted(nodes_map[x]):
                col.extend(sorted(nodes_map[x][y]))
            result.append(col)
        return result
        