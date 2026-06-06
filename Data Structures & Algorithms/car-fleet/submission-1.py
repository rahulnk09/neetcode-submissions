class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Quick edge case check
        if not position:
            return 0
            
        # zip() pairs them up: [(pos1, speed1), (pos2, speed2)...]
        # sorted(..., reverse=True) sorts them by position in descending order automatically
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        slowest_time_ahead = 0.0 # This replaces your stack[-1]
        
        for p, s in cars:
            time = (target - p) / s
            
            # If this car's time is strictly greater, it CANNOT catch up.
            # Therefore, it forms a brand new fleet, and becomes the new slowest_time_ahead.
            if time > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = time
                
            # If time <= slowest_time_ahead, it catches up. 
            # We do nothing, effectively merging it into the current fleet.
            
        return fleets