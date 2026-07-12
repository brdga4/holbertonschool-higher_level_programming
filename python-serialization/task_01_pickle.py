import pickle


class CustomObject:
    """A custom class to represent an individual's basic details."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes the CustomObject with a name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object's attributes in a clean format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb", encoding="utf-8") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb", encoding="utf-8") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
