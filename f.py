n=(int(input("enter no of terms")))
name=(input("enter name"))
marks=[]
for i in range (n) :
    x=int(input (f"enter marks of sub "))
    marks.append(x)
print(name)
print(marks)
total=(marks[0]+marks[1]+marks[2]+marks[3]+marks[4])
print(f"{total}/500")
percentage=total/500*100
print(percentage)
if percentage>=90:
    print("GRADE:A")
elif percentage>=75 and percentage<=89:
    print("GRADE:B")
elif percentage>=60 and percentage<=74:
    print("GRADE:C")
elif percentage>=40 and percentage<=59:
    print("GRADE:D")
elif percentage <40:
    print("GRADE:F")
else:                       
    print("invalid input")