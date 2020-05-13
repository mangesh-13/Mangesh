#fibonacci series using generator
#Advantages of generator is memory utilization and performance improvement

def fib():
    a,b=0,1
    while True:
        
        yield a
        a,b=b,a+b
for n in fib():
    if n>1000:
        break
    print(n)

