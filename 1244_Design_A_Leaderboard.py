class Leaderboard:

    def __init__(self):
        self.leaders = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaders:
            self.leaders[playerId] = score
        else:
            self.leaders[playerId] += score
        

    def top(self, K: int) -> int:
        return sum(heapq.nlargest(K, self.leaders.values()))
        

    def reset(self, playerId: int) -> None:
        if playerId in self.leaders:
            self.leaders[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)