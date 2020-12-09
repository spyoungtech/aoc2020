from day8 import Instruction, get_input_lines, run


def main():
    instructions = [Instruction.from_line(index, line) for index, line in enumerate(get_input_lines())]
    candidates = [inst.index for inst in instructions if inst.action in ('jmp', 'nop')]
    for cand in candidates:
        insts = [inst.copy() for inst in instructions]
        to_change = insts[cand]
        if to_change.action == 'jmp':
            to_change.action = 'nop'
        else:
            to_change.action = 'jmp'
        try:
            return run(insts)
        except RuntimeError:
            continue
        # with open(f'input{cand}.txt', 'w') as f:
        #     for inst in insts:
        #         f.write(f'{inst.action} {inst.number}\n')


if __name__ == '__main__':
    print(main())