# Menu program for Programming Final Project
# Used with Github to ensure that students know the GitHub process.

semester = "ITSE1479 - Spring 2022";

def main():
    #*****************************************************************
    # jumpTable for all functions
    # 
    # Modify your line to create a jumpTable entry for your 
    #   function.  Replace stub() with the name of your function that 
    #   you added to the end this code section.
    #
    # Notes:
    #    jumpTables hold the name of a function, not the variables
    #       that are passed to it.  See smileyFunction for a way
    #       to pass variables manually, 
    #       OR create your own inputs inside of your function to 
    #           collect user input.
    #   Use the following code at the end of your function to 
    #       pause the program
    #           print()
    #           print("Press ENTER to return to the menu")
    #           input()
    #   DO NOT TRASH THE CALL TO main() at the end.  Thanks.
    #*****************************************************************
    jumpTable = {}
    jumpTable['1'] = smileyFunction       # Smiley - call to function goes here
    jumpTable['2'] = stub                 # Alvarez - call to function goes here
    jumpTable['3'] = stub                 # Appiah - call to function goes here
    jumpTable['4'] = stub                 # Balderas - call to function goes here
    jumpTable['5'] = stub                 # Butler - call to function goes here
    jumpTable['6'] = kennedyFunction      # Kennedy - call to function goes here
    jumpTable['7'] = stub                 # Long - call to function goes here
    jumpTable['8'] = stub                 # Nguyen - call to function goes here
    jumpTable['9'] = stub                 # Overby - call to function goes here
    jumpTable['10'] = stub                # Robarge - call to function goes here
    jumpTable['11'] = stub                # Roeper - call to function goes here
    jumpTable['12'] = stub                # Subba - call to function goes here
    jumpTable['13'] = stub                # Thorne - call to function goes here
    jumpTable['14'] = stub                # Thurman - call to function goes here
    jumpTable['15'] = stub                # Valdez - call to function goes here

    chrChoice = ""      # To hold a menu choice

    # Constants for the menu choices
    EXIT = '0';

    while chrChoice != '0':
        # Display the menu and get the user's choice.
        showMenu();
        
        chrChoice = input("Enter your selection (0 to exit): ")
        
        if(chrChoice.isdigit() and int(chrChoice) < (len(jumpTable) + 1)):
            # Validate the menu selection.
            if chrChoice == EXIT:
                print()
                print("Thank for using the", semester, "Menu Program. ")
                print("Have a nice day.")
            else:
                jumpTable[chrChoice]()
        else:
            print("Please enter one of the numeric values from the menu.  Thanks")
            print("Press ENTER to continue.")
            input()    

            

#*****************************************************************
# Definition of function showMenu which displays the menu.       *
#*****************************************************************

def showMenu():
    print("*******************************************************************")
    print("*   Welcome to the ", semester, " Program!")
    print("*      Make a selection from the list below to see student output *")
    print("*                                                                 *")
    print("*      Enter 0 and press Enter to Quit.                           *")
    print("*******************************************************************")

    print("1.  Smiley")
    print("2.  Alvarez")
    print("3.  Appiah")
    print("4.  Balderas")
    print("5.  Butler")
    print("6.  Kennedy")
    print("7.  Long")
    print("8.  Nguyen")
    print("9.  Overby")
    print("10. Robarge")
    print("11. Roeper")
    print("12. Subba")
    print("13. Thorne")
    print("14. Thurman")
    print("15. Valdez")
    print()

# *****************************************************************************************
# Function Definitions Section
# *****************************************************************************************
# Add your function below.  
#  
# FunctionName:  lastnameFunction(your parameters)
# *****************************************************************************************

# *****************************************************************************************
# FUNCTION:         stub (default for menu)
# DESCRIPTION:      stub function created to print a single message: Not Implemented Yet
# OUTPUT EXAMPLE:   User enters any jumpTable entry that has not been created yet
# *****************************************************************************************
def stub():
    print()
    print()

    print("Not implemented at this time.  Check back later.")
    print("Press ENTER to continue.")
    input()    

# *****************************************************************************************
# FUNCTION:         smileyFunction
# DESCRIPTION:      calls SmileyFib with a parameter of 11
#                   prints the Fibonacci series as defined by the input value
# OUTPUT EXAMPLE:   User enters 11
#                   Program outputs the following:
#                      Fibonacci Sequence (9 iterations): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# *****************************************************************************************
def smileyFunction():
    smileyFib(11)
    print("Press ENTER to continue.")
    input()    

def smileyFib(numberOfTimes):
    current = 0
    nextOne = 1
    nextTerm = 0

    print()
    print()
    print("Fibonacci Sequence (", str(numberOfTimes)," iterations)")

    for i in range(0, numberOfTimes):
        if (i == 1):                    # Prints the first term
            print(str(current), end= '')

        elif (i == 2):                 # Prints the second term
            print(str(nextOne), end = '')
        else:                          # Prints all subsequent terms
            nextTerm = current + nextOne;
            current = nextOne;
            nextOne = nextTerm;

            print(str(nextTerm), end = '')

        if (i + 1) < numberOfTimes:
            print(", ", end = '')

    print()
    print()

# *****************************************************************************************
# FUNCTION:         kennedyFunction
# DESCRIPTION:      a range based for loop iterates over the first 10 integers (0-9),
#                   each iteration passes the iterator to the kennedyFactorial function call
#                   that uses recursion to compute the factorial of the corresponding integer
# OUTPUT EXAMPLE:   range is set to 10
#                   Program prints the factorials of 0! through 9!
# *****************************************************************************************
def kennedyFunction():
    
    print("\nThe factorials of the first 10 non-negative integers:\n")

    for i in range(10):
       print(str(i) + "! =", kennedyFact(i)) 
       
    print("\nPress ENTER to continue.")
    input()   
           
def kennedyFact(n):
   """kennedyFact(int): 
       Computes the factorial of a non-negative integer using recursion"""

   if n == 0 or n == 1:  
       return 1  
   else:  
       return n * kennedyFact(n - 1)
    
#*****************************************************************
# Please leave me alone,
#   Sincerely,
#       main()
#*****************************************************************


main()
