C_COMMAND_TYPE = 'C'
A_COMMAND_TYPE = 'A'
EMPTY_COMMAND_TYPE = 'N'
LABEL_COMMAND_TYPE = 'L'
A_COMMAND_SYMBOL = '@'
EMPTY_COMMAND_SYMBOL = ''
LABEL_COMMAND_SYMBOL = 'L'
COMMENT_SYMBOL = '//'
WHITE_SPACES_CHARS_LIST = [" ", "\t"]
TYPES_DICT = {A_COMMAND_SYMBOL: A_COMMAND_TYPE, LABEL_COMMAND_SYMBOL: LABEL_COMMAND_TYPE,
              EMPTY_COMMAND_SYMBOL: EMPTY_COMMAND_TYPE}


class Parser:
    def __init__(self, command):
        """

        :param command:
        """
        self.command_type = None
        self.command = command

    def clear(self):
        """
        Reformat the command - removes comments and any white spaces
        """
        comment_pos = self.command.find(COMMENT_SYMBOL)  # search for a comments chars "//"
        if comment_pos >= 0:
            self.command = self.command[:comment_pos]  # removes any comment if there is any
        for note in WHITE_SPACES_CHARS_LIST:
            self.command.replace(note, "")  # removes any white spaces

    def set_type(self):
        """
        Sets the type of the command: A-instruction / C-instruction / empty line / label
        """
        if self.command[0] not in TYPES_DICT:  # search for special symbol. If there aren't any then it is C-instruction
            self.command_type = C_COMMAND_TYPE
        else:  # set the type based on the symbol
            self.command_type = TYPES_DICT[self.command[0]]

