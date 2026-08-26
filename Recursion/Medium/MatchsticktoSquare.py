class Solution:
    def makesquare(self, matchsticks):
        total = sum(matchsticks)
        side = total // 4
        if total % 4 != 0:
            return False 
        matchsticks.sort(reverse=True)
        if matchsticks[0] > side:
            return False 
        sides = [0] * 4 
        
        return self.possible(0, side, sides, matchsticks)
    
    def possible(self, index, side, sides, matchsticks):
        if index == len(matchsticks):
            return True
        stick = matchsticks[index]
        
        for i in range(4):
            if sides[i] + stick > side:
                continue
            if i > 0 and sides[i] == sides[i - 1]:
                continue
            sides[i] += stick
            if self.possible(index + 1, side, sides, matchsticks):
                return True 
            sides[i] -= stick 
            if sides[i] == 0:
                break 
        return False
            