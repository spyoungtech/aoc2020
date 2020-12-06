import string
def parse(file="input.txt"):
    with open(file) as f:
        text = f.read()
    groups = text.split("\n\n")
    return groups

def parse_group(group_text):
    # letters = set(''.join(c for c in group_text.strip() if c in string.ascii_letters))
    # return len(letters)
    people = {}
    for person_id, line in enumerate(group_text.strip().split('\n')):
        person = line.strip()
        yes = ''.join(c for c in person.strip() if c in string.ascii_letters)
        people[person_id] = set(yes)
    sets = list(people.values())
    s = set.intersection(*sets)
    return len(s)

total = 0
for group in parse():
    num = parse_group(group)
    total += num

print(total)