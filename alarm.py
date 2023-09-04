import winsound, time, os, platform
from datetime import datetime


def sound():
	winsound.MessageBeep(-1) # Sound played.
	time.sleep(2) # How long between beeps
	winsound.MessageBeep(-1)
	
	while True:  # loop to ask if the user would like to set another alarm
		restart = input("\nWould you like to start another timer? (Y/N):").capitalize()
		if restart == "Y":
			main()
		elif restart == "N":
			print("\nThank you for using the alarm app")
			break
		

def alarm(n):
	
	print()
	print(f"Wait time: {n} seconds.")
	while n != 0: #count down for the time remaining
		mins, secs = divmod(n, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		n -= 1
	print("beep beep!")
	sound()

def input_destinations(user_input):

	if user_input == '1':
		
		user_input = int(input("Enter the number of hours: "))
		
		wait_time = (user_input * 60) * 60
		alarm(wait_time)
	
	elif user_input == '2':
		
		user_input = int(input("Enter the number of minutes: "))
		
		wait_time = user_input * 60
		alarm(wait_time)

	elif user_input == '3':

		user_input = int(input("Enter the number of seconds: "))

		wait_time = user_input
		alarm(wait_time)

	elif user_input == '4':

		hours = int(input("Hours: "))
		minutes = int(input("Minutes: "))
		seconds = int(input("Seconds: "))

		wait_time = ((hours*60)*60) + (minutes*60) + seconds
		print(wait_time)
		alarm(wait_time)

	else:
		
		try:
			os.system('cls') # If OS is Windows
			main()
			
		except:
			os.system('clear') # If OS is Linux or Mac
			main()

def main():
	print("What unit of time do you want to wait?\n (1) Hours\n (2) Minutes\n (3) Seconds\n (4) Combination")
	main_input = input(": ")
	
	input_destinations(main_input)

main()