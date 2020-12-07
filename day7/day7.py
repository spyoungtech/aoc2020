import re

parse_contents = r'(\d+) (.*?)(,|\.)'
rules = {}

class Rule:
    def __init__(self, line):
        self.line = line
        b, contains = line.split('contain')
        self.color, _ = b.split(' bags', 1)
        self.contains_shiny_gold = 'shiny gold' in contains
        self.contains = contains

    def __contains__(self, item):
        return item in self.contains

    def __len__(self):
        if 'no other bags' in self.contains:
            return 0
        total = 0
        for num, rule in self.contents:
            total += num + num * len(rule)
        return total

    @property
    def contents(self):
        r = []
        for num, color, _ in re.findall(parse_contents, self.contains):
            color = color.replace(' bags', '').replace(' bag', '').strip()
            r.append((int(num), rules[color]))
        return r

def parse(file="input.txt"):
    with open(file) as f:
        return [line.strip() for line in f if line.strip()]


for line in parse():
    r = Rule(line)
    rules[r.color] = r

can_contain_gold = {}

for color, rule in rules.items():
    if rule.contains_shiny_gold:
        can_contain_gold[rule.color] = rule

while True:
    new_found = False
    to_add = {}
    for color, rule in rules.items():
        if color in can_contain_gold:
            continue
        for c in can_contain_gold:
            if c in rule:
                to_add[color] = rule
                new_found = True
    can_contain_gold.update(to_add)
    if not new_found:
        break

print(len(can_contain_gold))
golden_rule = rules['shiny gold']
print(len(golden_rule))