#check whether string entered by user is palindrome or not.

org=input("Enter String :")
rev=org[::-1]
print("Orginal String :",org)
print("Reversed String :",rev)
if org==rev:
    print("palindrome String")
else:
    print("Not a salindrome String")
