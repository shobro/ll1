from pprint import pprint


def classify_terminal(ch):
    if (
        ch == "("
        or ch == ")"
        or ch == "+"
        or ch == "-"
        or ch == "/"
        or ch == "*"
        or ch == "$"
    ):
        return ch

    for c in ch:
        if c.isalpha():
            return "i"

    return "n"


def reverse(x):
    if x == None:
        return None
    return x[::-1]


def parsing(rules, parsing_tables):
    f = open("output.txt", "r")
    lines = f.readlines()
    input_stack = []
    for line in lines:
        input_stack.append(line)

    non_terminals = set()
    for nt in rules.keys():
        non_terminals.add(nt)

    terminals = set()
    for nt in rules.keys():
        for r in rules[nt]:
            if r == None:
                # terminals.add("$")
                continue
            for ch in r:
                if ch not in non_terminals:
                    terminals.add(ch)

    grammar_stack = []
    grammar_stack.append("E")
    input_stack.append("$\n")
    for i in input_stack:
        i = i[: len(i) - 1]
        t = classify_terminal(i)
        while True:
            g = grammar_stack.pop()
            if g not in rules.keys() or len(parsing_tables[g][t]) == 0:
                print("not parsed with ", g, " and ", grammar_stack, " in stack")
                return
            for g_rules in parsing_tables[g][t]:
                g_rules = reverse(g_rules)
                # print(g_rules)
                if g_rules != None:
                    for rule in g_rules:
                        if rule == None:
                            break
                        grammar_stack.append(rule)
            if len(grammar_stack) > 0 and grammar_stack[-1] == t:
                print(grammar_stack.pop())
                break
            if len(grammar_stack) == 0:
                break
        if i == "$" and len(grammar_stack) == 0:
            print("successfully parsed")
