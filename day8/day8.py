from ast import literal_eval
def get_input_lines(file="input.txt"):
    with open(file) as f:
        return [line.strip() for line in f if line.strip()]

accum = 0
has_run = set()


class Instruction:
    def __init__(self, index, action, number):
        self.action = action
        self.number = number
        self.index = index

    @classmethod
    def from_line(cls, index, line):
        action, number = line.strip().split()
        number = literal_eval(number)
        return cls(index, action, number)

    def __repr__(self):
        return f'Instruction({self.index}, {self.action}, {self.number})'

    def run(self):
        global accum
        if self.action == 'acc':
            accum += self.number
            return self.index + 1
        elif self.action == 'jmp':
            new_index = self.index + self.number
            return new_index
        elif self.action == 'nop':
            return self.index + 1
        else:
            raise RuntimeError(f"Unknown operation {self.action}")

    def has_run(self):
        return self in has_run

    def __hash__(self):
        return hash((self.action, self.number))

    def copy(self):
        return Instruction(self.index, self.action, self.number)

# instructions = {}
# for index, line in enumerate(get_input_lines()):
#     inst = Instruction.from_line(index, line)
#     instructions[inst.index] = inst
#
#
# for instruction in instructions.values():
#     instruction.run()



from collections import Counter
run_counter = Counter()
def run(instructions):
    global accum
    global has_run
    accum = 0
    next_instruction = 0
    has_run = set()

    while True:
        try:
            inst = instructions[next_instruction]
        except IndexError:
            return accum
        if inst.has_run():
            raise RuntimeError("Duplicated instruction")
        next_instruction = inst.run()
        has_run.add(inst)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('input', default='input.txt')
    args = parser.parse_args()
    instructions = [Instruction.from_line(index, line) for index, line in enumerate(get_input_lines(args.input))]
