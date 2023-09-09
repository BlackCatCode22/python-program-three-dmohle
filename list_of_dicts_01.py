# This is a sample Python script

# Define functions here
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # Use a breakpoint in the code line below to debug your script.
    # Use a breakpoint in the code line below to debug your script.
    # Use a breakpoint in the code line below to debug your script.
    # Use a breakpoint in the code line below to debug your script.

# Create a dictionary.
# my_dict = {"name": "YourNameHere"}
my_dict = {"name": "Dennis Mohle", "phone": "559-321-1234", "email": "dmohle@gmail.com" }
print(type(my_dict))
print("\n\n")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("\n\n")

# Create a list of dict objects.
my_list_of_contacts = []
my_list_of_contacts.append(my_dict)
print("\n")
print(my_list_of_contacts)

# do this again for a second contact

# Create a dictionary.
# my_dict = {"name": "YourNameHere"}
my_dict = {"name": "Donald Duck", "phone": "559-308-1234", "email": "donduck@gmail.com" }
print(type(my_dict))
print("\n\n")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("\n\n")

# Create a list of dict objects.
# my_list_of_contacts = []
my_list_of_contacts.append(my_dict)
print("\n")
print(my_list_of_contacts)

# Iterate through the list and print key-value pairs for each dictionary
for my_dict in my_list_of_contacts:
    for key, value in my_dict.items():
        print(f"{key}: {value}")
    print()  # Print an empty line to separate the dictionaries











