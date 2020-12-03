from typing import Tuple
class Policy:
    def __init__(self, minimum: int, maximum: int, alpha: str):
        self.range = range(minimum, maximum+1)
        self.alpha = alpha

    def validate(self, password: str) -> bool:
        if password.count(self.alpha) in self.range:
            return True
        return False


def parse_line(line: str) -> Tuple[Policy, str]:
    line = line.strip()
    policy_part, password = line.split(': ')
    quantifier, alpha = policy_part.split()
    min_quantity, max_quantity = quantifier.split('-')
    policy = Policy(int(min_quantity), int(max_quantity), alpha)
    return policy, password

def parse_input(fp='input.txt'):
    with open(fp) as input_file:
        return [parse_line(line) for line in input_file if line.strip()]


def main(fp='input.txt'):
    valid_count = 0
    for policy, password in parse_input(fp):
        if policy.validate(password):
            valid_count += 1
    return valid_count

if __name__ == '__main__':
    print(main())