while True:
	print("1. check prime number ")
	print("2. check palindrome number ")
	print("3. Reverse a digit ")
	print("4. Count Digits ")
	print("5. Exit " )
	choice  = int(input("Enter Your Choice: "))
	match choice:
		case 1:
			a = int(input("Enter Your Number: "))
			x= 0
			for i in range(1,a+1):
				if a%i==0:
					x= x+1
	
			else:
				if x ==2:
					print("Prime Number")
				else:
					print("non prime")
		case 2:
			b = int(input("Enter your Number: "))
			temp = b
			rev = 0
			for i in range (len(str(b))):
   				rev = rev*10 + b%10
   				b = b//10
			if rev == temp:
   				print("Palindrome: yes ")
			else:
   				print("not Palindrome")
			
		case 3:
			b = int(input("Enter your Number: "))
			rev = 0
			for i in range (len(str(b))):
   				rev = rev*10 + b%10
   				b = b//10
			print("REVERSE = ", rev)


		case 4:
			b = int(input("Enter your Number: "))
			l = len(str(b))
			print("Count Digits: ", l)
			
		case 6:
			if choice >=6:
				print("INVALID CHOICE, PLEASE TRY AGAIN ")
		case 5:
			break

		
	again = input("DO YOU WANT TO CONTINUE(YES / NO ): " ).lower()
	match again:
		case "yes":
			continue
		case "no":
			break
		case __:
			print("PLEASE CHOOSE APPROPRIATE OPTION")