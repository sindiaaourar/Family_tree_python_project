# F2a - Siblings and Cousins
from person import Person
# I imported the Person class from the 'person' file because the FamilyMember class is inheriting from it.

class FamilyMember(Person):

    def __init__(self, name, surname, dob, parents, spouse, children):
        # I called the constructor of the parent class (Person).
        super().__init__(name, surname, dob, parents, spouse, children)

    # Method to get the siblings of the current FamilyMember.
    def get_siblings(self, family_dict):
        # If the current person has no parents, they cannot have siblings.
        if not self.parents:
            return []

        siblings = set()  # Initialize a set instead of a list to store siblings avoiding duplicates.

        # Loop through the names of the person's parents.
        for parent_name in self.parents:
            # The method checks the family_dict (a dictionary that stores family members) to find the parent's details.
            parent = family_dict.get(parent_name)
            if parent:  # If the parent exists in the family dictionary:
                # The method goes through the list of that parent’s children (names).
                for sibling_name in parent.children:
                    #  it checks if the name is different from the current person’s name
                    if sibling_name != self.name:
                        # If it’s a different name, it adds it to the siblings set.
                        siblings.add(sibling_name)

        # Convert the set of siblings to a list and return it.
        return list(siblings)

    # Method to get the cousins of the current FamilyMember.
    def get_cousins(self, family_dict):
        # If the current person has no parents, they cannot have cousins.
        if not self.parents:
            return []

        cousins = set()  # I used a set instead of a list to avoid duplicates.

        # Loop through the names of the person's parents.
        for parent_name in self.parents:
            # The method checks the family_dict (a dictionary that stores family members) to find the parent's details.
            parent = family_dict.get(parent_name)

            if not parent or not parent.parents:
                continue  # Skip if the parent or their parents (grandparents) are missing.

            # Loop through the names of the parent's parents (grandparents).
            for grandparent_name in parent.parents:
                # If the parent has their own parents listed, the method retrieves these grandparents from the family_dict.
                grandparent = family_dict.get(grandparent_name)

                if not grandparent or not grandparent.children:
                    continue  # Skip if the grandparent or their children are missing.

                # Loop through the grandparent's children (aunts and uncles).
                for sibling_name in grandparent.children:
                    # Exclude the parent from the list of siblings.
                    if sibling_name != parent_name:
                       # for each grandparent it checks their list of children (the siblings of the current person’s parent).
                        sibling = family_dict.get(sibling_name)
                        # If the sibling has children, add them as cousins.
                        if sibling and sibling.children:
                            cousins.update(sibling.children)

        # Convert the set of cousins to a list and return it.
        return list(cousins)
