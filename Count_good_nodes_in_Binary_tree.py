'''PRoblem : Count Good Nodes In Binary Tree '''

#CODE :

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        n_good_nodes = 0
        queue = deque([(root, float(-inf))])
        while queue:
            node, maximum = queue.popleft()
            if not node: continue
            if node.val >= maximum:
                maximum = node.val
                n_good_nodes += 1
            queue.append((node.right, maximum)), queue.append((node.left, maximum))
        return n_good_nodes
