"""
a=int(input("Enter a number:"))   # Palindrome
temp=a
rev=0
while (a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
    """
a=input()
if a==a[::-1]:
    print("palindrome")
else:
    print("not palindrome")