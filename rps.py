import random
d={1:'r',2:'p',3:'s'}
c=d[random.randint(1,3)]
while(1):
	p=input("enter 'r','p','s'")
	print("computer",c)
	if(c==p):
		print("tie")
	elif(c=='r'and p=='s'or c=='p'and p=='r'or c=='s'and p=='p'):
		print("computer wins")
	else:
		print("player wins")
		
OUTPUT
	enter 'r','p','s'r
computer p
computer wins
enter 'r','p','s's
computer p
player wins
enter 'r','p','s'r
computer p
computer wins
enter 'r','p','s'p
computer p
tie
	
    	
