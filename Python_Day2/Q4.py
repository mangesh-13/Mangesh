'''
Given the triangle of consecutive odd  numbers


Above triangle is given Calculate Sum row wise
Example we call function :- row_sum_odd_numbers(2)
Result will be=3 + 5 = 8
if user give 4 then ur output is 13 + 15 + 17+ 19 = 64

'''

def EmptyList(n):
    List=[]
    for i in range(n):
        List.append([])
    return List

def row_sum_odd_numbers(n):
    List=EmptyList(n)
    a=1
    sum=0
    for i in range(n):
        for j in range(1,i+2):
            List[i].append(a)
            a+=2
    print(List)
    for i in List[i]:
        print(i,"+",end=" ")
        sum+=i
    print("=",sum)

n=int(input("Enter a row:"))
row_sum_odd_numbers(n)
