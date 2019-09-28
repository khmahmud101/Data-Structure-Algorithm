def selection_sort(L):
   n = len(L)
   for i in range(0,n-1):
       index_min = i
       for j in range(i+1,n):
           if L[j] < L[index_min]:
            index_min = j
       if i != index_min:
            L[i],L[index_min] = L[index_min], L[i]
   for i in range(0,n):
        print (L[i])
if __name__ == "__main__":
    L=[5,2,7,6,9]
    print("Before Sorting:",L)
    selection_sort(L)





