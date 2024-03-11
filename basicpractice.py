l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9]
x = []
a = int(''.join(str(i) for i in reversed(l1)))
b = int(''.join(str(i) for i in reversed(l2)))

for i in str(a + b):
    x.append(i)
x.reverse()
print(x)
#leetcode add two numbers.
#leetcode has not default list,just has ListNode,so cant run this code in the web.


