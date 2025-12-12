name = ["deepsa", "sahu", "varenyam", "byom"]


def upper_case(string):
    return string.upper()
#s = upper_case("lipsa")
#print(s)


upper_names = list(map(upper_case, name))
print(upper_names)