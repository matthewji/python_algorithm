# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# my solution
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        count = [0, 0]

        def search(node, idx):
            if node:
                count[idx] += 1
            if node.left:
                search(node.left, 1 - idx)
            if node.right:
                search(node.right, 1 - idx)

        search(root, 0)

        if count[0] == 0 and count[1] == 0:
            return None
        elif count[0] == 0:
            return count[1]
        elif count[1] == 0:
            return count[0]
        else:
            return min(count)
# Status: Wrong Answer
# Algorithm: Recursion
# Time Complexity: O(n)
# Runtime:
# Intuition: 아이디어 자체가 틀렸다.
#            홀수레벨 노드의 합과 짝수레벨 노드의 합 중 작은 값을 return 했는데 반례가 있음
#            [0,0,null,null,0,0,null,null,0,0]

# 코드만 놓고 보자면 위에 recursion은 잘 짰고 밑에 0인 요소를 제외하고 min 값을 도출해낼 때는 더 간결하게 쓸 수 있을 것 같은데 어떻게 하지?

# leetcode solution을 봤는데 아직 hard는 도전하지 않는걸로..