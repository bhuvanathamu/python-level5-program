print("Diamond Pattern")
print("-----------------")
n = int(input("Enter the number: "))


for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))


for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "* " * (i + 1))
