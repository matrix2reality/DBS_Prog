### ASSIGNMENT 
### Module Code: B8IT102 
### Module Title: B8IT102 Programming Essentials
### Lecturer Name: Eoin Meehan
### Nicolenco Svetlana
### 10265376
### 04 June 2017


### input employee name 
def get_empName():

    invalid = 1
    
    while invalid:
        invalid=0

        empName = raw_input("Please enter your name: ")
        
        if not empName.isalpha():   ### name validation - alphabetic
            print "Please enter a valid name"
            invalid = 1

        elif len(empName) > 35:   ### name validation - no more than 35 char
            print "Please enter a valid name"
            invalid = 1
            
    return empName

name = get_empName()

### get employee number
def get_empID():

    invalid = 1
    
    while invalid:
        invalid=0

        empID = raw_input("Please enter your number: ")
        
        if not empID.isalnum():   ### number validation - alphanumeric
            print "Please enter a valid number"
            invalid = 1

        elif len(empID) > 10:  ### number validation - 10 characters max
            print "Please enter a valid number"
            invalid = 1
            
    return empID

empID = get_empID()

import string

def get_weekDate():
	invalid = 1	

	while invalid == 1:
		invalid = 0			

		weekDate = raw_input("Please enter date for week ending in format dd/mm/yyyy : ")
	

	
		weekDate = string.replace(weekDate, " ", "")
		weekDate = string.replace(weekDate, chr(9), "")
	
# string Validation contains "0"-"9"or "/"

		dd, mm, yyyy = string.split(weekDate, "/")
	
		for ch in weekDate:
			if (ord(ch) < 47 or ord(ch) >59):
				invalid = 1
				print "Please eneter a valid date : ",ch

# Now check the others

		if invalid != 1:
			idd, imm, iyyyy = int(dd), int(mm), int(yyyy)
		
			if len(weekDate) != 10:  ### date validation - 10 characters 
				print "Please enter a valid date"
				invalid = 1
			elif string.count(weekDate,"/") != 2:   ### date validation - 2 '/'
				print "Please enter a valid date"
				invalid = 1
			elif imm < 1 or imm > 12:  ### month validation 1-12 
				print "Please enter a valid date"
				invalid = 1
			elif idd <1 or idd > 31:   ### date validation 1-31 
				print "Please enter a valid date"
				invalid = 1
	return weekDate
	
week = get_weekDate()

### get hours per week form the employee
def get_weekHrs():
    weekHrs = float(raw_input('Please enter hours/week worked: '))
    while weekHrs > 60 or weekHrs < 1:
        print ('Please enter your normal working hours')
        weekHrs = float(raw_input('Please enter hours/week worked: '))
    payRate = float(input('Please enter your pay rate (hour)?: '))
    while payRate < 1.00 or payRate > 50.00:
        print ('Please enter a valid payRate')
        payRate = float(input('Please enter your pay rate (hour)?: '))
    return weekHrs, payRate
	
weekHrs, payRate = get_weekHrs()

### get a tax rate in a range 10%, 17.5%, 20%		
def get_taxRate():

    invalid = 1
    
    while invalid:
        invalid=0

        taxRate = float(raw_input("Please enter your tax rate: "))
        if (taxRate != 10 and
           taxRate != 17.5 and
           taxRate != 20):
           print "Please enter your tax rate."
           invalid = 1
           
            
    return taxRate

taxRate = get_taxRate()

### calculate overtime 	hours and overtime payment 
def computepay():

    if weekHrs < 37.5:
        normHrs = weekHrs
        overHrs = 0
    else:
        normHrs = 37.5
        overHrs = weekHrs - 37.5

    if weekHrs > 37.5:
        overRate = 1.5 * payRate
        overPay = (weekHrs-37.5) * overRate
    else:
        overPay = 0

    return normHrs, overHrs, overPay

normHrs, overHrs, overPay  = computepay()

def calculate_grossPay():
    standPay = normHrs * payRate
    grossPay = standPay + overPay
	
    return standPay, grossPay
	
standPay, grossPay = calculate_grossPay()


taxAmount = (grossPay * taxRate)/100
nettSalary = grossPay - taxAmount 
    
print 
print '---------------PAYSLIP------------------'
print '--------WEEK ENDING', week
print
print 'Employee Name', name
print 'Number', empID
print 'Earnings ---------------------Deductions'
print '------------------Hours----Rate-----Total----tax rate(%)'
print 'Hours (normal)', weekHrs, payRate, grossPay, taxRate
print '-----------overtime hours---overtime pay----tax amount'
print 'Overtime', overHrs, overPay, taxAmount
print
print 'Your gross salary are $%.2f.' % grossPay
print 'your net salary are $%.2f.' % nettSalary


