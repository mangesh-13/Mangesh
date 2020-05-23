'''
def EmptyList(n):
    List = []
    for l in range(n):
        List.append([])
    return List

def row_sum_odd_numbers(n):
    List =EmptyList(n)
    a=1
    for i in range(n):
        for j in range(1,i+2):
            List[i].append(a)
            a+=2
    return List
n=int(input("Enter row:"))
L=row_sum_odd_numbers(n)

sum=0
for i in L[n-1]:
    print(f"{i}+",end="")
    sum+=i
print("=",sum)

'''

# Or

def row_sum_odd_numbers(row_no):
    return row_no**3



row_no=int(input("Enter the row:"))
result=(row_sum_odd_numbers(row_no))
print(result)




