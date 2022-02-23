from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


"""PART ONE"""

@app.route('/add')
def do_add():
    """Add parameters a + b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)


@app.route('/sub')
def do_sub():
    """Subtract parameters a - b"""
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)

    return str(result)


@app.route('/mult')
def do_mult():
    """Multiply parameters a * b"""
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)


@app.route('/div')
def do_div():
    """Divide parameters a / b"""
    
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)


"""PART TWO"""

math = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<oper>")
def do_math(oper):
    """Perform math operation on a and b parameters"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = math[oper](a,b)

    return str(result)