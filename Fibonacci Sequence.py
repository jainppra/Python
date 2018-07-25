#Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

sum = [1, 1]
n = int(input("Enter the number"))
for i in range(n-1):
    sum.append(sum[i]+sum[i+1])
    print(sum)
