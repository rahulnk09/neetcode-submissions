from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(lambda: ([], []))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][0].append(value)
        self.store[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.store[key][1]
        print(timestamps)
        prev_smallest_timestamp_idx = -1
        l = 0
        r = len(timestamps) - 1

        while l <= r:
            m = (l + r) // 2
            print("l", timestamps[l])
            print("m", timestamps[m])
            print("r", timestamps[r])
            print("prev_smallest_timestamp_idx", prev_smallest_timestamp_idx)
            print(self.store[key][0][m])

            if timestamps[m] == timestamp:
                return self.store[key][0][m]

            if timestamp <= timestamps[m]:
                r = m - 1
            else:
                prev_smallest_timestamp_idx = m
                l = m + 1

        print("prev_smallest_timestamp_idx", prev_smallest_timestamp_idx)
        print(self.store[key][0])
        return (
            self.store[key][0][prev_smallest_timestamp_idx]
            if (prev_smallest_timestamp_idx >= 0 and self.store[key][1][prev_smallest_timestamp_idx] < timestamp)
            else ""
        )
