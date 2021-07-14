s = input()
p = list(input())
d = [0 for _ in range(26)]

for i in range(26):
    ind = ord(s[i])-ord('a')
    d[ind]=i

p.sort(key=lambda c:d[ord(c)-ord('a')])
print(''.join(p))
