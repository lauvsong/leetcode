class Solution:
    def search(self, nums, target) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            # left portion
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
                




        

def test(nums, target):
    sol = Solution()
    res = sol.search(nums, target)
    print(res)

test([4,5,6,7,0,1,2], 0)
test([4,5,6,7,0,1,2], 3)
test([1], 0)

"""

이진 탐색

- 0번째 인덱스 확인
- target보다 클 시
    - 
- target 보다 작을 시
    - 

"""