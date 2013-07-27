gender = raw_input("Enter your gender(f/m):")
if gender == "m":
	print "Your cannot join the club."
if gender == "f":
	age = float(raw_input("Enter your age:"))
	if age>=10 and age<=12:
		print "You can join the club."
	else:
		print "You cannot join the club"
