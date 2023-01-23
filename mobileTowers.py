"""
The telecommunications company has installed N mobile towers in a city to improve signal coverage.
The company wants to know which areas are currently covered by the mobile towers so that they can install additional towers in areas that are not yet covered.
There is a lot of data that need to be examined.The data might show some areas overlap with other areas because some mobile towers cover common areas.

The company wants you to provide them with a summarized list of areas that are currently covered by the mobile towers by combining the common areas.

For example, if the data is [[1, 3], [3, 5], [10, 15]], we can combine [1, 3], [3, 5] and provide a summarized list as [[1, 5], [10, 15]].

Write a program that reads the number of mobile towers N, start points and end points of the mobile towers, and prints the summarized list 
of areas under coverage by combining the common areas. 

"""


def summarizedList(Lst):
    for i in Lst:
        for j in Lst:
            if i!=j:
                if i[0]>j[0]:
                    pass
                elif i[0]<=j[0] and j[0]<=i[1]:
                    if j[1]>=i[1]:
                        i[1]=j[1]
                        Lst.remove(j)
                    elif j[1]<i[1]:
                        Lst.remove(j)
    return Lst

N=int(input())
Lst=[]
for _ in range(N):
    Lst.append(list(map(int,input().split())))
print(summarizedList(Lst))

