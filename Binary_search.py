#n = int(input())
nums = ['1', '2', '3']
#for i in range(n):
    #nums.append (input("enter num: "))
#print(nums)
#print(nums[2])
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 3
print(list_numbers.index(4))
def binary_search(L,x):
    left = 0
    right = len(L)-1
    while left <= right:
        mid = (left+right)//2
        if L[mid] == x:
            return L[mid]
        if L[mid] < x:
            left = mid +1
        else:
            right = mid -1
    return -1
#print(binary_search([1,2,3,4,5,6,7],9))

if __name__ == "__main__":
    L = [1,2,3,4,5,6,7,8,9,]
    for x in range(1,100):
        position = binary_search(L,x)
        if position == -1:
            if x in L:
                print(x, "is in L, but function return -1")
            else:
                print(x,"not in list")
        else:
            if position == x:
                print(x,"found in correct position")
            else:
                print("Binary search returned", position, "for",x, "which is incorrect")
    print("program Terminated")








