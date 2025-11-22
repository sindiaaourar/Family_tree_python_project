# F3b - Number of Children

def calculate_number_of_children(family_dict):
    # It creates an empty dictionary called children_count.
    children_count = {}  # This will hold the name of each family member and their number of children.

    # the total_children is set to 0, which will keep track of the total number of children across all family members.
    total_children = 0

    # The function looks at all the family members in the family_dict.
    for person in family_dict.values():
        # It counts their children using len(person.children).
        num_children = len(person.children)
        # It adds their name and the number of their children to the children_count dictionary.
        children_count[person.name] = num_children
        # It updates the total_children by adding this person's number of children.
        total_children += num_children

    # Calculate the average number of children per family member.

    # If the family_dict is empty, the function avoids a division error by setting the average to 0.
    average_children = total_children / len(family_dict) if family_dict else 0

    return children_count, average_children
