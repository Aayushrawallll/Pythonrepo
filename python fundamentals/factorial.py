fact=1
n=7
if n<0:
    print("Invalid No.")
elif n==0:
    print("Fact of 0 is 1")
else:
    for i in range(fact, n+1):
        fact=fact*i
    print("The fact of ", n, "is", fact)            