def linear_search(L,x):
    i = 0
    n = len(L)
    while i < n:
        if L[i] == x:
            return i
        i += 1
    return -1

result = linear_search([1,2,3,4,5],3)
if result == -1:
    print("Element Not found")
print("Element found at index", result)

# def linear_search(L,x):
#     n = len(L)
#     for i in range(n):
#         if L[i] == x:
#             return i
#
#     i = -1
#     return i
#
# print(linear_search([1,2,3,4,5],3))
