class TimeMap:
    # Binary search on hashmap
    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Set key = [value, timestamp]
        # Append new timestamps & values if exists.
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        # Get matching Vals and then search for most recent timeStamp
        matching_vals = self.time_map.get(key, [])
        l,r = 0, len(matching_vals) - 1
        res = ''
        while l <= r:
            m = (l + r ) // 2
            # We take the mid each time as times are ascending
            # It will eventually return most recent
            if matching_vals[m][1] <= timestamp:
                res = matching_vals[m][0]
                l = m + 1
            else:
                r = m - 1
        return res            
        

