username = input('What is your name?')
password = input('What is your password?')

print(
    f'{username}, your password, {password}, is {len(password)} letters long')

# here the password is not hidden when displayed.
# so we can add "print('*' * len(password))" to hide it
# rewriting it as:
username = input('What is your name?')
password = input('What is your password?')

print(
    f'{username}, your password, {"*" * len(password)}, is {len(password)} letters long'
)

# OR we can do the following way to hide it:
username = input('What is your name?')
password = input('What is your password?')

password_length = len(password)
print(
    f'{username}, your password, {"*" * password_length}, is {password_length} letters long'
)

# OR this way to hide it:
username = input('What is your name?')
password = input('What is your password?')

password_length = len(password)
hidden_password = '*' * password_length
print(
    f'{username}, your password, {hidden_password}, is {password_length} letters long'
)
