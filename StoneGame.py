'''Problem : Stone Game '''

#CODE : 

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if len(piles) % 2 == 0 or len(piles) == 1:
            return True

        dp = [0] * len(piles)
        for i in reversed(range(len(piles))):
            dp[i] = piles[i]
            for j in range(i+1, len(piles)):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        return dp[-1] >= 0
        
