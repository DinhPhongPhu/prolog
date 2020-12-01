s="abcjd(akkdd),lllll(llll)"

idx=s.find(")")

t=s[:idx+1]

s=s[idx+2:]

print(t)
print(s)