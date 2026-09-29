class TimeMap:

    def __init__(self):
        self.information = {}    

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.information:
            self.information[key] = []
        self.information[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        sol = self.information.get(key, [])

        L, R = 0, len(sol) - 1

        while L <= R:
            m = L + (R - L) // 2
            if sol[m][1] <= timestamp:
                res = sol[m][0]
                L = m + 1
            else:
                R = m - 1

        return res