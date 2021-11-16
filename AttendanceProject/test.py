# str1=input("Enter 1st string: ")
# def palindrome(str1):
#     l=len(str1)
#     pal_str=""
#     for i in range(1,l+1):
#         str1[i-1]=pal_str[-i]
#     for j in range(0,l):
#         if str1==pal_str:
#             print("Yes the string is a palindrome", str1)

# palindrome(str1)

# l1=len(str1)
# str2=input("Enter 2st string: ")
# l2=len(str2)
# c=0
# if l1==l2:
#     for i in range(0,l1):
#         if str1[i] in str2:
#             c=1

# else:
#     print("strings are not anagrams")

x=input("Enter a string: ")
'''
nitin==nitin
new=[]
l=['n','i','t','i','n']
new.append(l.pop())


'''
def palindrome(x):
    new=[]
    c=0
    l=[]
    for i in x:
        l.append(i)
    print(l)
    for i in range(0,len(l)):
        new.append(l.pop())
    print(new)
    for i in range(0,len(l)):
        if l[i]==new[i]:
            c+=1
    if c==len(l):
        print(x," is a palindrome string")
palindrome(x)