import string


def parse(file="input.txt"):
    with open(file) as f:
        text = f.read()
    passports_text = text.split("\n\n")
    for pp_text in passports_text:
        pp = {}
        fields = pp_text.split()
        for field in fields:
            field = field.strip()
            k, v = field.split(":")
            k = k.strip()
            v = v.strip()
            pp[k] = v
        yield (pp)


def is_valid(pp):
    return all(
        condition(pp.get(key))
        for key, condition in [
            ("byr", lambda x: x and int(x) in range(1920, 2003)),
            ("iyr", lambda x: x and int(x) in range(2010, 2021)),
            ("eyr", lambda x: x and int(x) in range(2020, 2031)),
            (
                "hgt",
                lambda x: x
                and (
                    (x.endswith("cm") and int("".join(c for c in x if c.isdigit())) in range(150, 194))
                    or (x.endswith("in"))
                    and int("".join(c for c in x if c.isdigit())) in range(59, 77)
                ),
            ),
            (
                "hcl",
                lambda x: x and x.startswith("#") and sum(x.count(char) for char in string.digits + "abcdef") == 6,
            ),
            (
                "ecl",
                lambda x: x and sum(x.count(t) for t in "amb blu brn gry grn hzl oth".split()) == 1,
            ),
            (
                "pid",
                lambda x: x and all((char.isdigit() for char in x)) and len(x) == 9,
            ),
            #    'cid',
        ]
    )


n = 0
for pp in parse():
    if is_valid(pp):
        n += 1
print(n)
