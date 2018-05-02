"""
Rock Paper Scissors Lizard Spock
"""


class InvalidThrow(Exception):
    pass


class Rules:
    """ Rules for RPSLS """

    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    lizard = "lizard"
    spock = "spock"

    plays = [
        rock,
        paper,
        scissors,
        lizard,
        spock,
    ]

    winning_moves = {
        rock: [scissors, lizard],
        paper: [rock, spock],
        scissors: [paper, lizard],
        lizard: [spock, paper],
        spock: [scissors, rock],
    }

    def __init__(self):
        pass

    @staticmethod
    def valid_throw(play):
        """ Is this play valid? """
        return play in Rules.plays

    @staticmethod
    def beats(this, that):
        """ Does this play beat that play? """
        if not Rules.valid_throw(this) or not Rules.valid_throw(that):
            raise InvalidThrow
        return that in Rules.winning_moves[this]


def main():
    """ Do stuff, totally. """
    pass


if __name__ == '__main__':
    main()
