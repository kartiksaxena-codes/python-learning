# WRITE A PROGRAM THAT TAKES MARKS FROM 5 STUDENTS AND THEN INCREMENT THE MARKS BY 10 IF THE SCORE IS LESS THAN 33AT THE END THE PROGRAM MUST DISPLAY THE S.NO AND GRADE OF STUDENT BASIS THE FOLLOWING TABLE.abs
# <33   C
# 33-60  B
# 61-90  A
#  >91  A+


marks=[]
i=0
while i<5:
    score= int(input("Enter marks of student"))
    if score <0 or score >100:
        print("Invalid score")
        continue
    marks.append(score)
    i=i+1
print(marks)