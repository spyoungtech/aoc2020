from typing import Tuple, Type, List


class Policy:
    def __init__(self, minimum: int, maximum: int, alpha: str):
        self.range = range(minimum, maximum+1)
        self.alpha = alpha

    def validate(self, password: str) -> bool:
        if password.count(self.alpha) in self.range:
            return True
        return False


class PositionalPolicy(Policy):
    def validate(self, password: str) -> bool:
        index_positions = (self.range.start-1, self.range.stop-2)
        try:
            index_values = ''.join(password[index] for index in index_positions)
        except IndexError:
            return False
        if index_values.count(self.alpha) != 1:
            return False
        else:
            return True


def parse_line(line: str, policy_type: Type[Policy]) -> Tuple[Policy, str]:
    line = line.strip()
    policy_part, password = line.split(': ')
    quantifier, alpha = policy_part.split()
    min_quantity, max_quantity = quantifier.split('-')
    policy = policy_type(int(min_quantity), int(max_quantity), alpha)
    return policy, password


def parse_input(fp='input.txt', policy_type: Type[Policy] = Policy) -> List[Tuple[Policy, str]]:
    with open(fp) as input_file:
        return [parse_line(line, policy_type=policy_type) for line in input_file if line.strip()]


def main(fp='input.txt', policy_type: Type[Policy] = Policy) -> int:
    valid_count = 0
    for policy, password in parse_input(fp, policy_type=policy_type):
        if policy.validate(password):
            valid_count += 1
    return valid_count


if __name__ == '__main__':
    print(main())  # part 1
    print(main(policy_type=PositionalPolicy))  # part 2
