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
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]


    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id
    
    def add_member(self, member):
        ## You have to implement this method
        ## Append the member to the list of _members
        if 'id' not in member:
            # if they arent, generate id for this member
            member.update(
                id=self._generate_id()
            )
        # append the member to the members list
        self._members.append(member)
        return member 

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

