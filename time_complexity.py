# sum 1 to n and check time complexity
n = 100

result = n * (n+1)//2
print(result)

# time complexity of this program is o(1) because operation is constant for any input value
res = 0
for i in range(n+1):
    res = i + res
print(res)

# time complexity of this program is o(n), operation  is proportional to value of n

even = [False] * (n+1)
for i in range(0,n+1,2):
    even[i] = True
print(even[3])

# time complexity of this program is 0(n) operation depends on n value and space complexity also o(n)
#elements  increase with n value
count = 0
num = 3
for i in range(num):
    for j in range(num):
        count = count + 1

print("num = ",num, "count = ", count)
# time complexity of this program is o(n square),  relation with input and operation o(n square)
# space complexity is n
count = 0
num = 3
for i in range(num):
    for j in range(num):
        for k in range(num):
            count = count + 1

print("num = ",num, "count = ", count)
# time complexity of this program is o(n2)  relation with input and operationo(n3)