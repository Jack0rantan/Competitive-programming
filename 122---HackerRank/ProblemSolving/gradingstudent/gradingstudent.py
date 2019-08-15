import sys

# input file
f = open('testinput.txt', 'r')
sys.stdin = f

def gradingStudents(grades):
    # Write your code here
    ans = []
    for i in grades:
        if i >= 38:
            if str(i)[-1] == "8" or str(i)[-1] == "3":
                i += 2
            if str(i)[-1] == "9" or str(i)[-1] == "4":
                i += 1
        ans.append(i)
    return ans

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
