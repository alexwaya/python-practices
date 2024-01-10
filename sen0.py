# import re

# def StringChallenge(sen):
#     # Remove punctuation from the string
#     sen = re.sub(r'[^\w\s]', '', sen)
    
#     # Split the string into words
#     longest_string = sen.split()
    
#     # Find the longest word
#     StringChallenge = max(longest_string, key=len)
    
#     # Concatenate the longest word with 'ChallengeToken'
#     sen = StringChallenge + 'ChallengeToken'
    
#     # Replace every third character with 'X'
#     sen = ''.join([c if (i+1) % 3 != 0 else 'X' for i, c in enumerate(sen)])
    
#     return sen

# print(StringChallenge("fun&!! time"))


a = int(input("Enter a: "))
b = int(input("Enter b: "))

def SumTotal():

    sum = a + b   
    return sum
 
print(SumTotal())



 

# def add_two_numbers():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     sum = num1 + num2
#     return sum

# # Call the function
# print(add_two_numbers())
