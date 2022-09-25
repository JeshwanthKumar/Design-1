#Time Complexity: add() - O(1), remove() - O(1), contains() - O(1)
#Space Complexity: O(n) - We're storing 'n' numbers
#Approach: Double Hashing

class MyHashSet:

    def __init__(self):
        self.length = 1000      #Assigning the length to 1000
        self.primary = [None] * self.length #Setting the primary to None to its length
        
    def hashkey(self, key):
        return key % self.length   #First hash function: Modulus the key with the length to get the index in the primary array
    
    def doublehashkey(self, key):
        return key // self.length   #Seconf hash function: Floor divide the key with the length to get the index in the secondary array

    def add(self, key: int) -> None:
        hashIndex = self.hashkey(key)
        doubleHashIndex = self.doublehashkey(key)
        
        if self.primary[hashIndex] == None:
            if hashIndex == 0:
                self.primary[hashIndex] = [False] * (self.length + 1)   #If there is no key in the first index of the primary index, create secondary array with "False" to length+1
            else:
                self.primary[hashIndex] = [False] * self.length #Else create secondary array with "False" to length
                
        self.primary[hashIndex][doubleHashIndex] = True  #If the key enters the index change the corresponding index's key to "True", meaning the key is added

    def remove(self, key: int) -> None:
        hashIndex = self.hashkey(key)
        doubleHashIndex = self.doublehashkey(key)
        
        if self.primary[hashIndex] != None:
            self.primary[hashIndex][doubleHashIndex] = False #If the index of the key is found in the secondary array change the key to "False"
            
    def contains(self, key: int) -> bool:
        hashIndex = self.hashkey(key)
        doubleHashIndex = self.doublehashkey(key)
        
        if self.primary[hashIndex] != None:
            return self.primary[hashIndex][doubleHashIndex] #Return "True" if the key is found


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)