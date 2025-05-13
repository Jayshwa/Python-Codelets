class Human:
    """
    A base class representing a human being with a name and age.
    This class demonstrates the concept of inheritance in object-oriented programming.
    """
    def __init__(self, name, age):
        """
        Initializes a Human object with a name and age.

        Args:
            name (str): The name of the human.
            age (int): The age of the human in years.
        """
        self.name = name  # Stores the provided name as an attribute.
        self.age = age    # Stores the provided age as an attribute.

    def limbs(self):
        """
        Returns the typical number of limbs for a human.

        Returns:
            int: The number 4.
        """
        return 4

class Family(Human):
    """
    A class representing a member of a family, inheriting properties from the Human class.
    It adds a 'family' attribute and overrides the 'limbs' method.
    This demonstrates inheritance and method overriding.
    """
    def __init__(self, name, age, family):
        """
        Initializes a Family object with a name, age, and family name.

        Args:
            name (str): The name of the family member (inherited from Human).
            age (int): The age of the family member (inherited from Human).
            family (str): The name of the family this person belongs to.
        """
        super().__init__(name, age)  # Calls the __init__ method of the parent class (Human)
                                     # to initialize the name and age attributes.
        self.family = family        # Stores the provided family name as an attribute.

    def limbs(self):
        """
        Overrides the limbs method from the Human class.
        In this context, it seems to represent something specific to the 'Family'
        class, returning 2 instead of the typical 4 for a human.
        Note: This is a somewhat unusual representation and might be for illustrative purposes.

        Returns:
            int: The number 2.
        """
        return 2

# Creating an instance (object) of the Family class.
# Here, we are creating an object named 'John' who is 25 years old and belongs to the "Smith" family.
John = Family("John", 25, "Smith")

# Accessing the 'family' attribute of the 'John' object.
# This will print the family name that was provided when the 'John' object was created.
print(John.family)