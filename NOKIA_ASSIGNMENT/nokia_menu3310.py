main_menu = """
Welcome to Nokia3310Menu Service
 
 1  Phone Book
 2  Messages
 3  Chat
 4  Call Register
 5  Tones
 6  Setting
 7  Call Divert
 8  Games
 9  Calculator
 10  Reminders
 11  Clock
 12  Profiles
 13  SIM Services

"""		
print(main_menu)
main_menu_choice = int(input("enter a number: "))

match main_menu_choice:
	case 1 : 
		print("Phone Book") 
		phone_book_menu = """
1  Search
2  Service Nos
3  Add name
4  Erase
5  Edit
6  Assign tone
7  Send b'card
8  Options
9  Speed dials
10  Voice tags
"""
		print(phone_book_menu)
		phone_book_menu_choice = int(input("enter a number"))

		match phone_book_menu_choice: 
			case 1 : 
				print("Search")
			case 2 : 
				print("Services Nos")
			case 3 : 
				print("Add name") 
			case 4 : 
				print("Erase") 
			case 5 : 
				print("Edit") 
			case 6 : 
				print("Assign tone") 
			case 7 : 
				print("Send b'card") 
			case 8 : 
				print("Options") 
				option_menu = """
1. Type of view
2. Memory status
"""

				print(option_menu)
				option_menu_choice = int(input("enter a number"))
				match option_menu_choice:
					case 1 : 
						print("Type of view")
					case 2 : 
						print("Memory status")
					case _ : 
						print("not valid") 
				 			
						
			case 9 : 
				print("Speed dials") 
			case 10 : 
				print("Voice tages") 
			case _ : 
				print("not valid")			
						

	case 2 : 
		print("Messages")
		messages_menu = """
1. Write messages
2. Inbox
3. Outbox
4. Picture message
5. Templates
6. Smileys
7. Messages settings
8. info service
9. voice mainbox number
10. Sevice command editor
"""
		
		print(messages_menu)
		messages_menu_choice = int(input("enter a number: "))

		match messages_menu_choice:
			case 1 : 
				print("Write Messages") 
			case 2 : 
				print("Inbox")
			case 3 : 
				print("Outbox")
			case 4 : 
				print("Picture Message") 
			case 5 : 
				print("Templates") 
			case 6 : 
				print("Smileys") 
			case 7 : 
				print("Messages Settings") 
				messages_settings_menu = """
1. Set 1
2. Common 
"""  
				print(messages_settings_menu)
				messages_settings_menu_choice = int(input("enter a number: "))

				match messages_settings_menu_choice: 
					case 1 : 
						print("set 1") 
						set1_menu = """

1. Message centre number
2. Messages sent as 
3. Message validity
"""

						print(set1_menu)
						set1_menu_choice = int(input("enter a number: "))

						match set1_menu_choice:
							case 1 : 
								print("Message centre number") 
							case 2 : 
								print("Messages sent as") 
							case 3 : 
								print("Message validity") 
							case _ :  
								print("not valid")


					case 2 : 
						print("Common") 
						common_menu = """
					

					 

1. Delivery reports
2. Reply via same centre
3. Character support
""" 
		
						print(common_menu)
						common_menu_choice = int(input("enter a number: "))

						match common_menu_choice:
							case 1 : 
								print("Delivery reports")
							case 2 : 
								print("Reply via same centre") 
							case 3 : 
								print("Character support") 
							case _ : 
								print("not valid")





			case 8 : 
				print("info service") 
			case 9 : 
				print("Voice mainbox number") 
			case 10 : 
				print("Service command editor") 
			case _ : 
				print("not valid")		



	case 3 : 
		print("Chat") 
	case 4 : 
		print("Call_Register") 
		call_register_menu = """	
1. Missed call
2. Recieved calls
3. Dialled number
4. Erase recent call lists
5. Show call duration
6. Show call cost
7. call cost settings
8. prepaid credit
"""
		print(call_register_menu)
		call_register_menu_choice = int(input("enter a number: "))

		match call_register_menu_choice:
			case 1 : 
				print("Missed call") 
			case 2 : 
				print("Recieved calls") 
			case 3 : 
				print("Dialled number")
			case 4 : 
				print("Erase recent call lists") 
			case 5 : 
				print("Show call duration") 
				show_call_duration_menu = """

1. Last call duration
2. All calls duration
3. Recieved calls duration
4. dialled calls duration
5. cleared timer
"""
				print(show_call_duration_menu)
				show_call_duration_menu_choice = int(input("enter a number: "))

				match show_call_duration_menu_choice:
					case 1 : 
						print("Last call duration") 
					case 2 : 
						print("All calls duration") 
					case 3 : 
						print("Recieved calls duration")
					case 4 : 
						print("Dialled calls duration")
					case 5 : 
						print("cleared timer") 
					case _ : 
						print("not valid")
							
						
			case 6 : 
				print("Show call cost") 
				show_call_cost_menu = """
1. Show last call cost
2. All calls cost
3. Clear counters
"""
				print(show_call_cost_menu)
				show_call_cost_menu_choice = int(input("enter a number: "))
				match show_call_cost_menu_choice:
					case 1 : 
						print("show last call cost") 
					case 2 : 
						print("All calls cost") 
					case 3 : 
						print("Clear counters") 
					case _ : 
						print("not valid")
							
						
			case 7 : 
				print("Call cost settings") 
				call_cost_settings_menu = """
1. Call cost limit
2. Show cost in
"""
				print(call_cost_settings_menu)
				call_cost_settings_menu_choice = int(input("enter a number: "))
				match call_cost_settings_menu_choice:
					case 1 : 
						print("Call cost limit") 
					case 2 : 
						print("Show cost in") 
					case _ : 
						print("not valid")
							
						
			case 8 : 
				print("Prepaid credit") 
			case _ : 
				print("not valid")

			
	case 5 : 
		print("Tones")
		tones_menu = """
1. Ringig tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Messages alert tone
6. Keypad tone
7. Warning and game tones
8. Vibrating alert
9. Screen saver
"""
		print(tones_menu)
		tones_menu_choice = int(input("enter a number: "))
		match tones_menu_choice:
			case 1 : 
				print("Ringing tone") 
			case 2 : 
				print("Ringing volume") 
			case 3 : 
				print("Incoming call alert") 
			case 4 : 
				print("Composer") 
			case 5 : 
				print("Messages alert tone") 
			case 6 : 
				print("Keypad tone") 
			case 7 : 
				print("Warning and game tones") 
			case 8 : 
				print("Vibrating alert") 
			case 9 : 
				print("Screen saver") 
			case _ : 
				print("not valid")


	case 6 : 
		print("Settings")
		setting_menu = """
1. Call setting
2. Phone setting
3. Security setting
4. Restore factory settings
"""
		print(setting_menu)
		setting_menu_choice = int(input("enter a number: "))
		match setting_menu_choice:
			case 1 : 
				print("Call setting")
				call_setting_menu = """
1. Automatic redial
2. Speed dialling
3. call waiting option
4. Own number sending
5. Phone line in use
6. Automatic answer
"""
				print(call_setting_menu)
				call_setting_menu_choice = int(input("enter a number: "))
				match call_setting_menu_choice:
					case 1 : 
						print("Automatic redial") 
					case 2 : 
						print("Speed dialling") 
					case 3 : 
						print("call waiting option") 
					case 4 : 
						print("Own number sending") 
					case 5 : 
						print("Phone line in use") 
					case 6 : 
						print("Automatic answer") 
					case _ : 
						print("not valid")


			case 2 : 
				print("Phone setting")
				phone_setting_menu = """
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Light
6. Comfirm SIM service action
"""
				print(phone_setting_menu)
				phone_setting_menu_choice = int(input("enter a number: "))
				match phone_setting_menu_choice:
					case 1 : 
						print("Language") 
					case 2 : 
						print("Cell info display") 
					case 3 : 
						print("Welcome note") 
					case 4 : 
						print("Network selection") 
					case 5 : 
						print("Light") 
					case 6 : 
						print("Comfirm SIM service action") 
					case _ : 
						print("not valid")


			case 3 : 
				print("Security setting")
				security_setting_menu = """
1. Pin code request
2. Call barring service
3. Fixed dialling
4. closed user group
5. Phone security
6. Change access code
"""
				print(security_setting_menu)
				security_setting_menu_choice = int(input("enter a number: "))
				match security_setting_menu_choice:
					case 1 : 
						print("Pin code request") 
					case 2 : 
						print("Call barring service")
					case 3 : 
						print("Fixed dialling") 
					case 4 : 
						print("closed user group") 
					case 5 : 
						print("Phone security") 
					case 6 : 
						print("Change access code") 
					case _ : 
						print("not valid")


			case 4 : 
				print("Restore factory settings") 
			case _ : 
				print("not valid")


	case 7 : 
		print("Call Divert")
	case 8 : 
		print("Games") 
	case 9 : 
		print("Calculator") 
	case 10 : 
		print("Reminders") 
	case 11 : 
		print("Clock") 
		clock_menu = """
1. Alarm clock 
2. Clock settings
3. Date settings
4. Stopwatch
5. Coundown timer
6. Auto update of date and timeaD
"""
		print(clock_menu)
		clock_menu_choice = int(input("enter a number: "))

		match clock_menu_choice:
			case 1 : 
				print("Alarm clock") 
			case 2 : 
				print("Clock settings") 
			case 3 : 
				print("Date settings") 
			case 4 : 
				print("Stopwatch") 
			case 5 : 
				print("Coundown timer") 
			case 6 : 
				print("Auto update of date and time") 
			case _ : 
				print("not valid")



	case 12 : 
		print("Profiles") 
	case 13 : 
		print("SIM Services") 
	case _ : 
		print("not valid")

