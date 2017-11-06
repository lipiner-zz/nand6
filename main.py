from first_parse import FirstParse
from second_parse import SecondParse

if __name__ == '__main__':
    parser = FirstParse("(LOOP)")
    print(parser.get_label_name())
    parser = FirstParse("//(LOOP)")
    print(parser.get_label_name())
    print(parser.get_line_number())
    parser = FirstParse("@wer")
    print(parser.get_label_name())
    parser = FirstParse("D = A")
    print(parser.get_label_name())
    parser = FirstParse("(LOOP) // sdad")
    print(parser.get_label_name())
    print(parser.get_line_number())
    print(FirstParse.get_line_number())

    parser = SecondParse("D = A")
    print(parser.get_dest(), parser.get_comp(), parser.get_jump())
    parser = SecondParse("D = M;JPE")
    print(parser.get_dest(), parser.get_comp(), parser.get_jump())
    parser = SecondParse("0;JEQ")
    print(parser.get_dest(), parser.get_comp(), parser.get_jump())

