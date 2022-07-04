from datetime import date, datetime


def get_dob():
    # write code here
	year=input("pleasae enter your birth Year: ")
	month=input("pleasae enter your birth month: ")
	day=input("pleasae enter your birth day: ")
	x= date(int(year), int(month), int(day))
	return x
	...


def get_age(dob):
    # write code here
	current_date= date(2019,9,4)
	if(dob > current_date):
		return("Sorry, this is invalid Date")
	else:
		if(dob.month > current_date.month):
			return current_date.year - dob.year
		elif(dob.month == current_date.month):
			if(dob.day>=current_date.day):
				return current_date.year - dob.year 
			else:
				return current_date.year - dob.year -1 

		else:
			return current_date.year - dob.year -1 
...


def main():
	x = get_dob()
	age = get_age(x)	
	print(str(age) +" years old")
	# write code here
	...


if __name__ == '__main__':
    main()
