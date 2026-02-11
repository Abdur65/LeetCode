class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for ops in logs:
            if ops == "./":
                continue
            elif ops == "../":
                if depth > 0:
                    depth -= 1
            else:
                depth += 1

        return depth