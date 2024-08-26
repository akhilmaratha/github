# Identify 2 real world examples where you do something which can be repetitive, and implement that as loops.
# Make one loop as a for loop and another as a while loop.
# Use break and continue statements in both loops.
# FOR LOOP
emails = [ "spam@example.com", "boss@example.com", 
          "family@example.com", "spam@example.com", "friend@example.com", "boss@example.com", ]

for email in emails:
    if email == "boss@example.com":
        print(" boss email found!!")
        break
    if email == "spam@example.com":
        print("Spam email found. Skipping this email.")
        continue
    print(f"Checking email from: {email}")

# WHILE LOOP

i = 0
while i < len(emails):
    email = emails[i]
    if email == "boss@example.com":
        print("Boss email found!!")
