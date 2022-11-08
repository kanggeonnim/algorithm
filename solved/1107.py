channel = int(input())
errNum = int(input())
if errNum != 0:
    errList = list(map(int, input().split(' ')))
else:
    errList = []
upNum = -2000000  # find number 0 to channel
downNum = 2000000  # find number 1000000 to channel
cNum = None # candidate number

# channel보다 작은 쪽에서부터 찾아감.
for i in range(0, channel + 1):
    str_i = list(map(int, str(i)))
    if all(j not in errList for j in str_i):
        upNum = i

# # channel보다 큰 쪽에서부터 찾아감. 
for i in range(1000000, channel - 1, -1):
    str_i = list(map(int, str(i)))
    if all(j not in errList for j in str_i):
        downNum = i

# choose candidate number
if (channel - upNum) <= (downNum - channel):
    cNum = upNum
else:
    cNum = downNum

#print(list(str(cNum)))
# count using (number, plus, minus) button
numCount = len((list(str(cNum)))) + abs(cNum - channel) # cNum으로 이동하기 위해 눌러야하는 숫자 버튼 수 + plus, minus 버튼 수
#print(f' num count is {len((list(str(cNum))))} + {abs(cNum - channel)}')
# count using only (plus, minus) button
pmCount = abs(channel - 100)

print(min(numCount, pmCount))

# print(f'UpNum is {upNum}, DownNum is {downNum}')
# print(f'channel is {channel}')
# print(f'errNum is {errNum}')

# print(f'errList is')
# print(errList)