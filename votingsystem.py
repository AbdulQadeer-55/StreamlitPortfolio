class Voter:
    """A class representing a voter in a voting system."""
    def __init__(self, name: str, age: int):
        """Initialize a new Voter object.

        :param name: The name of the voter.
        :param age: The age of the voter.
        """
        self.name = name
        self.age = age

    def is_eligible_to_vote(self) -> bool:
        """Determine if the voter is eligible to vote.

        :return: True if the voter is eligible to vote, False otherwise.
        """
        return self.age >= 18


class VotingSystem:
    """A class representing a voting system."""

    def __init__(self):
        """Initialize a new VotingSystem object."""
        self.voters = []

    def add_voter(self, voter: Voter):
        """Add a voter to the voting system.

        :param voter: The voter to add.
        """
        self.voters.append(voter)

    def get_number_of_eligible_voters(self) -> int:
        """Get the number of eligible voters in the voting system.

        :return: The number of eligible voters.
        """
        return sum(1 for voter in self.voters if voter.is_eligible_to_vote())


if __name__ == "__main__":
    # Create some voters
    voters = [
        Voter("Alice", 25),
        Voter("Bob", 17),
        Voter("Charlie", 22),
        Voter("David", 30),
    ]

    # Create a voting system and add the voters
    voting_system = VotingSystem()
    for voter in voters:
        voting_system.add_voter(voter)

    # Print the number of eligible voters
    print(f"Number of eligible voters: {voting_system.get_number_of_eligible_voters()}")