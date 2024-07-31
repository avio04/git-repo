def is_armstrong_number(number):
    # Convert the number to a string to easily iterate through digits
    num_str = str(number)
    num_length = len(num_str)
    
    # Calculate the sum of digits each raised to the power of num_length
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    
    # Check if the sum of powers is equal to the original number
    if sum_of_powers == number:
        return True
    else:
        return False

# Test the function
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
