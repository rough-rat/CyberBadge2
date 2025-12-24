import re
import sys
# "D[0-9]+_[0-9]+"
# $11$2$3

regex = r"\(at ([0-9]+[.][0-9]+) ([0-9]+[.][0-9]+)\)\n.+D([0-9]+)_([0-9]+)."
scale_factor = 2.5


def scale_numbers(match):
    x = float(match.group(3)) * scale_factor
    y = float(match.group(4)) * scale_factor
    d1 = match.group(3)
    d2 = match.group(4)
    return f"(at {x:.1f} {y:.1f})\n(property \"Reference\" \"D{d1}_{d2}\""


with open(sys.argv[1], "r") as file:
    data = file.read()

data = re.sub(regex, scale_numbers, data)

for match in re.finditer(regex, data):
    print(match.group(1), match.group(2), match.group(3), match.group(4))

with open(sys.argv[1], "w") as file:
    file.write(data)

with open(sys.argv[1] + ".bak", "w") as file:
    file.write(data)



