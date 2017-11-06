import sys
import os
from first_parse import FirstParse
from second_parse import SecondParse
from symbol_table import SymbolTable
from translator import Translator

#############
# constants #
#############
PATH_POS = 1
ASM_SUFFIX_LENGTH = 3
HACK_SUFFIX = "hack"
ASM_SUFFIX = "asm"
WRITING_MODE = "w"
LINE_BREAK = "\n"


def assemble_file(file_name):
    with open(file_name) as input_file:
        output_file_name = file_name.replace(ASM_SUFFIX, HACK_SUFFIX)
        with open(output_file_name, WRITING_MODE) as output_file:
            # first parse of the file
            for line in input_file:
                first_parser = FirstParse(line)
                SymbolTable.set_label(first_parser)
            # second parse of the file
            input_file.seek(0)
            for line in input_file:
                second_parser = SecondParse(line)
                binary_line = Translator.translate(second_parser)
                if binary_line:
                    output_file.write(binary_line + LINE_BREAK)


def assemble_directory(directory_name):
    files_list = os.listdir(directory_name)  # list of all the files' name in the subject directory
    for directory_file in files_list:
        if ASM_SUFFIX in directory_file:
            asm_file = os.path.join(directory_name, directory_file)
            assemble_file(asm_file)

if __name__ == '__main__':
    path = sys.argv[PATH_POS]
    if os.path.isdir(path):
        assemble_directory(path)
    else:
        assemble_file(path)
