class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        unsorted_traffic = list(zip(position, speed))

        sorted_traffic = [(target - position) / speed for position, speed in sorted(unsorted_traffic)]

        print(sorted_traffic)

        fleets = 0
        fleet_timing = 0

        while sorted_traffic:
            time = sorted_traffic.pop()
            if time > fleet_timing:
                fleets += 1
                fleet_timing = time

        return fleets
