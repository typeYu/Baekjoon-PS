n=int(input())
arr=bin(n)
arr=arr[2:]
arr_reverse=arr[::-1]
num=int(arr_reverse,2)

print(num)