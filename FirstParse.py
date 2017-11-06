from Parser import Parser
from Parser import C_COMMAND_TYPE, A_COMMAND_TYPE, EMPTY_COMMAND_TYPE, LABEL_COMMAND_TYPE


class FirstParse (Parser):
    """
    A Parser object to parse the command to its parts in the first parse phase.
    """
    __line_number = 0  # initialize the line number to 0

    def __init__(self, command):
        """
        Initializes the Parser object with the command
        :param command: the command to parse
        """
        Parser.__init__(self, command)

    def get_label_name(self):
        """
        Incrementer the line number (iff the command doesn't empty) and returns the label name iff the command
        is a label
        :return: the label name if the command is a label
        """
        command_type = self.get_type()
        if command_type == LABEL_COMMAND_TYPE:
            return self.command[1:-1]  # ignores the () at the beginning and the end
        if command_type != EMPTY_COMMAND_TYPE:
            FirstParse.__line_number += 1

    @staticmethod
    def get_line_number():
        """
        :return: the current line number
        """
        return FirstParse.__line_number
