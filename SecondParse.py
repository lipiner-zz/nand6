from Parser import Parser


class SecondParse (Parser):
    """
    A Parser object to parse the command to its parts in the second parse phase.
    """
    def __init__(self, command):
        """
        Initializes the Parser object with the command.
        :param command: the command to parse
        """
        Parser.__init__(self, command)
        self.__dest = None
        self.__comp = None
        self.__jump = None

    def parse(self):
        pass

    def get_address(self):
        pass

    def get_dest(self):
        pass

    def get_comp(self):
        pass

    def get_jump(self):
        pass
