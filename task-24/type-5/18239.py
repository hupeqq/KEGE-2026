from re import finditer

with open(r'..\files\24_18239.txt') as file:
    data = file.readline()

pattern = rf'-?([1-9]+-)+[1-9]+'

matches = [match.group() for match in finditer(pattern, data)]

ans = 0
for match in matches:
    match = match.split('-')[1:]
    nums = list(map(lambda x: -int(x), match))
    l = summ = len_nums = 0
    for r in range(len(nums)):
        summ += nums[r]
        len_nums += len(str(nums[r]))
        while summ - 2 * nums[l] < -20_000:
            summ -= nums[l]
            len_nums -= len(str(nums[l]))
            l += 1
        ans = max(ans, len_nums)

print(ans)