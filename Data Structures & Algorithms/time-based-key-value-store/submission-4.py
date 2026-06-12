class TimeMap:

    def __init__(self):
        self.status={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.status.keys():
            self.status[key].append((value,timestamp))
        else:
            self.status[key]=[(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        ans=""
        if key in self.status.keys():
            
            for val in self.status[key]:
                if val[1]<=timestamp:
                    ans=val[0]
                else:
                    break
            
        return ans
