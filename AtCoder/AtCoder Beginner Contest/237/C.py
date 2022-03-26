S=input()
s=list(S)

def kaibun(l):
    for i in range(len(s)//2):
        if s[i]!=s[-i-1]:
            return False
            exit()
    return True

if kaibun(s):
    print("Yes")
else:
    for i in range(len(s)):
        if s[-i-1]!='a':
            break
    for j in range(len(s)):
        if s[j]!='a':
            break
    if i==0:
        print("No")
        exit()
    elif i>=j:
        del s[-i:]
        del s[:j]
    else:
        del s[-i:]
        del s[:i]
    if kaibun(s):
        print("Yes")
    else:
        print("No")