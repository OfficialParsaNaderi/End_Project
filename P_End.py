# Hello , this code have  510  line and use :
# library : os , math , random : choice.randint ,time : sleep . break ,turtle : penup.size.down.color.pencolor.bgcolor.shape.size.circle.Screen.bye.done 
# def,whileTrue,try,except,ValueError, TypeError,float,int,str,sin,factorial,+,-,*,/,**,//,split,input,replace,lower,upper,title,print,f,==,!=,open("file"),or,if,elif,else 
from os import system
system("cls")

from time import sleep

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The Story section (1) :

print(" <------------------------------------------------------------------------------------------------------------>")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#The first minigame (1) :

sleep(2)

print(" Parsa Naderi present ! Welcome to the Game ! \n I hope ful you like my Game so Let's play !.👍🤗")


def Story_maker() :
    try :
        user1,user2,user3,user4,user5 = (input("Choose a noun : \n >>")),(input("Choose a Pornoun : \n <<")),(input("Name a Place : \n >>")),(input("Choose a Adj : \n <<")),(input("Choose a noun : \n >>"))
        print("start short story : \n <------------->")
        print(f"Be kind to your {user1} - footed {user2} \n For a duck may be somebody {user3} , \n be kind to your {user2} in {user3} \n Where the weather is always {user4} \n ")
        print(f"You may think that is this the {user5} \n Well it is .")
        print(" <-------------> \n finished short story . ")
        print(" This was an educational joke . Well , I think it was educational because I searched on the internet .\n"
        " Let's go to the continuation of the program . My name is Parsa Naderi and I hope you like my program.❤️🎈👍")
    except ValueError :
        print(" you Have Entered a Wrong Value ! ")
    except TypeError :
        print(" you Write a Wrong Type ! ")
Story_maker()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The Story section (2) :

print("\n <-------------------------------------------------------------------------------------------------------->")
print(" \n   Well you Must play I hope you like this !")
print("    ( Well , if you want to enter the introduction of the game , dear user , well , let's start together , we have a story axis \n      that you have to enter our program and buy our services with the bank account we give you and give us the service ! )😎😝")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The Story section (3) :

print("\n <------------------------------------------------------------------------------------------------------------>")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#The second minigame (2) :

sleep(2)

print(" Welcome to the mini Game 2 !👍🤗")


def Purchase_service () :
    try :
        number1 = (100)
        while (number1 < 200):
            user6=float(input(" you Choose a Number in range 10 or 20 ! ( Please deposit $100 to my account to allow you to enter the game !)🤯❤️\n >>").replace("$",""))
            if user6 == 10 or user6 == 20 :
                number1 = number1-int(user6)
                print(f"result : ${number1}")
            else :
                print(" dear don't end !") 
            if number1 == 0 :
                print(" End Thanks ! Well go next Game ! ❤️🎈")
                break
            if user6 != 0 :
                print(" dear don't end continue !:) 😉👍")
    except ValueError :
        print(" you Have Entered a Wrong Value ! 😣❤️")

Purchase_service()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The Story section (3) :

print("<------------------------------------------------------------------------------------------------------------>")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#The third minigame (3) :

sleep(2)

print(" Welcome to the mini Game 3 !🤗👍")


import math
def math1() :
    try :
        while True :
            user7 = (input(" Do you wnat choose a favorite number and math operators !? 😅❤️\n >>").replace("$",""))
            first_number , math_operators , last_number = user7.split()
            if  math_operators  == ("+") :
                print(f" result : {int(first_number) + int(last_number)}$")
            elif math_operators == ("-") :
                print(f" result : {int(first_number) - int(last_number)}$")
            elif math_operators == ("*") :
                print(f" result : {int(first_number) * int(last_number)}$")
            elif math_operators == ("/") :
                print(f" result : {int(first_number) / int(last_number)}$")
            elif math_operators == ("**") :
                print(f" result : {int(first_number) ** int(last_number)}$")
            elif math_operators == ("//") :
                print(f" result : {int(first_number) // int(last_number)}$")
            elif math_operators == ("factorial") :
                print(f" result : {math.factorial(int(first_number)) , math.factorial(int(last_number))}")
            elif math_operators == ("sin") :
                print(f" result : {math.sin(int(first_number)) , math.sin(int(last_number))}")
            user8 = (input(" Do you want continue the Game (yes/y) , (no/n)! 🤯😎❤️\n <<"))
            if user8 == "y" :
                continue
            else :
                break
    except ValueError :
        print(" you have a Entered a Wrong Value ! 😉👍😣")

math1()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The Story section (4) :

print("\n <------------------------------------------------------------------------------------------------------------>")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#the minigame (4) :

sleep(2)

print(" Welcome to the mini Game 4 !👍🤗")

def weather() :
    try :
        for school in range(5):
            print(school)
        user13 =float(input(" start ! \n enter your number school class  ? :👍😉\n >>"))
        print(" value1 is :", user13)
        user14 =int(input(" enter your number english class ?:👍😉\n <<"))
        print(" value2 is :", user14)
        user15 =input(" who's the weather  ? :🤯😝\n <>")
        print(" value3 is :", user15)
        if user15 == ('hot'):
            print(" weather is hot!")
        elif user15 == ('cold'):
            print(" weather is cold!")
        if user13<user14:
            result1= user13*user14+2
            print(" result1 :", result1)
            print(" youre number class school and english good ! 👍😉💵")
        if user13>user14:
            result2=user13/user14-2
            print(" result2 :", result2)
            print(" youre number class school and english bad ! 😣👍")
    except ValueError :
        print(" you Have Entered a Wrong Value ! 😣👍😉")

weather()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#The story section (5) :

print("\n <------------------------------------------------------------------------------------------------------------>")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#the minigame (5) :

sleep(2)

print(" Welcome to the mini Game 5 !👍🤗")

def emoji() :
    try :
        print(" This is a last mini game let's play !")
        user16,user17,user18,user19,user20=(input(" choose a name1 ! 😉😎\n >>")),(input("choose a name2 ! 😎😉\n <<")).title(),(input("choose a emoji ! 😉😎\n >")),(input("choose a emoji ! 😎😉\n <")),(input(" choose a emoji ! 😉😎\n >"))
        print(user16.replace(" ","...")) if" "in user16 else print(f"{user16}")
        print(user17.lower())
        print(user18.replace(":)","😁")) if":)"in user18 else print(f"{user18}")
        print(user19.replace(":(","😕")) if":("in user19 else print(f"{user19}")
        print(user20.replace(":|","😐")) if":|"in user20 else print(f"{user20}")
    except ValueError :
        print(" you Have Entered a Wrong Value ! 😣👍😉")

emoji()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#The story section (6) :

print("\n <------------------------------------------------------------------------------------------------------------>")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#the main game (1) !:

sleep(2)

print(" Are you ready play a main game !!🤗👍🥳❤️")


from turtle import fd,lt,penup,pendown,Turtle,circle,shape,shapesize,pensize,pencolor,color,bgcolor,Screen,bye,setx,sety,done


user23 = input("do you want to register or login ? \n >>").lower()

if user23 == "register" :
    username = input(" Username :")
    userpassword = input(" Password :")
    user_info = open("file1.txt","r")
    info_list = user_info.readlines()
    counter = 0
    for line in info_list :
        if userpassword in line or username in line :
            counter += 1
    if counter == 2 :
        print("you have already registered in our databases ! Let's play !❤️👍😎🤯")
        penup()
        lt(-180)
        fd(700)
        pendown()
        circle(radius=60)
        penup()
        lt(-120)
        fd(100)
        pendown()
        circle(radius=60)
        penup()
        lt(-90)
        fd(200)
        pendown()
        circle(radius=70)
        penup()
        lt(30)
        fd(200)
        pendown()
        for x in range (4) :
            fd(100)
            lt(90)
        penup()
        fd(300)
        pendown()
        circle(radius=70)
        penup()
        fd(100)
        pendown()
        for y in range (4) :
            fd(100)
            lt(90)
        penup()
        fd(200)
        pendown()
        circle(radius=70)
        penup()
        fd(100)
        pendown()
        fd(180)
        lt(120)
        fd(190)
        lt(122)
        fd(190)
        penup()
        lt(-240)
        fd(-1100)
        pendown()


        import random
        act1 = 1
        act2 = 6
        roll_again = "yes"
        while roll_again == "yes" or roll_again == "y" :
            print("Dices rolling... ")
            print("The values are : ")
            user21 = int(input(" Do you Want Choose a fav number in range (1:6) ! \n >>"))
            user22 = random.randint(act1,act2)
            print(f"{user21},{user22}", end=" : ")
            if user21 == 1 :
                shape("turtle")
                color("#fc3b38")
                pencolor("#38fcf6")
                pensize(1)
                bgcolor("#71ebb6")
                shapesize(1)
                lt(90)
                fd(200)
                lt(-110)
            if user21 == 2 :
                shape("turtle")
                color("#eb7571")
                pencolor("#ebf")
                pensize(1)
                bgcolor("#71ebb6")
                shapesize(1)
                fd(250)
                lt(20)
            if user21 == 3 :
                shape("turtle")
                color("#e9f5ea")
                pencolor("#f28")
                pensize(1)
                bgcolor("#f25")
                shapesize(1)
                fd(300)
            if user21 == 4 :
                shape("turtle")
                color("#f28")
                pencolor("#ebf")
                pensize(1)
                bgcolor("#38fcf6")
                shapesize(1)
                fd(400)
            if user21 == 5 :
                shape("turtle")
                color("#71ebb6")
                pencolor("#38fcf6")
                pensize(1)
                bgcolor("#fc3b38")
                shapesize(1)
                fd(500)
            if user21 == 6 :
                shape("turtle")
                color("#f25")
                pencolor("#ebf")
                pensize(1)
                bgcolor("#f28")
                shapesize(1)
                fd(600)
            user23 = str(input(" Do you Want continue Game (yes/y) , (no/n)!? 🤯😎👍💵"))
            if user23 == "yes" or user23 == "y" :
                    print(" Thanks ! has a not problem ! try again !! 🤯😎👍❤️")
                    continue
            if user23 == "no" or user23 == "n" :
                    print(" Yes ! Thanks ! I know you can thanks but this is a end of game good bye !. 👍🤯❤️ \n love you thanks because play my game !.❤️🎈😎")
                    Screen().bye()
                    break
    else :
        Screen().bye()
        user_info = open("file1.txt","a")
        user_info.write(f"Username : {username}\npassword : {userpassword}")
        user_info.close()
        print("you info have been added to our databases ! oh try again !😣🤯😅❤️")


elif user23 == "login" :
    username = input(" Username :")
    userpassword = input(" Password :")
    user_info = open("file1.txt","r")
    info_list = user_info.readline()
    for line in user_info:
        if username in line or userpassword in line :
            print(f" Welcome.master {username} !🥳❤️👍😎")
            penup()
            lt(-180)
            fd(700)
            pendown()
            circle(radius=60)
            penup()
            lt(-120)
            fd(100)
            pendown()
            circle(radius=60)
            penup()
            lt(-90)
            fd(200)
            pendown()
            circle(radius=70)
            penup()
            lt(30)
            fd(200)
            pendown()
            for x in range (4) :
                fd(100)
                lt(90)
            penup()
            fd(300)
            pendown()
            circle(radius=70)
            penup()
            fd(100)
            pendown()
            for y in range (4) :
                fd(100)
                lt(90)
            penup()
            fd(200)
            pendown()
            circle(radius=70)
            penup()
            fd(100)
            pendown()
            fd(180)
            lt(120)
            fd(190)
            lt(122)
            fd(190)
            penup()
            lt(-240)
            fd(-1100)
            pendown()
            import random
            act1 = 1
            act2 = 6
            roll_again = "yes"
            while roll_again == "yes" or roll_again == "y" :
                print("Dices rolling... ")
                print("The values are : ")
                user21 = int(input(" Do you Want Choose a fav number in range (1:6) if you lose write (no/n) if you win (yes/y) ! \n >>"))
                user22= random.randint(act1,act2)
                print(f"{user21},{user22}", end=" : ")
                if user21== 1 :
                    shape("turtle")
                    color("#fc3b38")
                    pencolor("#38fcf6")
                    pensize(1)
                    bgcolor("#71ebb6")
                    shapesize(1)
                    lt(90)
                    fd(200)
                    lt(-110)
                if user21== 2 :
                    shape("turtle")
                    color("#eb7571")
                    pencolor("#ebf")
                    pensize(1)
                    bgcolor("#71ebb6")
                    shapesize(1)
                    fd(250)
                    lt(20)
                if user21== 3 :
                    shape("turtle")
                    color("#e9f5ea")
                    pencolor("#f28")
                    pensize(1)
                    bgcolor("#f25")
                    shapesize(1)
                    fd(300)
                if user21== 4 :
                    shape("turtle")
                    color("#f28")
                    pencolor("#ebf")
                    pensize(1)
                    bgcolor("#38fcf6")
                    shapesize(1)
                    fd(400)
                if user21== 5 :
                    shape("turtle")
                    color("#71ebb6")
                    pencolor("#38fcf6")
                    pensize(1)
                    bgcolor("#fc3b38")
                    shapesize(1)
                    fd(500)
                if user21== 6 :
                    shape("turtle")
                    color("#f25")
                    pencolor("#ebf")
                    pensize(1)
                    bgcolor("#f28")
                    shapesize(1)
                    fd(600)
                user23 = str(input(" Do you Want continue Game (yes/y) , (no/n)!? 🤯😎👍💵"))
                if user23 == "yes" or user23 == "y" :
                    print(" Thanks ! has a not problem ! try again !! 🤯😎👍❤️")
                    continue
                if user23 == "no" or user23 == "n" :
                    print(" Yes ! Thanks ! I know you can thanks but this is a end of game good bye !. 👍🤯❤️ \n love you thanks beacause play my game !.❤️🎈😎")
                    print("\n <------------------------------------------------------------------------------------------------------------>")
                    print("Project programmer: Parsa Naderi")
                    print("Project designer: Parsa Naderi")
                    print("Student semester: Semester 2")
                    print("Project Name: Game World")
                    print("Thanks to Parsa Naderi")
                    print("And all the friends who helped us in making this project.❤️🤯🎈💒💵😎👍")
                    print("\n <------------------------------------------------------------------------------------------------------------>")
                    Screen().bye()
                    break
        else :
            print(" you don't have account !😣❤️👍")
done()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------