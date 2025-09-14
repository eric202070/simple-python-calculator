def calc(x, y, operation):
    operations = ['+', '-', '*', '/']
    if operation not in operations:
        return "Please, enter a valid expression like: 2 + 2, using +, -, *, /"
    try:
        if operation == '+':
            return x + y
        elif operation == '-':
            return x - y
        elif operation == '*':
            return x * y
        elif operation == '/':
            if y == 0:
                return "Division by 0 is not allowed."
            return x / y
    except Exception as e:
        return str(e)
   
def main():
    print("Small Calculator 1.0") 
    print("To quit, type 'exit'")
    while True:
        user_input = input("Gimme an simple expression, like 2 + 2:")
        if (user_input.lower() == 'exit'):
            print("Goodbye!")
            break
        try:
            x, operation, y = list(user_input.replace(" ", ""))
            print(x, operation, y)
            x = float(x)
            y = float(y)
            result = calc(x,y,operation)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter a valid SIMPLE expression like: 2 + 2")
if __name__ == "__main__":
    main()