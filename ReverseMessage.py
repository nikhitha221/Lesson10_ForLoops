message = input("Enter your message")
reverse = " "
for char in message:
    reverse = char + reverse
print("Your original message is" , message)
print("Your reversed message is", reverse)