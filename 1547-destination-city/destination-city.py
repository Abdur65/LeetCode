class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        count = defaultdict(int)

        for i in range(len(paths)):
            count[paths[i][0]] += 1

        for i in range(len(paths)):
            if count[paths[i][1]] == 0:
                return paths[i][1]
