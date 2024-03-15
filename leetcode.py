
nums = [5, 3, 3]
def f(l):
    for i in range(len(l)):
        while i + 1 < len(l) and l[i] <= l[i + 1]:
            m = l[i] + l[i + 1]
            l[i + 1] = m
            l.pop(i)
            print(l)
            i += 1
        else:
            pass
while len(nums) >= 2:
    f(nums)
print(max(nums))
##leetcode No.2789 timeout##
