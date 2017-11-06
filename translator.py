from symbol_table import SymbolTable

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
C_OPCODE = "1"
M_REGISTER = "M"
A_REGISTER = "A"
D_REGISTER = "D"
SHIFT_LEFT = "<<"
SHIFT_RIGHT = ">>"


class Translator:

    @staticmethod
    def translate(parser):
        instruction_type = parser.get_type()
        if instruction_type == A_INSTRUCTION_CODE:
            return Translator.__translate_A(parser)
        elif instruction_type == C_INSTRUCTION_CODE:
            return Translator.__translate_C(parser)
        else:
            return EMPTY_TRANSLATION

    @staticmethod
    def __translate_A(parser):
        address = parser.get_address()
        # checks if the address is actually a variable or label and replaces it with its address from the SymbolTable
        if not address.isdigit():
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
        # getting the instruction parts
        jump = parser.get_jump()
        dest = parser.get_dest()
        comp = parser.get_comp()

        # converting the instructions to binary codes
        jump_binary = Translator.__translate_jump(jump)
        comp_binary = Translator.__translate_comp(comp)
        dest_binary = Translator.__translate_dest(dest)
        shift_bit = Translator.__translate_shift(comp)

        return C_OPCODE + shift_bit + BINARY_ONE + comp_binary + dest_binary + jump_binary

    @staticmethod
    def __translate_jump(jump):
        return JUMP_TRANSLATOR[jump]

    @staticmethod
    def __translate_comp(comp):
        a = BINARY_ZERO
        # for M comp instructions: setting a to 1 and replacing M with A for figuring the comp instruction
        if M_REGISTER in comp:
            a = BINARY_ONE
            comp = comp.replace(M_REGISTER, A_REGISTER)

        comp_binary = COMP_TRANSLATOR[comp]

        return a + comp_binary

    @staticmethod
    def __translate_dest(dest):
        d1 = d2 = d3 = BINARY_ZERO
        if A_REGISTER in dest:
            d1 = BINARY_ONE
        if D_REGISTER in dest:
            d2 = BINARY_ONE
        if M_REGISTER in dest:
            d3 = BINARY_ONE

        return d1 + d2 + d3

    @staticmethod
    def __translate_shift(comp):
        if SHIFT_LEFT in comp or SHIFT_RIGHT in comp:
            return BINARY_ZERO

        return BINARY_ONE
