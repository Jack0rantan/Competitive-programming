class Difference:
    maximumDifference = 0

    def __init__(self, a):
        self.__elements = a
        
	# Add your code here
    def computeDifference(self):
        sub = []
        for i in range(len(a)):
            for j in range(len(a))[i+1:]:
                sub.append(abs(a[i]-a[j]))
        self.maximumDifference = max(sub)

# End of Difference class

f = open('input.txt','r')
input = f.readline

_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()

print(d.maximumDifference)