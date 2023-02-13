pnumber = input("enter phone number:")
fp = open('data.txt')
for i in fp:
    if pnumber in i:
        print("phone number is found:", i)
    else:
        print("phone number is not found")

'''
output:-

enter phone number:1234567890
phone number is not found

====== RESTART: C:/9.file handling in python/search_pnumber_assignment.py ======
enter phone number:6698765445
phone number is found: 980765789808976698765445

'''