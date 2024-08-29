class MinStack:
    #To do this we create a new min_stack [] that adds the min of (curr val vs last smallest in min_stack)
    #this lets us remove els from stack keeping smallest in min_stack
    #the rest is just basic methods
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #append val if its smaller than current in minStack 
        #IF nothing in minstack just add it
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

