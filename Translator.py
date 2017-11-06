from SymbolTable import SymbolTable

#############
# constants #
#############
JUMP_TRANSLATOR = {"": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
                   "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"}
COMP_TRANSLATOR = {"0": "101010", "1": "111111", "-1": "111010", "D": "001100", "A": "110000", "!D": "001101",
                   "!A": "110001", "-D": "001111", "-A": "110011", "D+1": "011111", "A+1": "110111", "D-1": "001110",
                   "A-1": "110010", "D+A": "000010", "D-A": "010011", "A-D": "000111", "D&A": "000000",
                   "D|A": "010101", "D<<": "110000", "D>>": "010000", "A<<": "100000", "A>>": "000000"}
A_INSTRUCTION_CODE = 'A'
C_INSTRUCTION_CODE = 'C'
EMPTY_TRANSLATION = ""
BINARY_CODE = "{0:b}"
ADDRESS_LENGTH = 15
BINARY_ZERO = "0"
BINARY_ONE = "1"
A_OPCODE = "0"
M_REGIATER = "M"
A_REGIATER = "A"
D_REGIATER = "D"


class Translator:

    @staticmethod
    def translate(parser):
        instruction_type = parser.get_type
        if instruction_type == A_INSTRUCTION_CODE:
            return Translator.__translate_A(parser)
        elif instruction_type == C_INSTRUCTION_CODE:
            return Translator.__translate_C(parser)
        else:
            return EMPTY_TRANSLATION

    @staticmethod
    def __translate_A(parser):
        address = parser.get_address
        # checks if the address is actually a variable or label and replaces it with its address from the SymbolTable
        if address.isalpha():
            address = SymbolTable.find(address)
        # if the address contains only numbers- converting it to int
        else:
            address = int(address)

        # finding the binary representation of the address
        binary_repr = BINARY_CODE.format(address)
        # making sure the binary representation is 15 bits long
        binary_repr = (ADDRESS_LENGTH - len(binary_repr))*BINARY_ZERO + binary_repr

        return A_OPCODE + binary_repr

    @staticmethod
    def __translate_C(parser):
        jump = parser.get_jump
        dest = parser.get_dest
        comp = parser.get_comp
        a = BINARY_ZERO

        # converting the instructions to binary codes
        jump_binary = JUMP_TRANSLATOR[jump]
        if M_REGIATER in comp:
            a = BINARY_ONE
            #comp = comp.

        comp_binary = COMP_TRANSLATOR[comp]

