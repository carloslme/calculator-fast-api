from enum import Enum
from fastapi import FastAPI, Body, Path, Query, HTTPException, status
from .calculator import calculator as calc


class CalculatorFormat(str, Enum):
    SHORT = "digital"
    FULL = "analogic"


app = FastAPI()

"""
PARAMETER VALUES
Values are required after de endpoint.
"""


@app.get("/sum/{v1}/{v2}")
async def sum(v1: int, v2: int):
    result = int(calc.sum(v1, v2))
    print(f"'resultado': {result}")
    print(f"'resultado': {result}")
    return {"resultado": result}


"""
In a REST API, query parameters are commonly used on read endpoints 
to apply pagination, a filter, a sorting order, or selecting fields.
"""


@app.get("/subtract/")
async def subtract(v1: float = 1.0, v2: float = 2.0):
    result = int(calc.subtract(v1, v2))
    print(f"'resultado': {result}")
    print(f"'resultado': {result}")
    return {"resultado": result}


@app.get("/divide/{v1}/{v2}")
async def divide(v1: float, v2: float):
    if v2 == 0 or v1 == 0:
        print("resultado: cannot divide with 0")
        print("'resultado': 'cannot divide with 0'")
        return {"resultado": "can't divide with 0"}

    result = int(calc.divide(v1, v2))
    print(f"'resultado': {result}")
    print(f"'resultado': {result}")
    return {"resultado": result}


@app.get("/divide/{v1}/{v2}")
async def divide(v1: float, v2: float):
    if v2 == 0 or v1 == 0:
        print("resultado: cannot divide with 0")
        print("'resultado': 'cannot divide with 0'")
        return {"resultado": "can't divide with 0"}

    result = int(calc.divide(v1, v2))
    print(f"'resultado': {result}")
    print(f"'resultado': {result}")
    return {"resultado": result}


"""
Query is a class from the fastapi library. 
It's used to validate query parameters in an API call. 
It takes two arguments, default value and validation rules. 
In this case we're using gt for greater than and le for less 
than or equal to. The Query class can be used with any type 
of variable including int, str, float etc...
"""


@app.get("/divide-format")
async def divide_format(
    format: CalculatorFormat,
    v1: float = Query(1.0, gt=1.0),
    v2: float = Query(1.0, gt=1.0),
):
    if v2 == 0 or v1 == 0:
        print("resultado: cannot divide with 0")
        print("'resultado': 'cannot divide with 0'")
        return {"resultado": "can't divide with 0"}

    result = int(calc.divide(v1, v2))
    print(f"'resultado': {result}")
    print(f"'resultado': {result}")
    return {"format": format, "resultado": result}


"""
BODY REQUEST
Body is a function that takes in an argument. 
The argument can be anything, but it's usually used 
to take in data from the body of a HTTP request. 
The Body function returns whatever was passed into 
it as its first parameter. In this case, we're passing 
in ... which means that name is required and will throw 
an error if not provided when calling create_user().
"""


@app.post("/multiply-parameters")
async def multiply(text: str = Body(...)):  # (...) means that the argument is required
    try:
        values = text.split("*")
        v1 = int(values[0])
        v2 = int(values[1])

        print(type(v1), type(v2))
        if isinstance(v1, int) and isinstance(v2, int):
            result = int(calc.multiply(v1, v2))
            print(f"'resultado': {result}")
            print(f"'resultado': {result}")
            return {"resultado": result}

    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "resultado: invalid multiplication string.",
                "hints": [
                    "Check the numbers",
                    "Must be 'int*int', example 1*1",
                ],
            },
        ) from e


"""
PATH PARAMETERS
Path is a class that validates the input of an endpoint. 
It's part of fastapi and it has several parameters:

ge (greater than or equal to)
gt (greater than)
lt (less than)
le (less than or equal to). 

These are used for numbers, but there are also other parameters like 
min_lenght and max_length which can be used with strings. 
There's also regex parameter which 
takes in regular expressions as arguments. This allows you to validate 
inputs based on patterns such as email addresses, phone numbers etc...
"""


@app.get("/multiply-regex/{text}")
async def multiply_regex(text: str = Path(..., regex=r"[0-9]\*[0-9]")):
    values = text.split("*")
    v1 = int(values[0])
    v2 = int(values[1])

    print(type(v1), type(v2))
    if isinstance(v1, int) and isinstance(v2, int):
        result = int(calc.multiply(v1, v2))
        print(f"'resultado': {result}")
        print(f"'resultado': {result}")
        return {"resultado": result}
