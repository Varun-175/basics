from itertools import product

def truth_table(variables, expressions):
    combinations = product([True, False], repeat=len(variables))
    headers = variables + [f"({expr})" for expr in expressions]
    
    # Print header
    print(" | ".join(headers))
    print("-" * len(" | ".join(headers)))
    
    # Evaluate each row
    for combination in combinations:
        env = dict(zip(variables, combination))
        row = ['T' if env[v] else 'F' for v in variables] + \
              ['T' if eval(expr, {}, env) else 'F' for expr in expressions]
        print(" | ".join(row))

# Get user input
variables = input("Enter the variables separated by spaces (e.g., A B C): ").split()
n = int(input("How many logical expressions do you want to evaluate? "))
expressions = [input(f"Enter logical expression {i+1}: ") for i in range(n)]

# Generate the truth table
truth_table(variables, expressions)
