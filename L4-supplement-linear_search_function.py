def linear_search(arr,goal):
    for i in range(len(arr)):
        if arr[i]==goal:
            print(f' Element {arr[i]} found at {i}')
            break
    else:
        print("element not found")


size=int(input("Enter the size of array: "))
a=[None]*size
for i in range(size):
    b=int(input(f'Enter {i}th element: '))
    a[i]=b
print(a)    
target=int(input("Enter the target to be searched: "))        
linear_search(a,target)            
