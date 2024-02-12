# Console README

## Description
This console, `console.py`, is a command-line interface for managing objects in a hypothetical database. It supports basic operations such as creating, showing, destroying, updating, and listing instances of various classes (e.g., BaseModel, User, State).

## How to Run
1. Ensure you have Python 3 installed.
2. Execute the console by running the following command in your terminal:
```bash
./console.py
```
Alternatively, you can use `python3 console.py`.

## Usage
- **Commands:**
- `quit`: Exit the program.
- `EOF`: Signal to exit the program.
- `create <class_name>`: Create a new instance of the specified class.
- `show <class_name> <id>`: Display details of the instance with the given ID.
- `destroy <class_name> <id>`: Delete the instance with the given ID.
- `all [class_name]`: List all instances or instances of a specific class.
- `update <class_name> <id> <attribute_name> "<value>"`: Update an instance's attribute with the provided value.

- **Additional Features:**
- Default behavior supports methods like `all`, `show`, `destroy`, `update`, and `count`.
- Supports command chaining, e.g., `User.show(my_id).update(name, "John")`.

## Example
```bash
$ ./console.py
(hbnb) create User
e7c7194f-8650-4e45-ae61-624f6b51072d
(hbnb) show User e7c7194f-8650-4e45-ae61-624f6b51072d
[User] (e7c7194f-8650-4e45-ae61-624f6b51072d) {'id': 'e7c7194f-8650-4e45-ae61-624f6b51072d', 'created_at': datetime.datetime(2024, 2, 12, 10, 0, 0, 123456), 'updated_at': datetime.datetime(2024, 2, 12, 10, 0, 0, 123456)}
(hbnb) update User e7c7194f-8650-4e45-ae61-624f6b51072d name "John Doe"
(hbnb) show User e7c7194f-8650-4e45-ae61-624f6b51072d
[User] (e7c7194f-8650-4e45-ae61-624f6b51072d) {'id': 'e7c7194f-8650-4e45-ae61-624f6b51072d', 'created_at': datetime.datetime(2024, 2, 12, 10, 0, 0, 123456), 'updated_at': datetime.datetime(2024, 2, 12, 10, 0, 0, 123456), 'name': 'John Doe'}
```


