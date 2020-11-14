

import math

while True:
        print("\nChoose the math operation.\n0 - Addtion\n1 - Subraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a Power\n6 - Logarithm\n7 - Square Root\n8 - Sine\n9 - Cosine\n10 - Tangent")

        value = input("\nPlease select your option from the menu:")

        #Addition
        if value == "0":
            val1 = float(input("\nEnter your first number"))
            val2 = float(input("\nEnter your second number"))
            Addition = val1 + val2

            print ("\nThe value for the number added is " + str(Addition) + "\n")

            print ("would you like to continue")
            back = input("\n Go back to the main menu? (y/n)")
            if back == "y":
                continue
            else:
                break


        #Subtraction
        elif value == "1":
            val1 = float(input("\nEnter your first number "))
            val2 = float(input("\nEnter your second number "))
            sub = val1 - val2

            print ("\nThe value for the number subtracted is " + str(sub) + "\n")

            print ("would you like to continue")
            back = input("\n Go back to the main menu? (y/n)")
            if back == "y":
                continue
            else:
                break

        #Multiplication
        elif value == "2":
            val1 = float(input("\nEnter your first number "))
            val2 = float(input("\nEnter your second number "))
            multiply = val1 * val2

            print ("\nThe value for the number multiplied is " + str(multiply) + "\n")

            print ("would you like to continue")
            back = input("\n Go back to the main menu? (y/n)")
            if back == "y":
                continue
            else:
                break

        #Divison
        elif value == "3":
            val1 = float(input("\nEnter your first number "))
            val2 = float(input("\nEnter your second number "))
            division = val1/val2

            print ("\nThe value for the number divided is " + str(division) + "\n")

            print ("would you like to continue")
            back = input("\n Go back to the main menu? (y/n)")
            if back == "y":
                continue
            else:
                break

        #Modulus
        elif value == "4":
            val1 = float(input("\nEnter your first number "))
            val2 = float(input("\nEnter your second number "))
            modulo = val1 % val2

            print ("\nThe Modulus of this number is " + str(modulo) + "\n")

            print ("would you like to continue")
            back = input("\n Go back to the main menu? (y/n)")
            if back == "y":
                continue
            else:
                break

        #Raising to Power
        elif value == "5":
            val1 = float(input("\nEnter your first number "))
            val2 = float(input("\nEnter your second number "))
            power = math.pow(val1,val2)

            print ("\nThe Power of this number is " + str(power) + "\n")

            print ("would you like to continue")
            back = input("\n Go back to the main menu? (y/n)")
            if back == "y":
                continue
            else:
                break

        #Logarithm
        elif value == "6":
            val1 = float(input("\nEnter your first number "))
            logr = math.log(val1, 2)

            print ("\nThe Logarithm of this number is " + str(logr) + "\n")

            print ("would you like to continue")
            back = input("\n Go back to the main menu? (y/n)")
            if back == "y":
                continue
            else:
                break

        #Square Root
        elif value == "7":
            val1 = float(input("\nEnter your first number "))
            squart = math.sqrt(val1)

            print ("\nThe Power of this number is " + str(squart) + "\n")

            print ("would you like to continue")
            back = input("\n Go back to the main menu? (y/n)")
            if back == "y":
                continue
            else:
                break


        #Sine
        elif value == "8":
            val1 = float(input("\nEnter your number in degrees"))
            syn = math.sin(math.radians(val1))

            print ("\nThe Sine of this number is " + str(syn) + "\n")

            print ("would you like to continue")
            back = input("\n Go back to the main menu? (y/n)")
            if back == "y":
                continue
            else:
                break

        #Cosine
        elif value == "9":
            val1 = float(input("\nEnter your number in degrees"))
            cosyn = math.cos(math.radians(val1))

            print ("\nThe Cosine of this number is " + str(cosyn) + "\n")

            print ("would you like to continue")
            back = input("\n Go back to the main menu? (y/n)")
            if back == "y":
                continue
            else:
                break


        #Tangent
        elif value == "10":
            val1 = float(input("\nEnter your number in degrees "))
            tan = math.tan(math.radians(val1))

            print ("\nThe Cosine of this number is " + str(tan) + "\n")

            print ("would you like to continue")
            back = input("\n Go back to the main menu? (y/n)")
            if back == "y":
                continue
            else:
                break


        else:
            print ("\nInvalid Option")
            continue

pass
