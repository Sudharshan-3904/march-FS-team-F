import re

class DataManager:
    def __init__(self):
        self.data = []  # Stores data as a list of dictionaries
        self.ids = set()  # Track unique IDs

    def is_valid_id(self, id_):
        return isinstance(id_, int) and id_ not in self.ids

    def is_valid_name(self, name):
        return isinstance(name, str) and bool(re.match("^[A-Za-z ]+$", name))

    def is_valid_age(self, age):
        return isinstance(age, int) and 0 <= age < 50

    def add_entry(self, id_, name, age):
        if not self.is_valid_id(id_):
            print(f"Invalid ID: {id_} (must be unique and an integer).")
            return False
        if not self.is_valid_name(name):
            print(f"Invalid Name: {name} (should contain only alphabets and spaces).")
            return False
        if not self.is_valid_age(age):
            print(f"Invalid Age: {age} (should be an integer below 50).")
            return False

        entry = {"ID": id_, "Name": name, "Age": age}
        self.data.append(entry)
        self.ids.add(id_)
        print("Entry added successfully.")
        return True

    def display_data(self):
        if not self.data:
            print("No data available.")
            return
        for entry in self.data:
            print(entry)

# Example Usage
manager = DataManager()
manager.add_entry(1, "John Doe", 25)
manager.add_entry(2, "Jane123", 30)  # Invalid name
manager.add_entry(3, "Alice", 55)  # Invalid age
manager.add_entry(1, "Bob", 40)  # Duplicate ID
manager.display_data()
