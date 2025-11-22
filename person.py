# Feature 1a:
class Person: #define the first class
    def __init__(self, name, surname, dob, parents, spouse, children):
        self.name = name # Initialize the first name of the person
        self.surname = surname # Initialize the last name of the person
        self.dob= dob # Initialize the date of birth of the person
        self.parents = parents or [] # Initialize the list of parents (default to empty list if None is passed)
        self.spouse = spouse or []   # Initialize the list of spouses (default to empty list if None is passed)
        self.children = children or [] # Initialize the list of children (default to empty list if None is passed)

    def full_name (self):
    # combine the firstname and the last name
        return f"{self.name} {self.surname}"
    # method to get the list of parents
    def get_parents(self):
        return self.parents if self.parents else f"not found"
    # method to get the list of spouse
    def get_spouse(self):
        return self.spouse if self.spouse else "not found"
    # method to get the list of grandchildren
    def get_grandchildren(self, family_dict):
        if not self.children:
            return []  # if there's no children it means no grandchildren
        grandchildren = set()
        for child_name in self.children:
            child = family_dict.get(child_name)  # Looking for the child in the family dictionary
            if child:
                grandchildren.update(child.children)  # Add their children (grandchildren)
        # Convert the set of grandchildren to a list and return it, or "not found" if empty
        return list(grandchildren) if grandchildren else "not found"

















