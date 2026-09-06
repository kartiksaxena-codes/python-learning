# WRITE A PROGRAM THAT DISPLAY 5 ODD NO. STARTING FROM S (TO BE TAKEN FROM THE USER)
#  HAVES, ANY NO. DIVISIBLE BY 5 IN TO BE IGNORED



s=int(input("enter starting no."))
c=0
while c!=5:
    if s%2!=0:
        if s%5!=0:
            print(s)
            c=c+1
    s=s+1