problem = "problem1"
student_name = "Beemnet_Amdissa_Teshome"
student_number = "T0338757"

#function for Part A
def months_to_DP(total_cost_of_house, 
                 annual_salary, proportion_saved):
    # your code here
    
    down_payment = 0.25 * total_cost_of_house
    current_savings = 0.0
    monthly_salary = annual_salary / 12.0
    monthly_return_rate = 0.05 / 12.0
    month_count = 0

    # Continue looping until current savings reach the down payment
    while current_savings < down_payment:
        # Accumulate interest on current savings first
        current_savings += current_savings * monthly_return_rate
        # Add money from the monthly savings
        current_savings += monthly_salary * proportion_saved
        month_count += 1

    
    print(f"It will take you {month_count} to save up for the down payment.")
    #print('months_to_DP not implemented')
    return month_count

#function for Part B
def months_with_biannual_raise(total_cost_of_house, 
                 annual_salary, proportion_saved, biannual_raise):
    # your code here

    down_payment = 0.25 * total_cost_of_house
    current_savings = 0.0
    monthly_salary = annual_salary / 12.0
    monthly_return_rate = 0.05 / 12.0
    month_count = 0

    # Continue looping until current savings reach the down payment
    while current_savings < down_payment:
        # Accumulate interest on current savings first
        current_savings += current_savings * monthly_return_rate
        # Add money from the monthly savings
        current_savings += monthly_salary * proportion_saved
        month_count += 1

        # Update the annual salary every 6 month based on the biannual raise
        if month_count % 6 == 0:
            annual_salary += (1 + biannual_raise)
            monthly_salary = annual_salary / 12


    print(f"It will take you {month_count} to save up for the down payment.")
    #print('months_with_biannual_raise not implemented')
    return month_count

#function for Part C
import random

def bisection_search():
    # your code here
    print("*************\n"
    "Bisection Search\n"
    "*******************\n")
    
    print("""Think of a number between 1 and 10,000. I'll try to guess the number using 
          bisection search. Please respond with :
          'y' if the guess is correct.
          'h' if the number is higher than my guess.
          'l' if the number is lower than my guess.""")
    
    low = 1
    high = 10000
    guesses = 0
    found = False

    while low <= high:
        guess = (low + high) // 2
        guesses += 1
        response = input(f"Is your number {guess}? (y/h/l): ").lower()

        if response == 'y':
            found = True
            print(f"I guessed your number {guess} in {guesses} guesses!")
            break
        elif response == 'h':
            low = guess + 1
        elif response == 'l':
            high = guess - 1
        else:
            print("Invalid input. Please enter 'y', 'h', or 'l'.")
    
    if not found:
        print("Hmm, I couldn't find your number. Did you make an error in your responses?")


    #print('bisection_search not implemented')

months_to_DP(500000, 80000, .2)
print('\n')
months_with_biannual_raise(500000, 80000, .2, .1)