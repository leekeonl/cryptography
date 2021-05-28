def productExceptSelf(nums):
  size = len(nums)
  L = []
  # total = 1
  for i in range(size):
    total = 1
    for j in range(size):
      if nums[i] != nums[j]:
        total *= nums[j]
    L.append(total)
  return L

def productExceptSelf(nums):
  size = len(nums)
  L = []
  # total = 1
  for i in range(size):
    total = 1
    for j in range(size):
      total *= nums[j]
      if nums[i]== nums[j]:
        total /= nums[j]
    L.append(total)
  return L


L = [1,2,3,4]
print(productExceptSelf(L))


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
            n = len(nums)
            curr_sum = max_sum = nums[0]
            
            for i in range(1, n):
                curr_sum = max(nums[i], curr_sum + nums[i]) 
                max_sum = max(max_sum, curr_sum)
            
            return max_sum
        
# current array
# [-2,1,-3,4,-1,2,1,-5,4]