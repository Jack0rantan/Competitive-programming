import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.head = None
        self.qhead = None
        self.qrear = None
        
    def pushCharacter(self, data):
        nd = Node(data)
        if not self.head:
            self.head = nd
        else:
            nd.next = self.head
            self.head = nd

    def enqueueCharacter(self, data):
        nd = Node(data)
        if not self.qhead:
            self.qhead = self.qrear = nd
        else:
            self.qrear.next = nd
            self.qrear = nd

    def popCharacter(self):
        if not self.head:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def dequeueCharacter(self):
        if not self.qhead:
            return None
        else:
            popped = self.qhead.data
            self.qhead = self.qhead.next
            return popped

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


f = open('input.txt','r')
input = f.readline

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    