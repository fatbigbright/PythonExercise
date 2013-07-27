original = input("Enter the price of goods you've bought:")
if original <= 10:
	print "The discount is 10%. The final price is ", original * 0.9
elif original > 10:
	print "The discount is 20%. The final price is ", original * 0.8
