from collections import namedtuple, defaultdict

# Define the symbols
Symbol = namedtuple("Symbol", ["type", "name"])
SymbolType = {"TERMINAL": "TERMINAL", "NON_TERMINAL": "NON_TERMINAL"}

# Define a production rule
Production = namedtuple("Production", ["left", "right"])

# Define the grammar
grammar = [
    Production(Symbol(SymbolType["NON_TERMINAL"], "E"), [Symbol(SymbolType["NON_TERMINAL"], "E"), Symbol(SymbolType["TERMINAL"], "+"), Symbol(SymbolType["NON_TERMINAL"], "T")]),
    Production(Symbol(SymbolType["NON_TERMINAL"], "E"), [Symbol(SymbolType["NON_TERMINAL"], "T")]),
    Production(Symbol(SymbolType["NON_TERMINAL"], "T"), [Symbol(SymbolType["NON_TERMINAL"], "T"), Symbol(SymbolType["TERMINAL"], "*"), Symbol(SymbolType["NON_TERMINAL"], "F")]),
    Production(Symbol(SymbolType["NON_TERMINAL"], "T"), [Symbol(SymbolType["NON_TERMINAL"], "F")]),
    Production(Symbol(SymbolType["NON_TERMINAL"], "F"), [Symbol(SymbolType["TERMINAL"], "("), Symbol(SymbolType["NON_TERMINAL"], "E"), Symbol(SymbolType["TERMINAL"], ")")]),
    Production(Symbol(SymbolType["NON_TERMINAL"], "F"), [Symbol(SymbolType["TERMINAL"], "id")])
]

# Define the start symbol
start_symbol = Symbol(SymbolType["NON_TERMINAL"], "E")

# Build the LR(0) item sets
def closure(item_set):
    result = list(item_set)
    while True:
        new_items = []
        for item in result:
            dot_index = item.right.index(Symbol(SymbolType["TERMINAL"], "."))

            if dot_index < len(item.right) - 1:
                next_symbol = item.right[dot_index + 1]
                if next_symbol.type == SymbolType["NON_TERMINAL"]:
                    for prod in grammar:
                        if prod.left == next_symbol:
                            new_item = Production(prod.left, [Symbol(SymbolType["TERMINAL"], ".")] + prod.right)
                            if new_item not in result and new_item not in new_items:
                                new_items.append(new_item)
        if not new_items:
            break
        result.extend(new_items)
    return result

def goto(item_set, symbol):
    new_set = []
    for item in item_set:
        dot_index = item.right.index(Symbol(SymbolType["TERMINAL"], "."))
        if dot_index < len(item.right) - 1 and item.right[dot_index + 1] == symbol:
            new_item = Production(item.left, item.right[:dot_index] + [symbol] + [Symbol(SymbolType["TERMINAL"], ".")] + item.right[dot_index + 2:])
            new_set.append(new_item)
    return closure(new_set)

# Build the canonical collection of LR(0) item sets
canonical_collection = []
state_to_items = {}

initial_item_set = closure([Production(start_symbol, [Symbol(SymbolType["TERMINAL"], "."), start_symbol])])
state_to_items[0] = initial_item_set
canonical_collection.append(initial_item_set)

current_state = 0
while current_state < len(canonical_collection):
    current_item_set = canonical_collection[current_state]

    for symbol in (Symbol(SymbolType["NON_TERMINAL"], "E"), Symbol(SymbolType["TERMINAL"], "+"), Symbol(SymbolType["TERMINAL"], "*"), Symbol(SymbolType["TERMINAL"], "("), Symbol(SymbolType["TERMINAL"], ")"), Symbol(SymbolType["TERMINAL"], "id")):
        new_item_set = goto(current_item_set, symbol)
        if new_item_set and new_item_set not in canonical_collection:
            canonical_collection.append(new_item_set)
            state_to_items[len(canonical_collection) - 1] = new_item_set

    current_state += 1

# Build the action and goto tables
action_table = [{} for _ in range(len(canonical_collection))]
goto_table = [{} for _ in range(len(canonical_collection))]

for state, item_set in enumerate(canonical_collection):
    for item in item_set:
        if item.right[-1] == Symbol(SymbolType["TERMINAL"], "."):
            if item.left == start_symbol:
                action_table[state][Symbol(SymbolType["TERMINAL"], "$")] = "Accept"
            else:
                prod_index = grammar.index(item.left)
                for symbol in (Symbol(SymbolType["TERMINAL"], "+"), Symbol(SymbolType["TERMINAL"], "*")):
                    action_table[state][symbol] = f"Reduce {prod_index}"

    for symbol in (Symbol(SymbolType["NON_TERMINAL"], "E"), Symbol(SymbolType["NON_TERMINAL"], "T"), Symbol(SymbolType["NON_TERMINAL"], "F")):
        next_state = goto_table[state].get(symbol)
        if next_state is not None:
            goto_table[state][symbol] = next_state

# Parse input using the CLR parser
def parse_input(input_str):
    state_stack = [0]
    symbol_stack = []
    input_index = 0

    while True:
        current_state = state_stack[-1]

        if action_table[current_state].get(Symbol(SymbolType["TERMINAL"], input_str[input_index])):
            action = action_table[current_state][Symbol(SymbolType["TERMINAL"], input_str[input_index])]

            if action.startswith("Shift"):
                next_state = int(action.split()[1])
                state_stack.append(next_state)
                symbol_stack.append(Symbol(SymbolType["TERMINAL"], input_str[input_index]))
                input_index += 1
            elif action.startswith("Reduce"):
                prod_index = int(action.split()[1])
                prod = grammar[prod_index]
                num_to_pop = len(prod.right)
                state_stack = state_stack[:-num_to_pop]
                symbol_stack = symbol_stack[:-num_to_pop]
                current_state = state_stack[-1]
                symbol_stack.append(prod.left)
                state_stack.append(goto_table[current_state][prod.left])
            elif action == "Accept":
                return True
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    input_str = input("Enter an expression: ")
    success = parse_input(input_str)
    if success:
        print("Parsing successful!") 
        
        
    else:
        print("Parsing failed!")
