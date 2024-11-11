from flask import Flask, jsonify
from flask_cors import CORS
import random
import operator

app = Flask(__name__)
CORS(app, supports_credentials=True)  


def generate_numbers():
    return [random.randint(1, 10) for _ in range(4)]


def random_operation():
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    return random.choice(list(operations.items()))


def calculate(numbers):
    result = numbers[0]
    equation = str(numbers[0])

    for number in numbers[1:]:
        op_symbol, op_func = random_operation()
        try:
            result = op_func(result, number)
            equation += f" {op_symbol} {number}"
        except ZeroDivisionError:
            continue

    return equation, result


@app.route('/calculate', methods=['GET', 'OPTIONS'])
def calculate_api():
    if request.method == 'OPTIONS':
       
        response = jsonify({'message': 'CORS preflight'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    
    numbers = generate_numbers()
    equation, result = calculate(numbers)
    return jsonify({
        "numbers": numbers,
        "equation": equation,
        "result": result
    })

if __name__ == '__main__':
    app.run(debug=True)
