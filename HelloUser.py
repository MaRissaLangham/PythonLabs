usernames = ['Admin', 'Eric', 'John', 'James', 'Jenny']

if usernames:
    for username in usernames:
        if username == 'Admin':
            print("Hello Admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again!")
else:
     print("We need to find some users!")