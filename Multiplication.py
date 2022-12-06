# Multiplication-Table
#I created a multiplication table application where user will enter a sentinel value n and the application will display the mathematical multiplication tables till given sentinel value n. For example, if user enters n = 4 then application will display the multiplication tables of 2, 3, and 4.
class Tables:
    def __init__(self,a):
        self.a=a
    def printtables(self):
        for i in range(2,self.a+1):
            print("Multiplication Table of",i,"is.")
            for j in range(1,11):
                print(i,"x",j,"=",j*i)
num=int(input("Enter a Number: "))
obj=Tables(num)
obj.printtables()
print("Thank you for your precious time :)")
