#snake and ladder game
import random
count=0
while(count<=100):
	n=input("enter r to roll the dice")
	if(n=='r'):
		a=random.randint(1,6)
		count=count+a
		print("my positin",count)
		print("your random value",a)
	if(count==8):
		count=37
		print("hurry ladder")
	elif(count==11):
		count=2
		print("oops! its a snake bite")
	elif(count==12):
		count=34
		print("hurry ladder")
	elif(count==25):
		count=4
		print("oops! its a snake bite")
	elif(count==38):
		count=9
		print("oops! its a snake bite")
	elif(count==40):
		count=68
		print("hurry ladder")
	elif(count==52):
		count=81
		print("hurry ladder")
	elif(count==65):
		count=46
		print("oops! its a snake bite")
	elif(count==76):
		count=97
		print("hurry ladder")
	elif(count==89):
		count=70
		print("oops! its a snake bite")	
	elif(count==93):
		count=64
		print("oops! its a snake bite")
	elif(count>100):
		count=count-a
		print("u cant go beyond 100")	
	elif(count==100):
		print("congo! u won the game")
		break	