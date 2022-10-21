email = input("Enter your Email here : ").strip()

username = email[:email.index('@')]
domain = email[email.index('@'):]

print(f"Your Email's username is {username}")
print(f"Your Email's domain is {domain}")
