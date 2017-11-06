from Parser import Parser
from Parser import C_COMMAND_TYPE, A_COMMAND_TYPE, EMPTY_COMMAND_TYPE, LABEL_COMMAND_TYPE


class FirstParse (Parser):
    """
    A Parser object to parse the command to its parts in the first parse phase.
    """

    def __init__(self, command):
        """
        Creates a new FirstParse object.
        """
        Parser.__init__(self)
        self.__line_number = 0  # initialize the line number to 0

    def get_label_name(self):
        """
        Increments the line number (iff the command doesn't empty) and returns the label name iff the command
        is a label
        :return: the label name if the command is a label
        """
        command_type = self.get_type()
        if command_type == LABEL_COMMAND_TYPE:
            return self.command[1:-1]  # ignores the () at the beginning and the end
        if command_type != EMPTY_COMMAND_TYPE:  # increments the line number if it is not a blank line or a label
            self.__line_number += 1

    def get_line_number(self):
        """
        :return: the current line number
        """
        return self.__line_number
