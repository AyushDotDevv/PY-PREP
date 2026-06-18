n=5
name=(input("enter name"))
marks=[]
for i in range (n) :
    x=int(input (f"enter marks of sub "))
    marks.append(x)

def ctotal():
    total= sum(marks) 
    return total
t= ctotal()
def cpercentage():
    percentage=(t/500*100)
    return percentage
p= cpercentage()
def cgrade():
    if p>=90:
        grade=("A")
    elif p>=75 and p<=89:
        grade=("B")
    elif p>=60 and p<=74:
        grade=("C")
    elif p>=40 and p<=59:
        grade=("D")
    elif p<40:
        grade=("F")
    else:                       
        print("invalid input")
    return grade 
g= cgrade()
def printresult ():
    print(name)
    print(marks)
    print(t)
    print(p)
    print(g)        

printresult()