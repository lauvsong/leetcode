class Solution:

    def isOverlapped(self, interval, newInterval):
        if interval[1] < newInterval[0]: return False
        if newInterval[1] < interval[0]: return False
        
        return True
    
    def merge_interval(self, interval, newInterval):
        return [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        newInterval = intervals[0]

        for i in range(len(intervals)):
            if self.isOverlapped(intervals[i], newInterval):
                ans.pop()
                newInterval = self.merge_interval(intervals[i], newInterval)
            else:
                newInterval = intervals[i]
            
            ans.append(newInterval)
            
        return ans
    

sol = Solution()
res = sol.merge([[1,3],[2,6],[8,10],[15,18]])
print(res)

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""