#Inbuilt sorting technique
#Let an array of integers

arr = [5,8,3,1,7]

arr = sort(arr)


#bubble sort

n=len(arr)
def bubbleSort(arr):
   for i in range(n):
        for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                        arr[j],arr[j+1] = arr[j+1],arr[j]

   return arr


#QuickSort

def Partition(arr,low,high):
    
    pivot = arr[high]
    i = low-1
    
    for j in range(low,high):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
            
    arr[i+1],arr[high] = arr[high],arr[i+1]
    
    return i+1


def QuickSort(arr,low,high):
    
    if low < high:
        pi = Partition(arr, low, high)
        QuickSort(arr, low, pi-1)
        QuickSort(arr, pi+1, high)
        

    return arr
    



                        

