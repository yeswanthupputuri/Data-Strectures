'''  
1. find break element which means of : arr[i] < arr[i + 1]
2.Swap the break point element with the smallest elemnt which lies from next to break-point elemnt to end end of array.
  So buy that it will be next close permutation
3.sort the complemet array [breakpoint next element to - last elemnt ]
'''

class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        index = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        
        if index == -1:
            nums.reverse()
            return
        
        for i in range(n-1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break 
        
        nums[index+1:] = reversed(nums[index+1:])
        return 
            
