"""******************************************************************
Author: Marissa Langham
Assignment Number: LAB 6: Adress Book
File Name: AddressBook.py
Date: 08/02/2023
This program will allow the user to enter a name and look up their
phone number, email address, mailing address, city, state, and zip code 
if they are in the address book. if they are not in the address book, 
the user will be prompted to enter their information and it will be 
added to the address book.
******************************************************************"""

import sys

addressBook = {

    'johndoe': {
        'Name': 'John Doe', 
        'Phone': '555-555-5555', 
        'Email': 'jdoe@outlook.com', 
        'Address': '1234 Main St', 
        'City': 'Anytown', 
        'State': 'CA', 
        'Zip': '12345', 
        'Birthday': '01/01/2000', 
        'Notes': 'John is a great guy!'
        }, 
    
    'janedoe': {
        'Name': 'Jane Doe', 
        'Phone': '555-555-5555', 
        'Email': 'janedoe@outlook.com',
        'address': '1234 Main St',
        'City': 'Anytown',
        'State': 'CA',
        'Zip': '12345',
        'Birthday': '01/01/2000',
        'Notes': 'Jane is a great gal!'
        },
    }

# Print a welcome message
print('Welcome to your Address Book!')

# Get user input
userInput = input('Please enter a name to look up their information or "add" to add a new contact')

# Transform user input to lowercase and remove spaces
userInput = userInput.replace(" ", "")
userInput = userInput.lower()

# Check if the user input is in the address book
if userInput == 'add':
    # Gets user's new contact Information
    print('Please enter the following information:')
    
    # Get the user's information
    name = input('Name: ')
    phone = input('Phone Number: ')
    email = input('Email Address: ')
    address = input('Mailing Address: ')
    city = input('City: ')
    state = input('State: ')
    zip = input('Zip Code: ')
    birthday = input('Birthday: ')
    notes = input('Notes: ')
    
    # Create a dictionary for the user's information
    contactName = {'name': name, 'phone': phone, 'email': email, 'address': address, 'city': city, 'state': state, 'zip': zip, 'Birthday': birthday, 'notes': notes}
    
    # Add the user's information to the address book
    addressBook.updated(contactName)
    
    # Print the user's information
    print('Here is the information you entered:')
    
    for key, value in name.items():
        print(key, ':', value)
    
    # Print a goodbye message
    print('Thank you for using your Address Book!')
    
    # Exit the program
    exit()
    
# If the user input is in the address book, print the user's information
elif userInput in addressBook:
    
    # Print the user's information
    print('Here is the information you requested:')

    for key, value in addressBook[userInput].items():
        print(key, ':', value)  
        
# If the user input is not in the address book, prompt the user to add their information 
else:
    print('Sorry, that name is not in your Address Book. Did you want to add them as a new contact..')
    addContact = input('Please enter "yes" or "no"')
    addContact = addContact.replace(" ", "")
    addContact = addContact.lower()
    
    if addContact == 'yes':
        
        # Gets user's new contact Information
        print('Please enter the following information:')
    
        # Get the user's information
        name = input('Name: ')
        phone = input('Phone Number: ')
        email = input('Email Address: ')
        address = input('Mailing Address: ')
        city = input('City: ')
        state = input('State: ')
        zip = input('Zip Code: ')
        birthday = input('Birthday: ')
        notes = input('Notes: ')
        
        # Create a dictionary for the user's information
        name = {'name': name, 'phone': phone, 'email': email, 'address': address, 'city': city, 'state': state, 'zip': zip, 'Birthday': birthday, 'notes': notes}
        
        # Add the user's information to the address book
        addressBook.update(name)
        
        # Print the user's information
        print('Here is the information you entered:')
        for key, value in name.items(): 
            print(key, ':', value)
        
        # Print a goodbye message
        print('Thank you for using your Address Book!')
        
        # Exit the program
        exit()
            
    elif addContact == 'no':
        print('Thank you for using your Address Book!')
        exit()
    else:
        print('Sorry, that is not a valid response. Please try again.')
        exit()
