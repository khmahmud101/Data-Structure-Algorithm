def bubble_sort(L):
    n = len(L)
    count = 0
    for i in range(0,n):

        for j in range(0,n-i-1):

            if L[j] > L[j+1]:
                L[j] , L[j + 1] = L[j+1] , L[j]
            count +=1
            print("print List in step ",count, " = " ,L)
if __name__ == "__main__":
    L = [6,1,4,9,2]
    print("Before sort",L)
    bubble_sort(L)
    print("After complete sort sort",L)

