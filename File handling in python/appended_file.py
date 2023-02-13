'''
When there is need to presserve old data or new data must be
added at the end of the old data use append mode.

'''

fp=open('data.txt','a') #here 'a' is appending at the end of the file or adding at the end of the file
#d="This is first line in this file" #here we're giving data to print
#fp.write(d)

mn=input("enter mobile number:") #taking input from user in files
data=mn+"\n" #\n that stand for new line character=>9870765642\n
fp.write(data)
fp.close()