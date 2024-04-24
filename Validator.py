from cerberus import Validator


schema = {
    'name': {'type': 'string', 'required': True},
    'age': {'type': 'integer', 'min': 0, 'max': 120},
    'email': {'type': 'string', 'regex': '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'}
}


validator = Validator(schema)


data = {
    'name': 'John Doe',
    'age': 90,
    'email': 'john.doe@example.com'
}


if validator.validate(data):
    print("Data passed validation!")
else:
    print("Data did not pass validation:")
    for field, errors in validator.errors.items():
        print(f"Field '{field}': {', '.join(errors)}")
