class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        fast, slow = 0, 0
        
        while True:
            
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if fast == slow: 
                break
        
        temp = 0
        while True:
            
            if nums[slow] == nums[temp]:
                return nums[slow]
            
            slow = nums[slow]
            temp = nums[temp]

