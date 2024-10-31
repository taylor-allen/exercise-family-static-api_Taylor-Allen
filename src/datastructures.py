"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member in the self._members list
- get_member: Should return a member from the self._members list
"""

from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        # Initializes the family with a last name
        self.last_name = last_name
        # Sets a starting point for the next unique ID (can increment for each new member)
        self._next_id = 1
        # Example list to hold family members as dictionaries
        self._members = []

    # Generates unique IDs (not currently used because ID is handled directly in add_member)
    # def _generateId(self):
    #     return randint(0, 10)

    def add_member(self, member):
        # Checks if the member dictionary already has an "id" key; if not, it assigns a random ID
        if "id" not in member:
            member["id"] = randint(0, 10)
        # Adds the member (with ID) to the family members list
        self._members.append(member)

    def delete_member(self, id):
        # Filters the list to exclude the member with the specified ID
        # Keeps only members whose "id" does not match the given id
        self._members = list(filter(lambda member: member["id"] != id, self._members))

    def get_member(self, id):
        # Filters the list to find members with the matching ID
        member = list(filter(lambda member: member["id"] == id, self._members))
        # Checks if at least one member with the matching ID was found
        if len(member) > 0:
            # Returns the first (and only) member with the matching ID
            return member[0]
        # Returns None if no matching member was found
        return None

    def get_all_members(self):
        # Returns a list of all family members
        return self._members
