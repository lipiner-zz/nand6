from FirstParse import FirstParse

class SymbolTable:
    labels_dict = {}

    @staticmethod
    def set_label(parser):
        name = parser.get_label_name
        if name is not None:
            SymbolTable.labels_dict[name] = line_number

    @staticmethod
    def find(name):
        pass
