class TimeMap:

    def __init__(self):
        self.status={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.status.keys():
            self.status[key].append((timestamp,value))
        else:
            self.status[key]=[(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        ans=""

        if key in self.status.keys():

            values=self.status[key]

            l,r=0,len(values)-1

            while l<=r:
                mid=(l+r)//2

                if values[mid][0]==timestamp:
                    return values[mid][1]
                
                elif values[mid][0]>timestamp:
                    r=mid-1

                elif values[mid][0]<timestamp:
                    ans=values[mid][1]
                    l=mid+1

        return ans