#  WAP THAT TAKES AGE OF A PERSON AND DISPLAY THE AGE CATOGARY AS PER THE GIVEN AGE CHART
1.    # 1 to 12 (child)
2.     #13 to 17 (teen ager)
3.     #18 to 35 (adult)
4.     #35 to 58 (middle aged)
5.     #58 or more then (old age)




age=int(input("enter your age"))
if age>=1 and age<=12 :
    print("child")
if age>=13 and age<=17 :
    print("teen ager")
if age>=18 and age<=35 :
    print("adult")
if age>=35 and age<=58 :
    print("middle aged")
if age>58 :
    print("old age")
if age<0 :
    print("invalid age")