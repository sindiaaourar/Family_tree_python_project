# Feature 1b:
class ImmediateExtended: # this class holds both immediate and extended relationships
    def __init__(self, family_dict):

        self.family_dict = family_dict

    def get_immediate_family(self, person_name):

        if person_name not in self.family_dict: #Checks if the person exists in the family tree (family_dict)
            return f"{person_name} not found in the family tree."

        person = self.family_dict[person_name]
        immediate_family = {
            "Parents": person.parents, #Gets their parents directly from the Person object
            "Siblings": person.get_siblings(self.family_dict),#Calls a helper function (get_siblings) to find siblings
            "Spouse": [person.spouse] if person.spouse else [],#Adds the spouse, if any, to the list
            "Children": person.children,#Gets the names of their children
        }

        return immediate_family #It returns all this information as a dictionary

    def get_extended_family(self, person_name):

        if person_name not in self.family_dict:
            return f"{person_name} not found in the family tree." # returns the message if the person is not found in the family tree

        person = self.family_dict[person_name] # Retrieve the Person object for the specified name
        # Initialize a set to store the extended family members
        extended_family = set(person.parents)  # Start with the immediate family
        extended_family.update(person.get_siblings(self.family_dict)) # Add siblings to the extended family

        if person.spouse: # If the person has a spouse, add the spouse to the extended family
            extended_family.add(person.spouse)
        # Add children to the extended family
        extended_family.update(person.children)

        # Iterate through the person's parents to find aunts, uncles, and cousins
        for parent_name in person.parents:
            # Retrieve the parent from the family dictionary
            parent = self.family_dict.get(parent_name)
            if not parent or not parent.parents:
                # Skip if the parent doesn't exist or has no parents (grandparents)
                continue


            for grandparent_name in parent.parents:
                # Retrieve the grandparent from the family dictionary
                grandparent = self.family_dict.get(grandparent_name)
                if not grandparent or not grandparent.children:
                # Skip if the grandparent doesn't exist or has no children
                    continue
                # add aunts / uncle
                for aunt_uncle_name in grandparent.children:
                    # Skip the person's direct parent
                    if aunt_uncle_name != parent_name:
                        # Retrieve the aunt/uncle from the family dictionary
                        aunt_uncle = self.family_dict.get(aunt_uncle_name)
                        if aunt_uncle:
                            extended_family.add(aunt_uncle_name)
                            extended_family.update(aunt_uncle.children)  # Add cousins to the extended family

        # Filter extended family to only include alive members
        extended_family = [name for name in extended_family if self.family_dict[name]]

        return list(extended_family) # Return the list of extended family members
