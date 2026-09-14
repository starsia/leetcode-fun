class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_balance = 0
        current_tank = 0
        index = 0

        for i in range(len(gas)):
            total_balance += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                print(index)
                current_tank = 0
                index = i + 1

        if total_balance < 0:
            return -1

        else:
            return index

