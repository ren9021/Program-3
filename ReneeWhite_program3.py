#***************************************************************
#
#  Developer:         Renee White
#
#  Program #:         Program 3
#
#  File Name:         <Program3.py>
#
#  Description:       This program is to calculate annual property tax charged for homeowner
#
#***************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():
    
    developerInfo()
    
    ActualValue = float(input('What is the actual value of your house? '))
    CurrentRate = float(input('What is your current tax rate for each 100.00 of assessed value? '))
    AssessedValue = ActualValue * 0.60
    PropertyTax = (AssessedValue / 100.0) * CurrentRate
    print('The annual property tax of your house is', PropertyTax)
    
    
    
    
    
    
    # End of the main function 
    
#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     Renee White')
    print('Program:  3')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1
