from collections import defaultdict

class TimeMap:
    def __init__(self):
        # Automatically initializes an empty list for any new key
        self.status = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # No if/else needed! Just append.
        self.status[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Direct dictionary lookup
        if key not in self.status:
            return ""

        values = self.status[key]
        ans = ""
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                r = mid - 1
            else:
                ans = values[mid][1]
                l = mid + 1

        return ans