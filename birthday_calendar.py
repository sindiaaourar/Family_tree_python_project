# F2b-Birthdays and Birthdays in Common.

class BirthdayCalendar:

    def __init__(self, family_dict):
        # Store the dictionary of all Person objects.
        self.family_dict = family_dict  

    # Method to display all birthdays.
    def get_all_birthdays(self):
        birthdays = []  # The method creates an empty list called birthdays where all the collected birthday information will be stored.

        # It looks at every family member in the family_dict
        for name, member in self.family_dict.items():
            # For each family member, the method creates a pair that contains their name and their dob.
            birthdays.append((name, member.dob))  # the pair is added to the list.
        # Return the complete list of birthdays.
        return birthdays

    # Method to display common birthdays grouped by date (ignoring the year).
    def get_common_birthdays(self):
        birthday_calendar = {}  # an empty dictionary to group birthdays by date is created.

        # Loop through all family members in the dictionary.
        for name, member in self.family_dict.items():
            # #The method extracts just the day and month from the dob, ignoring the year.
            day_month = "/".join(member.dob.split("/")[:2])

            # It checks if this "day/month" is already in the dictionary.
            if day_month in birthday_calendar:
                # If it is, the person's name is added to the existing list for that date.
                birthday_calendar[day_month].append(name)  
            else:
                # If it isn't, a new entry is created with the name in a list.
                birthday_calendar[day_month] = [name]  

        # Sort the birthday calendar by date (month and day).
        sorted_calendar = sorted(
            birthday_calendar.items(),  # Convert the dictionary to a list of items for sorting.
            # Sort by month first and then by day (both converted to integers).
            key=lambda x: (int(x[0].split("/")[1]), int(x[0].split("/")[0]))
        )
        # Return the sorted calendar as a list of tuples.
        return sorted_calendar
