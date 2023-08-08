from flask import Flask, render_template, request

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            operator = request.form['operator']
            num2 = float(request.form['num2'])

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                return "Invalid operator"

            return render_template('index.html', result=result, num1=num1, num2=num2, operator=operator)

        except ValueError:
            return "Invalid input. Please enter valid numbers."

    return render_template('index.html', result=None, num1=None, num2=None, operator=None)

if __name__ == '__main__':
    app.run(debug=True)

