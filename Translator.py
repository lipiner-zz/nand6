#############
# constants #
#############
JUMP_TRANSLATOR = {None: "000", "JGT": "001", "JEQ": "010", "JGE": "011",
                   "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"}
COMP_TRANSLATOR = {"0": "101010", "1": "111111", "-1": "111010", "D": "001100", "A": "110000", "!D": "001101",
                   "!A": "110001", "-D": "001111", "-A": "110011", "D+1": "011111", "A+1": "110111", "D-1": "001110",
                   "A-1": "110010", "D+A": "000010", "D-A": "010011", "A-D": "000111", "D&A": "000000",
                   "D|A": "010101", "D<<": "110000", "D>>": "010000", "A<<": "100000", "A>>": "000000"}
A_INSTRUCTION = 'A'
C_INSTRUCTION = 'C'
EMPTY_TRANSLATION = ""


class Translator:

    def __init__(self):
        pass

    def translate(self, parser):
        instruction_type = parser.get_type
        if instruction_type == A_INSTRUCTION:
            return self.__translate_A(parser)
        elif instruction_type == C_INSTRUCTION:
            return self.__translate_C(parser)
        else:
            return EMPTY_TRANSLATION

    def __translate_A(self, parser):
        pass

    def __translate_C(self, parser):
        pass
