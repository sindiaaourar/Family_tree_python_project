import csv
from person import Person
from immediate_extended import ImmediateExtended
from family_member import FamilyMember
from birthday_calendar import BirthdayCalendar
from number_of_children import calculate_number_of_children  # Import the function



# Read family data from a CSV file and create a dictionary of FamilyMember objects
def parse_csv(filename):
    family_dict = {} # Store family members by name
    with open(filename, "r") as file:
        reader = csv.DictReader(file) # Read the CSV file as a dictionary
        for row in reader:
            # Normalize name fields by stripping and lowercasing
            name = row["name"].strip().lower()
            family_member = FamilyMember(
                name=name,
                surname=row["surname"].strip(),
                dob=row["dob"].strip(),
                parents=[p.strip().lower() for p in row["parents"].split(", ") if p.strip()] if row["parents"] else [],
                spouse=row["spouse"].strip().lower() if row["spouse"] else None,
                children=[c.strip().lower() for c in row["children"].split(", ") if c.strip()] if row["children"] else [],
            )
            family_dict[name] = family_member # Add to dictionary
    return family_dict


def main(): # Main function to run the program
    # Load family data from CSV
    family_dict = parse_csv("family_data.csv")

    # Initialize the classes for FamilyMember, ImmediateExtended, and BirthdayCalendar
    immediate_extended = ImmediateExtended(family_dict)
    birthday_calendar = BirthdayCalendar(family_dict)

    while True:
        # Show menu options
        print("\nFamily Tree Options:")
        print("1. Get Parents of an Individual")
        print("2. Get Grandchildren of an Individual")
        print("3. Get Immediate Family of an Individual")
        print("4. Get Extended Family of an Individual")
        print("5. Get Siblings of an Individual")
        print("6. Get Cousins of an Individual")
        print("7. Display Family Birthdays")
        print("8. Display Family Birthday Calendar")
        print("9. Calculate Number of Children and Average")
        print("10. Exit")

        # Ask the user to choose an option
        choice = input("\nEnter the number of your choice: ")

        if choice == '10': # Exit the program
            print("Exiting the program.")
            break

        if choice == '9':  # Calculate Number of Children
            children_count, average_children = calculate_number_of_children(family_dict)
            print("\nNumber of Children for Each Individual:")
            for name, count in children_count.items():
                print(f"{name}: {count}")
            print(f"\nThe average number of children per person is: {average_children:.2f}.")

        else:
            # Get the person's name
            person_name = input("\nEnter the name of the individual: ")

            if person_name not in family_dict:
                print(f"{person_name} not found in the family tree.")
                continue  # Ask again if the name is not found

            selected_person = family_dict[person_name] # Get the selected family member from the dictionary

            # Handle the user's choice
            if choice == '1':  # Get Parents
                print(f"=== {person_name}'s Parents ===")
                print(selected_person.get_parents())

            elif choice == '2':  # Get Grandchildren
                print(f"=== {person_name}'s Grandchildren ===")
                grandchildren = selected_person.get_grandchildren(family_dict)
                if grandchildren == "not found":
                    print("No grandchildren found.")
                else:
                    for grandchild in grandchildren:
                        print(grandchild)

            elif choice == '3':  # Get Immediate Family
                print(f"=== {person_name}'s Immediate Family ===")
                immediate_family = immediate_extended.get_immediate_family(person_name)
                for relation, members in immediate_family.items():
                    print(f"{relation}: {', '.join(members) if members else 'not found'}")

            elif choice == '4':  # Get Extended Family
                print(f"=== {person_name}'s Extended Family ===")
                extended_family = immediate_extended.get_extended_family(person_name)
                if extended_family:
                    print(", ".join(extended_family))
                else:
                    print("No extended family found.")

            elif choice == '5':  # Get Siblings
                print(f"=== {person_name}'s Siblings ===")
                family_member = FamilyMember(selected_person.name, selected_person.surname, selected_person.dob,
                                             selected_person.parents, selected_person.spouse, selected_person.children)
                siblings = family_member.get_siblings(family_dict)
                if siblings:
                    print(", ".join(siblings))
                else:
                    print("No siblings found.")

            elif choice == '6':  # Get Cousins
                print(f"=== {person_name}'s Cousins ===")
                family_member = FamilyMember(selected_person.name, selected_person.surname, selected_person.dob,
                                             selected_person.parents, selected_person.spouse, selected_person.children)
                cousins = family_member.get_cousins(family_dict)
                if cousins:
                    print(", ".join(cousins))
                else:
                    print("No cousins found.")

            elif choice == '7':  # Display Family Birthdays
                print(f"=== Family Birthdays ===")
                birthdays = birthday_calendar.get_all_birthdays()
                for name, dob in birthdays:
                    print(f"{name}: {dob}")

            elif choice == '8':  # Display Family Birthday Calendar
                print(f"=== Family Birthday Calendar ===")
                common_birthday_calendar = birthday_calendar.get_common_birthdays()
                for date, names in common_birthday_calendar:
                    print(f"{date}: {', '.join(names)}")

            else:
                print("Invalid option, please try again.") # Handle invalid options


if __name__ == "__main__": # Run the main function
    main()  # Start the program
