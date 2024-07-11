#imported all the variables required for this program
import pickle
import math
import datetime
a1=0
a2=0
a3=0
a4=0
a5=0
print("^"*65)
print("\t\tWELCOME TO LATTE LOVE")
print("~"*65)
name=input("enter your name:")
phno=int(input("enter your phone number:"))
print("_"*60)
# imported each and every option which the customer needs
def espresso():
    price=0
    answer='y'
    while answer.lower()=='y':
        print("\t ENJOY HOT OR COLD")
        print("-"*20)
        print("1.flat white                             -rs 310")
        print("2.caramal macito                         - rs.300")
        print("3.caffe mocha                            - rs.300")
        print("4.cappucino                              - rs.200")
        print("5.chocolate cappucino                    - rs.310")
        print("6.americano                              - rs.200")
        print("7.brewed coffee                          - rs.300")
        print("8. quit")
        print()
        enter=int(input("enter your choice (1-8):"))
        if enter in [1,5]:
            no=int(input("no of espresso:"))
            price=price+(310*no)
        elif enter in [2,3,7]:
            no=int(input("no of espresso:"))
            price=price+(300*no)
        elif enter in [4,6]:
            no=int(input("no of espresso:"))
            price=price+(200*no)
        else:
            break
        print()
        answer=input("any other in espresso(y/n):")
        print()
    return price

    

def frappuccino():
    price=0
    answer='y'
    while answer.lower()=='y':
        print("\tBLENDED BEVERAGES")
        print("-"*20)
        print("1.mocha/white mocha          -rs 285")
        print("2.java chip                  - rs.325")
        print("3.caramel/espresso           - rs.320")
        print("4.caramel java chip          - rs.320")
        print("5.vannila cream              - rs.285")
        print("6.stawberries&creme          - rs.285")
        print("7.green tea creme            - rs.325")
        print("8. quit")
        print()
        enter=int(input("enter your choice (1-8):"))
        if enter in [1,5,6]:
            no=int(input("no of frappuccinos:"))
            price=price+(285*no)
        elif enter in [2,7]:
            no=int(input("no of frappuccinos:"))
            price=price+(325*no)
        elif enter in [3,4]:
            no=int(input("no of frappuccinos:"))
            price=price+(285*no)
        else:
            break
        print()
        answer=input("any other in frappuccinos(y/n):")
        print()
    return price

def teavana():
    price=0
    answer='y'
    while answer.lower()=='y':
        print("\tTEA REIMAGINED")
        print("-"*20)
        print("1.black tea        - rs.225")
        print("2.green tea        - rs.240")
        print("3.tea latte        - rs.240")
        print("4.mint blend       - rs.225")
        print("5.matcha           - rs.225")
        print("6. quit")
        print()
        enter=int(input("enter your choice (1-6):"))
        if enter in [1,4,5]:
            no=int(input("no of teavana:"))
            price=price+(225*no)
        elif enter in [2,3]:
            no=int(input("no of teavana:"))
            price=price+(240*no)
        else:
            break
        print()
        answer=input("any other in teavana(y/n):")
        print()
    return price

def latte():
    price=0
    answer='y'
    while answer.lower()=='y':
        print("\tBEST EVER LATTE")
        print("-"*20)
        print("1.pistachio latte              -rs.380")
        print("2.honey oatmilk latte          - rs.380")
        print("3.caffe latte                  - rs.380")
        print("4.cinnamon dolce latte         - rs.360")
        print("5.special latte                - rs.360")
        print("6.blonde vannila latte         - rs.360")
        print("7. quit")
        print()
        enter=int(input("enter your choice (1-7):"))
        if enter in [1,2,3]:
            no=int(input("no of latte:"))
            price=price+(380*no)
        elif enter in [4,5,6]:
            no=int(input("enter how many latte you want"))
            price=price+(360*no)
        else:
            break
        print()
        answer=input("any other latte(y/n):")
        print()
    return price
def desserts():
    price=0
    answer='y'
    while answer.lower()=='y':
        print("1.dark chocolate frudge brownie     -rs.230")
        print("2.lime frosted cocounut bar         -rs.240")
        print("3.raspberry square                  -rs.240")
        print("4.toasted almond                    -rs.240")
        print("5.double chocolate brownie          -rs.230")
        print("6.chocolate chip cookie             -rs.270")
        enter=int(input("enter your order form(1-6)"))
        if enter in [1,5]:
            no=int(input("no of desserts:"))
            price=price+(230*no)
        elif enter in [2,3,4]:
            no=int(input("no of desserts:"))
            price=price+(240*no)
        elif enter==6:
            no=int(input("no of desserts"))
            price=price+(270*no)
        else:
            break
        answer=input("any other desserts(y/n):")
        print()
    return price


f=open("coffee.dat","wb")
ans='y'
rec=[]
while ans=='y':
    print("\tMENU")
    print("-"*20)
    print("1.espresso")
    print("2.frappuccino")
    print("3.teavana")
    print("4.latte")
    print("5.desserts")
    print("0. exit")
    print("-"*20)
    print()
    code=int(input("enter your order (0-5):"))
    print()
    if code==1:
        a1=a1+espresso()
        rec.append(["espresso",a1])
    elif code==2:
        a2=a2+frappuccino()
        rec.append(["frappucino",a2])
    elif code==3:
        a3=a3+teavana()
        rec.append(["teavana",a3])
    elif code==4:
        a4=a4+latte()
        rec.append(["latte",a4])
    elif code==5:
        a5=a5+desserts()
    else:
        break
    ans=input("continue? (y/n):")
    print()
pickle.dump(rec,f)
f.close()

print("_"*70)
print("\t\t    WELCOME")
print("-"*70)
print("\t\t     BILL")
print("-"*70)
now=datetime.datetime.now()
dtm=str(now)
print("date & time:     \t",dtm)
print("-"*70) 
print("name:            \t",name)
print("phone no:        \t",phno)
print("-"*70)
print("ITEMS\t\t\tPRICE")
print("-"*70)
a=a1+a2+a3+a4

f=open("coffee.dat","rb")
r=pickle.load(f)
for i in r:
    print(i[0],"\t\t",i[1])
f.close()
print("-"*70)    

if a>=500:
    disc=0.05*a
    am=a-disc 
    print("total price:     \t",a)
    print("discount 5%:     \t",disc)
    print("-"*70)
    print("total amount:    \t",am)
else:
    print("total amount:    \t",a)
print("_"*70)
print()
f.close()
print("*"*70)
print("\t\tTHANK YOU!! VISIT AGAIN!!!")
print("_"*70)
input()
