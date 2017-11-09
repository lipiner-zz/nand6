###########
# imports #
###########
from first_parse import FirstParse

#############
# constants #
#############
FIRST_REGISTER_ALLOCATED = 16


class SymbolTable:
    """
    A class for the symbol table for a single assembler code
    """
    def __init__(self):
        """
        Creates a SymbolTable object and initialize the pre-defined symbols
        """
        self.__labels_dict = {"R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4, "R5": 5, "R6": 6, "R7": 7, "R8": 8,
                              "R9": 9, "R10": 10, "R11": 11, "R12": 12, "R13": 13, "R14": 14, "R15": 15,
                              "SCREEN": 16384, "KBD": 24576, "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4}
        self.__empty_memory_register = FIRST_REGISTER_ALLOCATED

    def set_label(self, parser):
        """
        Sets a new label in the dictionary if there was a label command.
        :param parser: a FirstParser object contains the label
        """
        name = parser.get_label_name()
        if name is not None:
            self.__add_new_label(name, parser.get_line_number())

    def find(self, name):
        """
        Search for the given name in the dictionary. If doesn't exists, sets the label to be in the next empty
        register in the memory
        :param name: a label name to search for
        :return: the register number of the given name
        """
        if name not in self.__labels_dict:
            # the name doesn't exists - adds the name to the dictionary with the next empty register
            self.__add_new_label(name, self.__empty_memory_register)
            # increments the empty memory register
            self.__empty_memory_register += 1
        return self.__labels_dict[name]

    def __add_new_label(self, name, value):
        """
        Adds a new label to the dictionary
        :param name: the label name (the key)
        :param value: the value of the label
        """
        self.__labels_dict[name] = value
