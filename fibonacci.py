#fibonacci sequence using recursuion
#Name:Kushal R
#USN:1RUA25BCA0053
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


num = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(num):
    print(fib(i), end=" ")
