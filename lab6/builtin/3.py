string = input()
s2 = ''.join(reversed(string))


if s2 == string:
    print("Yes")
else:
    print("No")





def Palindrome(s):
    s1 = ''.join(reversed(s))

    if s1 == s:
        return True
    
    else:
        return False
    
s = input()

if(Palindrome(s)):
    print("YES")
else:
    print("NO")