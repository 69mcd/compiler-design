def calculate_first(grammar):
    first = {}

    def first_of(symbol):
        if symbol in first:
            return first[symbol]
        elif symbol in grammar:
            first[symbol] = set()
            for production in grammar[symbol]:
                if production[0] in grammar:
                    first[symbol] |= first_of(production[0])
                else:
                    first[symbol].add(production[0])
            return first[symbol]
        else:
            return {symbol}

    for non_terminal in grammar:
        first[non_terminal] = first_of(non_terminal)

    return first


def calculate_follow(grammar, first):
    follow = {non_terminal: set() for non_terminal in grammar}
    follow[next(iter(grammar))].add('$')

    while True:
        before = {non_terminal: set(follow[non_terminal]) for non_terminal in grammar}
        for non_terminal, productions in grammar.items():
            for production in productions:
                for i, symbol in enumerate(production):
                    if symbol in grammar:
                        if i + 1 < len(production):
                            follow[symbol] |= (first[production[i + 1]] - {'ε'})
                            if 'ε' in first[production[i + 1]]:
                                follow[symbol] |= follow[non_terminal]
                        else:
                            follow[symbol] |= follow[non_terminal]
        if before == follow:
            break

    return follow


grammar = {
    "S": [["A", "B"], ["B"]],
    "A": [["a", "A"], ["a"]],
    "B": [["b", "B"], ["b"]]
}

first_sets = calculate_first(grammar)
for non_terminal, first_set in first_sets.items():
    print(f"first({non_terminal}) = {first_set}")

follow_sets = calculate_follow(grammar, first_sets)
for non_terminal, follow_set in follow_sets.items():
    print(f"follow({non_terminal}) = {follow_set}")
