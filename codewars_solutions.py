#Solution: Even or Odd
#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number):
    
    if number % 2 == 0: 
        return "Even"
    else: 
        return "Odd"
print(even_or_odd(0))

#Solution: Convert a Number to a String
def number_to_string(number):
    return str(number)
print(number_to_string(0))

#Solution: Remove String Spaces
#Create a function that takes a string as an argument and returns a new string with all the
def no_space(string):
    return string.replace(" ", "")

#Solution: Count Vowels
def getCount(string): 
    vowels = "aeiou"
    count = 0
    for character in string:
        if character in vowels: 
            count += 1
    return count

