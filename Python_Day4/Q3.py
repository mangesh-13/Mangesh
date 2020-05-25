'''
3.Write a recursive function to calculate the sum of numbers from 0 to 10
Expected output: 55
'''

def rec_sum(n):                           # 10
     if n == 1:             
         return n
     return n + rec_sum(n-1)              # 10 + rec_sum(9)---------------------------------------------->10 + 45=55
                                         #        9 + rec_sum(8)----------------------------------------->9 + 36=45
                                         #              8+ rec_sum(7)------------------------------------>8 + 28=36
                                         #                   7 + rec_sum(6)------------------------------>7 + 21=28
                                         #                         6 +rec_sum(5)------------------------->6 + 15=21
                                         #                              5 + rec_sum(4)------------------->5 + 10=15
                                         #                                    4+ rec_sum(3)-------------->4 + 6=10
                                         #                                          3+ rec_sum(2) ------->3 + 3=6
                                         #                                              2+ rec_sum(1) ---> 2 + 1=3

n=int(input("Enter the number:"))  #10
print(rec_sum(n)) # func call