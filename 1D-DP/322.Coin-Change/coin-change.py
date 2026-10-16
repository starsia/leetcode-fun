class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort()
        
        point = len(coins) - 1
        output = 0 
        
        if point == -1:
            return -1
        
        while point >=0:
            if point == 0 and amount % coins[point] != 0 :
                return -1
                
            remainder = amount // coins[point] 
            
            output += remainder
            amount -= remainder * coins[point]
            point -= 1
            
            
                
            print(output, amount)
        
                
        return output
                
