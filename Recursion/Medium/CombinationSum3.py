class Solution:
  def poss(self, sum, last, curr, ans, k):
    if sum == 0 and len(curr) == k:
      ans.append(curr[:])
      return
  
    if sum <= 0 or len(curr) > k:
      return 
    
    for i in range(last, 10):
      if i <= sum:
        curr.append(i)
        self.poss(sum - i,i + 1, curr, ans, k)
        curr.pop()
      else:
        break
    
  def combinationSum3(self, k, n):
    ans = []
    curr = []
    self.poss(n,1,curr,ans,k)
    return ans