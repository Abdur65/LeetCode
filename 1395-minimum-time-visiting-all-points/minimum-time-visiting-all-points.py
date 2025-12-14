class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        if len(points) == 1:
            return 0

        time = 0
        for i in range(len(points)-1):
            x = abs(points[i][0]-points[i+1][0])
            y = abs(points[i][1]-points[i+1][1])
            diff = abs(x-y)
            p = min(x,y)
            time += (diff+p)

        
        return time