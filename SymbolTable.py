from FirstParse import FirstParse

FIRST_REGISTER_ALLOCATED = 16


class SymbolTable:
    labels_dict = {}
    empty_memory_register = FIRST_REGISTER_ALLOCATED

    @staticmethod
    def set_label(parser):
        """
        Sets a new label in the dictionary if there was a label command.
        :param parser: a FirstParser object contains the label
        """
        name = parser.get_label_name
        if name is not None:
            SymbolTable.__add_new_label(name, parser.get_line_number)

    @staticmethod
    def find(name):
        """
        Search for the given name in the dictionary. If doesn't exists, sets the label to be in the next empty
        register in the memory
        :param name: a label name to search for
        :return: the register number of the given name
        """
        if name not in SymbolTable.labels_dict:
            # the name doesn't exists - adds the name to the dictionary with the next empty register
            SymbolTable.__add_new_label(name, SymbolTable.empty_memory_register)
            # increments the empty memory register
            SymbolTable.empty_memory_register += 1
        return SymbolTable.labels_dict[name]

    @staticmethod
    def __add_new_label(name, value):
        """
        Adds a new label to the dictionary
        :param name: the label name (the key)
        :param value: the value of the label
        """
        SymbolTable.labels_dict[name] = value
