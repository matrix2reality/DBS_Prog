##  Payroll Calculator
# Svetlana Nicolenco
# May 2017

# receive input for employee name
def get_empName():
    print()
    while True:
        empName = raw_input('Please enter your Firstaname and Lastname: ')
        if all(char.isalpha() and len(empName)< 35 for char in empName):
            break
        print("Please enter a valid name! :c")
    print()
    return empName
	
# get employee ID
def get_empID():
    print()
    while True:
        empID = raw_input('Please enter your employee number: ')
        if all(is_alphanumeric() and len(empName)< 10 for char in empName) () :
            break
        print("Please enter a valid ID! :c")
    print()
    return empID

### get week ending date
from datetime import datetime
def validate(datetime_string):
        try:
            return datetime.strptime(datetime_string,"%d/%m/%Y %I:%M %p")   ### "%m/%d/%Y %I:%M %p"
        except ValueError:
            return False

### get total hours worked per week by the employee and their pay rate			
def get_weekHrs(weekHrs, payRate):
    weekHrs = int(raw_input('Please enter hours/week worked: '))
    while weekHrs > 60 or weekHrs < 1:
        print ('Please enter your normal working hours')
        weekHrs = int(raw_input('Please enter hours/week worked: '))
    payRate = float(input('Please enter your pay rate (hour)?: '))
    while payRate < 1.00 or payRate > 50.00:
        print ('Please enter a valid payRate')
        payRate = float(input('Please enter your pay rate (hour)?: '))
    return whrs, payRate

### calculate total hours worked 	
def compute_totHrs(weekHrs):
    if weekHrs <= 37.5:
        return [weekHrs, False]
    else:
        overtime = weekHrs - 37.5
        return [overtime, True]



### calculate overtime 	hours and overtime payment 
def compute_overtimePay(normHrs, oHrs, oPay):
    oRate = 1.5 * payRate
    normHrs = min(weekHrs, 37.5)
    oHrs = max(weekHrs-37.5, 0)
    oPay = oHrs * oRate
    return normHrs, oHrs, oPay

### calculate nett payment 
def compute_netPay(netPay, taxCharge):
    taxSum = (totPay * taxRate) / 100
	taxCharge = round(taxDeductions, 2)
	netPay = totPay + oPay - taxCharge
	netPay = round(netPay, 2)
    return netPay, taxCharge

		
def printPayslip1(EmpName, ID, Hrs, Rate, Total, TaxRate, TaxCharge, Nett):		
	 print('Payroll Information\n')
     print('Pay rate  $',format(rate,'7.2f'))
     print('Regular Hours  ',format(hours, '2.0f'))
     print('Overtime Hours  0')
     print('Regular pay  $',format(hours * rate,'7.2f'))
     print('Overtime pay  $ 0.00')
     print('Total pay:  $',format(hours * rate, '7.2f'))
	 
def printPayslip2(EmpName, ID, Hrs, Rate, Total, TaxRate, TaxCharge, Nett):
	print('Payroll Information\n')
	print('Pay rate  $',format(rate,'7.2f'))
    print('Regular Hours  ',format(hours, '2.0f'))
    print('Overtime Hours  $',format(othours, '2.0f'))
    print('Regular pay  $',format(hours * rate,'7.2f'))
    print('Overtime pay  $',format(otpay, '7.2f'))
    print('Total pay:  $',format(regularpay + otpay, '7.2f'))	
	
def main():
    empName, empID, weekEnds, weekHrs, payRate = getInput()
    if totPay(totHrs(weekHrs), payRate) == None:
    printPayslip1(EmpName, ID, Hrs, Rate, Total, TaxRate, TaxCharge, Nett):   
    else:
    otpay, regularpay, othours = rateCal(timeCal(hours), rate)        
main()



#display/print payslip
def printPayslip(EmpName, ID, Hrs, Rate, Total, TaxRate, TaxCharge, Nett):
  print 
  print '---------------PAYSLIP------------------'
  print '-------------WEEK ENDING' weekEnds
  print
  print 'Employee\n', % EmpName
  print 'Number $%6.0f.', % empID
  print 'Earnings --------------------------Deductions'
  print '-----------Hours---Rate---Total-----------'
  print 'Hours (normal)', Hrs, Rate, Total, TaxRate
  print 'Overtime', Hrs, Rate, Total
  print 'Gross Pay: %g' %(grossPay)
  'Deductions', TaxCharge
  print 'Nett pay', Nett
  print
  