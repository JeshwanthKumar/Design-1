#Time Complexity: push() - O(1), pop() - O(1), peek() - O(1), empty() - O(1)
#Space Complexity: O(n) - We're using another stack space to store the elements

class MyQueue:

    def __init__(self):
        self.inStack = []       #Initialization of inStack
        self.outStack = []      #Initialization of ooutStack

    def push(self, x: int) -> None:
        self.inStack.append(x)      #Appending 'x' into the inStack
        

    def pop(self) -> int:
        temp = self.peek() #Calling the peek function and storing the last element in temp variable
        self.outStack = self.outStack[:-1]      #Removing the last element in the outStack
        return temp     #Returning the temp

    def peek(self) -> int:
        if len(self.outStack) == 0:     #Checking if the outStack is empty
            while self.inStack:     #While it's empty, pop and push all the elements from the inStack into outStack
                elem = self.inStack.pop()       #Pop elements from inStack 
                self.outStack.append(elem)      #Append elements into outStack
        return self.outStack[-1]                #Return the last element on outStack

    def empty(self) -> bool:
        return len(self.inStack) + len(self.outStack) == 0      #Return true if the addition of length of inStack and outStack is equal to 0, Else return - 1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
