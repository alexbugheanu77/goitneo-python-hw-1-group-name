# goitneo-python-hw-1-group-name
DOCUMENTATION

Function Documentation: Task 1

Overview:

This function takes a list of dictionaries containing user information, including their names and birthdays, and returns a dictionary mapping each day of the current week to a list of colleagues who have birthdays on that day.
Parameters:

    users (list): A list of dictionaries where each dictionary represents a user. Each dictionary should have keys "name" and "birthday", with corresponding values being the user's name (string) and their birthday (datetime object).

Returns:

    birthdays_per_week (defaultdict): A defaultdict where keys are strings representing days of the week (e.g., "Monday", "Tuesday", etc.), and values are lists of names of colleagues whose birthdays fall on that day within the current week.

Implementation Details:

    Initialization:
        Initializes an empty defaultdict named birthdays_per_week to store birthdays grouped by the day of the week.
        Retrieves the current date using datetime.today().date().

    Iterating Through Users:
        Loops through each user in the users list.
        Extracts the user's name and birthday from each user dictionary.
        Determines the birthday for the current year using birthday.replace(year=current_date.year).
        Adjusts the birthday to the next year if it has already passed in the current year.
        Calculates the number of days until the birthday using delta_days.

    Grouping Birthdays by Weekday:
        If the birthday falls within the current week (0 to 6 days away), it categorizes the birthday under the corresponding day of the week.
        Adjusts Saturday and Sunday birthdays to Monday for easier display.

    Displaying the Results:
        Loops through the birthdays_per_week defaultdict.
        Converts the list of names for each day into a comma-separated string.
        Prints the day of the week followed by the names of colleagues with birthdays on that day.

    Return Value:
        Returns the birthdays_per_week defaultdict containing the grouped birthdays.

------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------
Chatbot Documentation: Task 2

Overview:

This program implements a simple command-line based chatbot that acts as a contact manager. Users can interact with the bot by entering commands to add, update, view contacts, and perform other related operations.
Functionality

The chatbot supports the following commands:

    hello: Greets the user and prompts for input.
    add [name] [phone_number]: Adds a new contact with the specified name and phone number.
    change [phone_number] [name]: Updates the contact information by replacing the old name associated with the given phone number.
    phone [name]: Retrieves and displays the phone number associated with the provided name.
    all: Displays all contacts stored in the bot's memory.
    goodbye, close, exit: Terminates the chat session.

Functions
parse_input(user_input)

    Description: Parses the user input to extract the command and arguments.
    Parameters:
        user_input: A string representing the input provided by the user.
    Returns: A tuple containing the command and its arguments.

add_contact(args, contacts)

    Description: Adds a new contact to the bot's contact list.
    Parameters:
        args: A tuple containing the name and phone number of the contact.
        contacts: A dictionary representing the contact list.
    Returns: A string indicating the success of the operation.

update_contact(args, contacts)

    Description: Updates an existing contact's information.
    Parameters:
        args: A tuple containing the new phone number and name of the contact.
        contacts: A dictionary representing the contact list.
    Returns: A string indicating the success of the operation.

show_phone(args, contacts)

    Description: Retrieves and displays the phone number associated with the provided name.
    Parameters:
        args: A tuple containing the name of the contact.
        contacts: A dictionary representing the contact list.
    Returns: The phone number associated with the provided name.

show_all(contacts)

    Description: Displays all contacts stored in the bot's memory.
    Parameters:
        contacts: A dictionary representing the contact list.
    Returns: A dictionary containing all contacts.

main()

    Description: Main function controlling the flow of the chatbot.
    Behavior:
        Initializes an empty contact list.
        Prompts the user for input in a loop.
        Parses the input, executes the corresponding command, and displays the result.
        Terminates the loop and ends the session upon receiving exit-related commands.

Usage

To run the chatbot, execute the script. Follow the prompts and enter commands as instructed. The bot will respond accordingly, performing actions such as adding contacts, updating contact information, displaying phone numbers, or showing all contacts.