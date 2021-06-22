import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        priority_queue = []
        
        for num in nums:
            heapq.heappush(priority_queue, (-1*num, num))
        
        for i in range(k-1):
            item = heapq.heappop(priority_queue)
            # print(item)
        k_th_largest = heapq.heappop(priority_queue)
        return k_th_largest[1]
        
if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    sol = Solution()
    print(sol.findKthLargest(nums, k))