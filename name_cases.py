first_name = "triston"  #Sets the value of 
last_name = "batemon" 	#
middle_initial = "r"	#

first_and_last = f"{first_name}{last_name}" 							#Joins first and last name variables together
first_middle_and_last = f"{first_name} {middle_initial}. {last_name}" 	#Joins all variables together
upper_case = first_middle_and_last.title()								#Sets variable for title for all variable
all_cap = first_middle_and_last.upper()								
all_lower = first_middle_and_last.lower()	
print(upper_case)
print(all_lower)
print(all_cap)

