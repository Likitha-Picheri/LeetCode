class MyCalendar:

    def __init__(self):
        self.check=[]
        

    def book(self, start: int, end: int) -> bool:
        if len(self.check)==0:
            self.check.append([start,end-1])
            return True
        else:
            for i in range(len(self.check)):

                if self.check[i][0]<=start<=self.check[i][1] or self.check[i][0]<=end-1<=self.check[i][1]:
                    return False 
                elif start<=self.check[i][0]<=end-1 or start<=self.check[i][1]<=end-1:
                    return False
            self.check.append([start,end-1])
            return True
    
        

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)