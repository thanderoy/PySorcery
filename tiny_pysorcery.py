"""
This is a very minimal interpreter that can only add numbers and can only
    understand 3 instructions.
    - LOAD_VALUE
    - ADD_TWO_VALUES
    - PRINT_ANSWER

The lexer, parser and compiler are not explored here.

"""


class Interpreter:
    """
    Implement the instructions.
    """
    def __init__(self) -> list:
        self.stack = []

    def LOAD_VALUE(self, value):
        self.stack.append(value)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_value = self.stack.pop()
        second_value = self.stack.pop()
        total = first_value + second_value
        self.stack.append(total)

    def run_code(self, what_to_execute):
        instructions = what_to_execute.get("instructions")
        numbers = what_to_execute.get("numbers")
        for each_step in instructions:
            instruction, argument = each_step
            match instruction:
                case "LOAD_VALUE":
                    number = numbers[argument]
                    self.LOAD_VALUE(number)
                case "ADD_TWO_VALUES":
                    self.ADD_TWO_VALUES()
                case "PRINT_ANSWER":
                    self.PRINT_ANSWER()


what_to_execute = {
    "instructions": [
        ("LOAD_VALUE", 0),
        ("LOAD_VALUE", 1),
        ("ADD_TWO_VALUES", None),
        ("LOAD_VALUE", 2),
        ("ADD_TWO_VALUES", None),
        ("PRINT_ANSWER", None)
    ],
    "numbers": [7, 9, 1]
}

interpreter = Interpreter()
interpreter.run_code(what_to_execute)
