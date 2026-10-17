class TimeMap:

    def __init__(self):
        self.array = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.array.get(key, None):
            self.array[key].append([timestamp, value])
        else:
            self.array[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if self.array.get(key, None):
            l, r = 0, len(self.array[key]) - 1
            while l < r:
                m = int((l + r + 1) / 2)
                if self.array[key][m][0] > timestamp:
                    r = m - 1
                elif self.array[key][m][0] < timestamp:
                    l = m 
                else:
                    return self.array[key][m][1]
            
            if l == 0 and self.array[key][l][0] > timestamp:
                return ''

            return self.array[key][l][1]
        else:
            return ''