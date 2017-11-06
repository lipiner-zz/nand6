C_COMMAND_TYPE = 'C'
A_COMMAND_TYPE = 'A'
EMPTY_COMMAND_TYPE = 'N'
LABEL_COMMAND_TYPE = 'L'
A_COMMAND_SYMBOL = '@'
EMPTY_COMMAND_SYMBOL = ''
LABEL_COMMAND_SYMBOL = '('
COMMENT_SYMBOL = '//'
WHITE_SPACES_CHARS_LIST = [" ", "\t"]
# TYPES_DICT = {A_COMMAND_SYMBOL: A_COMMAND_TYPE, LABEL_COMMAND_SYMBOL: LABEL_COMMAND_TYPE,
#               EMPTY_COMMAND_SYMBOL: EMPTY_COMMAND_TYPE}


class Parser:
    """
    A Parser object to parse the command to its parts.
    """
    def __init__(self, command):
        """
        Creates new object with the given command. Clears the command from comments and extra white spaces and
        set the type
        :param command: the command to parse
        """
        self.command = command
        self.__clear()
        self.__command_type = self.__set_type()

    def __clear(self):
        """
        Reformat the command - removes comments and any white spaces
        """
        comment_pos = self.command.find(COMMENT_SYMBOL)  # search for a comments chars "//"
        if comment_pos >= 0:
            self.command = self.command[:comment_pos]  # removes any comment if there is any
        for note in WHITE_SPACES_CHARS_LIST:
            self.command = self.command.replace(note, "")  # removes any white spaces

    def __set_type(self):
        """
        Sets the type of the command: A-instruction / C-instruction / empty line / label
        """
        if len(self.command) == 0:  # an empty command
            return EMPTY_COMMAND_TYPE
        # search for special symbol. If there aren't any then it is C-instruction
        if self.command[0] == A_COMMAND_SYMBOL:
            return A_COMMAND_TYPE
        if self.command[0] == LABEL_COMMAND_SYMBOL:
            return LABEL_COMMAND_TYPE
        return C_COMMAND_TYPE

    def get_type(self):
        """
        :return: the command type: A for A-instruction, C for C-instruction, N for empty line, and L for label
        """
        return self.__command_type
