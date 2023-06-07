a=int(input("enter1"))
b=int(input("enter2"))
c=a+b
print(c)

a=int(input("enter1"))
b=int(input("enter2"))
c=(a+b)/2
print(c)

a=int(input("enter1"))
b=int(input("enter2"))
W=a*b
print(W)

height=int(input("enter1"))
base=int(input("enter2")) 
area=(1/2)*(base*height)
print(area)

p=int(input("enter1"))
r=int(input("enter2"))
t=int(input("enter3"))
simple_interest=(p*r*t)//100
print(simple_interest)

x=int(input("enter"))
y=int(input("enter"))
x=x+y
y=x-y
x=x-y
print(x,y)

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

n=int(input("enter"))
if n>0:
    print("positive")
elif n==0:
    print("Zero")
else:
    print("negative")

n=int(input("enter"))
if n%5==0:
    print("hii")
    if n%11==0:
        print("bye")
    else:
        print("hii bye")

n=int(input("enter"))
if n%2==0:
    print("even number")
else:
    print("odd number")

year=int(input("Enter"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year")
else:
    print("The year isn't a leap year")

n=int(input("enter"))
if n<8:
    if n==0:
      print("sunday")
    elif n==1:
        print("Monday")
    elif n==2:
        print("Tuesday")
    elif n==3:
        print("Wednesday")
    elif n==4:
        print("Thursday")
    elif n==5:
        print("Friday")
    elif n==6:
        print("saturday")
    else:
        print("invalid")

month=int(input("enter"))
if month==31:
        print("January,March,May,July,August,October,December")
        if  month==30:
            print("April,June,September,November")  
else:
    print("invalid")  

math=int(input("enter"))
bio=int(input("enter"))
che=int(input("enter"))
phy=int(input("enter"))
com=int(input("enter"))
eng=int(input("enter"))
if math>=90:
    print("grade A")
elif bio>=80:
    print("grade B")
elif che>=70:
    print("grade c")
elif phy>=60:
    print("grade D")
elif com>=40:
    print("grade E")
elif eng<40:
    print("grade F")

Delhi=input()
Agra=input()
Jaipur=input()
if Delhi=="Red Fort":
    print("Delhi")
if Agra=="Taj Mahal":
    print("Agra")
if Jaipur=="Jal Mahal":
    print("Jaipur")
else:
    print("invalid")

num=int(input())
if num%5==0:
  print("Hello")
else:
  print("Bye") 

n=int(input())
if n%3==0:
    print("Divisible by 3")
else:
    print("not Divisible by 3")


n=int(input("enter"))
if n%5==0:
    print("Hello")
else:
    print("Bye")

n=int(input("enter"))
if n%10==0:
    print("last digit")
else:
    print("not last digit")

l=[h for h in range(1,101)if h%2==0]
print(l)

n=int(input("enter"))
if n>99 and n<1000:
    print("Three digit")
else:
    print("invalid")

n=int(input("enter"))
if n==100:
    print("boiling point")
else:
    print("not boiling point")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)

n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))
n3 = int(input("Enter third number "))
 
if n1 > n2 and n1 > n3:
  if n2>n3:
    print("The second largest number is",n2)
  else:
    print("The largest number is",n3)
elif n2 > n1 and n2 >n3:
  if n1 > n3:
    print("The second largest number is", n1)
  else:
    print("The second largest number is", n3)
else:
  if n1 > n2:
    print("The second largest number is",n1)
  else:
    print("The second largest number is", n2)

n=int(input("enter"))
if n=="1":
    print("number is 1")
elif n=="2":
    print("number is 2")
elif n=="3":
    print("number is 3")
elif n=="4":
    print("number is 4")
elif n=="5":
    print("number is 5")
elif n=="6":
    print("number is 6")
elif n=="7":
    print("number is 7")
elif n=="8":
    print("number is 8")
elif n=="9":
    print("number is 9")
else:
    print("number is not between 1 to 9")

a=int(input())
b=int(input())
sum=a+b
print(sum)

year=int(input())
if year%400==0:
    leapyear=True
elif year%100==0:
    leapyear=False
elif year%4==0:
    leapyear=True
    month = input("Input a month [1-12]")
if month in (1, 3, 5, 7, 8, 10, 12):
    monthlength=31
elif month==2:
    if leapyear:
        monthlength=29
    else:
        monthlength=28
else:
    monthlength=30
    day = int(input("Input a day [1-31]"))
    if day<monthlength:
         day+=1
    else:
        day==1
        if month==12:
            month==1
            year==1
        else:
            month+=1
            print("next yyyy-date-month.",year,day,month)


a=input("fisrt name")
b=input("last name")
print(b+a)

age=int(input())
sex=input()
if sex>=18 :
    print("Female")
else:
    if sex<30:
        print("male")

















