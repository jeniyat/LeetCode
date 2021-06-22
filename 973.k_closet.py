import math
import heapq

class Solution(object):
    def find_distance(self, p1, p2):
        x_diff = (p1[0]-p2[0])*(p1[0]-p2[0])
        y_diff = (p1[1]-p2[1])*(p1[1]-p2[1])
        return math.sqrt(x_diff+y_diff)
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        priority_queue = []
        origin = [0,0]
        for p in points:
            dist = self.find_distance(origin, p)
            heapq.heappush(priority_queue, (dist,p))
        coloset_points = []
        for i in range(k):
            (dist, point) = heapq.heappop(priority_queue)
            coloset_points.append(point)
        return coloset_points

if __name__ == '__main__':
    points = [[1,3],[-2,2]]
    k = 1
    sol = Solution()
    print(sol.kClosest(points, k))