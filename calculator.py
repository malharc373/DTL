# calculator.py

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    elif operator == '^':
        return a ** b
    else:
        return "Invalid operator"

if __name__ == "__main__":
    try:
        a = float(input("Enter the first number: "))
        operator = input("Enter operator (+, -, *, /, ^): ")
        b = float(input("Enter the second number: "))
        result = calculate(a, b, operator)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
# Added ^ operator
