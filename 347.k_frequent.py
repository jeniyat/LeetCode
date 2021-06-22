import heapq
from collections import Counter
class Solution(object):
    
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_frequency = Counter()
        
        for num in nums:
            num_frequency[num]+=1
            
        # print(num_frequency)
        priority_queue = []
        
        #heapq is min-heap structure, multiplying with -1 to make it max-heap
        
        for num in num_frequency:
            heapq.heappush(priority_queue, (-1*num_frequency[num], num))
            
        # print(priority_queue)
        
            
        output_list = []
        for i in range(k):
            if len(priority_queue)==0:
                break
            item = heapq.heappop(priority_queue)
            num = item[1]
            output_list.append(num)
            
        return output_list
if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(nums, k))