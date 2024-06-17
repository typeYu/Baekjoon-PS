nums = [False for _ in range(10001)]
indexNums = [i for i in range(10001)]
for i in indexNums:
    selfNum = i
    for j in str(i):
        selfNum += int(j)
    if 1 <= selfNum < 10001 and nums[selfNum] == False:
        nums[selfNum] = True

for i in range(1, len(nums)):
    if not nums[i]:
        print(i)