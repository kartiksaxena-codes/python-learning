# WRITE A PROGRAM THAT TAKES NO. FROM USER AND DISPLAY WETHER NO. IS PRIME OR NOT........abs
#                       FLAG CONCEPT


n=int(input("enter no."))
flag= 'green'
c=2
while c<n:
    if n%c==0:
        flag='red'
        c=n
    c=c+n
if flag=="green":
    print("prime")
else:
    print("Not prime")


    