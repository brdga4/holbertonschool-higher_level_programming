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
        """
        Serializes the current instance of CustomObject to a file using pickle.
        """
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        static method to deserialize a CustomObject instance from a file.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
