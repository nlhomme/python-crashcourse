# 5-8
usernames = ['admin', 'nilho', 'user', 'jack', 'bill']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again")

# 5-9
usernames = []

if not usernames:
    print("We need to check if ")

#5-10
current_users = ['admin', 'nilho', 'user', 'jack', 'bill']
new_users = ['tim', 'bernard', 'isabelle', 'titi', 'jack']

current_users_lowercase = []

for current_user in current_users:
    current_users_lowercase.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lowercase:
        print(f"username {new_user} already used")
    else:
        print(f"username {new_user} available")

# 5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}st")
