# You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

# Each minute, a node becomes infected if:

# The node is currently uninfected.
# The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # convert to a undirected graph
        adj = defaultdict(list)
        q = deque([root])
        while q:
            n = q.popleft()
            if n.left:
                adj[n.val].append(n.left.val)
                adj[n.left.val].append(n.val)
                q.append(n.left)
            if n.right:
                adj[n.val].append(n.right.val)
                adj[n.right.val].append(n.val)
                q.append(n.right)

        # BFS with HashSet
        q = deque([(start, 0)])
        res = 0
        visited = set()
        while q:
            i, depth = q.popleft()
            res = max(res, depth)
            visited.add(i)
            for a in adj[i]:
                if a not in visited: q.append((a, depth + 1))
        return res