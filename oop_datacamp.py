# class Customer:
#     def __init__(self, name, balance=0.0):
#         self.name = name
#         self.balance = balance
#     def __str__(self):
#         return f"Customer {self.name} has balance {self.balance}"

# cust = Customer("Abdul Qadeer", 1000)
# print(cust)


# print(f" Customer name: {cust.name}\n Balance: {cust.balance}")
# print("Hello {} dear".format("hello"))

# #three types of string formatting
# #1. using % operator
# print("I am one the blessed student %s %s" % (cust.name, cust.balance))
# #2. using format method
# #3. using f-string

# # print("I am one the blessed student %s %s" %cust.name %cust.balance)


class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      

    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)      
        return s
      
    # Add the __repr__method  
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})"
    
#what is difference between __str__ and __repr__?
#The __str__ method is used to return a user-friendly string that describes the object.
#The __repr__ method is used to return an unambiguous string that describes the object.
#when to use __str__ and __repr__?
#Use __str__ for creating output for end users.
#Use __repr__ for debugging and development.


emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))


# Polymorphism in Python refers to the ability for objects of different classes to respond differently to the same method call. It's a powerful concept that allows for flexible and reusable code. Here's a breakdown of polymorphism in Python:

# Imagine a Zoo:

# Think of your code as a zoo with different types of animals (classes) like lions, tigers, and bears (objects). Polymorphism allows you to have a common method, like "make_sound()", for all these animals. However, each animal will make a unique sound specific to its species.

# In Python Code:

# You can define a base class (like "Animal") with a method "make_sound()". This method might be empty in the base class, acting as a placeholder.
# Derived classes (like "Lion", "Tiger", and "Bear") inherit from the base class.
# Each derived class overrides the "make_sound()" method with its specific sound (roar, growl, or roar).
# When you call "make_sound()" on an object of a derived class (e.g., a lion object), Python automatically executes the overridden method specific to that class (the lion's roar).

# Benefits of Polymorphism:

# Flexibility: Code becomes more adaptable as you can add new derived classes with their own implementations without modifying the base class code.
# Reusability: You can write generic code that works with various objects as long as they share the same base class and method name.
# Cleaner Code: Polymorphism promotes cleaner and more readable code by separating the core functionalities in the base class and allowing specific behaviors in derived classes.
# Here's an example to illustrate:

class Animal:
  def make_sound(self):
    # Empty method in base class (placeholder)
    pass

class Lion(Animal):
  def make_sound(self):
    print("The lion roars!")

class Tiger(Animal):
  def make_sound(self):
    print("The tiger growls!")

# Create animal objects
lion = Lion()
tiger = Tiger()

# Call the same method on different objects - polymorphism in action!
lion.make_sound()  # Output: The lion roars!
tiger.make_sound()  # Output: The tiger growls!


# Operator overloading in Python allows you to define custom behavior for operators (like +, -, *, etc.) when used with objects of a class. This makes your code more intuitive and readable, especially when dealing with custom objects.

# **Here's a breakdown of operator overloading in Python:**

# **Why Overload Operators?**

# Imagine you have a class called `Vector` to represent 2D or 3D vectors. Wouldn't it be more natural to add two vectors using the `+` operator instead of a cumbersome custom method? Operator overloading allows you to achieve this.

# **How Does it Work?**

# Python relies on special methods within a class to define custom behavior for operators. These methods have names that start with double underscores (`__`) followed by the operator symbol.

# **For example:**

# * `__add__(self, other)`: Defines custom behavior for the `+` operator when used with a `Vector` object.
# * `__sub__(self, other)`: Defines custom behavior for the `-` operator.
# * `__mul__(self, other)`: Defines custom behavior for the `*` operator.

# **Example with Code:**

class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # Overloading the + operator for vector addition
  def __add__(self, other):
    if isinstance(other, Vector):
      return Vector(self.x + other.x, self.y + other.y)
    else:
      raise TypeError("Can only add vectors with other vectors")

  # Overloading the * operator for scalar multiplication
  def __mul__(self, scalar):
    return Vector(self.x * scalar, self.y * scalar)

  # ... other methods for the Vector class

v1 = Vector(2, 3)
v2 = Vector(1, 4)

# Custom addition using the overloaded + operator
v3 = v1 + v2  # Equivalent to v1.__add__(v2)
print(v3.x, v3.y)  # Output: 3 7

# Scalar multiplication using the overloaded * operator
v4 = v1 * 3
print(v4.x, v4.y)  # Output: 6 9

# We use the `isinstance()` function in Python for type checking in a controlled and informative way. Here are some key reasons why it's valuable:

# **1. More Informative than `type()`:**

# * The `type()` function simply returns the exact data type of an object. 
# * `isinstance()`, however, allows you to check if an object is an instance of a specific class or a subclass of that class. This provides more flexibility.

# **Example:**

# ```python
x = 10
# type() only tells you the exact type
print(type(x))  # Output: <class 'int'>

# isinstance() allows checking for subclasses
class MyNumber:
  pass

y = MyNumber()

print(isinstance(x, int))  # True - x is an instance of the built-in int class
print(isinstance(y, MyNumber))  # True - y is an instance of the MyNumber class (subclass of object)
# ```

# **2. Handling Inheritance:**

# * In object-oriented programming (OOP), classes can inherit from other classes. 
# * `isinstance()` lets you check if an object belongs to a specific class hierarchy, ensuring it has the necessary methods and attributes.

# **Example:**

# ```python
class Animal:
  def make_sound(self):
    pass

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

animal = Animal()
dog = Dog()

print(isinstance(animal, Dog))  # False - animal is not a Dog instance (but an Animal)
print(isinstance(dog, Animal))  # True - dog inherits from Animal
# ```

# **3. Flexible Type Checking:**

# * You can use `isinstance()` to check if an object belongs to one of multiple classes by passing a tuple of class types.

# **Example:**

# ```python
def process_number(number):
  if isinstance(number, (int, float)):
    # Perform calculations
    pass
  else:
    print("Error: Invalid number type")

process_number(10)  # Valid - int
process_number(3.14)  # Valid - float
process_number("Hello")  # Error - not a number type
# ```

# **4. Avoiding Type Errors:**

# * By using `isinstance()` for type checking, you can anticipate potential type mismatches and handle them gracefully before errors occur during runtime. This improves code robustness.

# By incorporating `isinstance()` into your code, you can write more robust and flexible programs with clear type expectations. It goes beyond basic type checks with `type()` and offers valuable benefits for object-oriented programming in Python.


# **Important Considerations:**

# * Overloading operators should be done judiciously to avoid making code confusing. Only overload operators when it makes sense for your custom object type.
# * Always consider type checking within your overloaded methods to ensure compatibility when performing operations with other objects.

# By effectively using operator overloading, you can create more intuitive and user-friendly code when working with custom data types in Python.

#  **Here's an explanation of access modifiers in Python with code examples:**

# **Access modifiers control the visibility and accessibility of attributes and methods within a class, enforcing encapsulation. Python supports three types:**

# **1. Public:**

# * Accessible from anywhere in the code.
# * Defined without any special prefix.

# **Example:**

class Dog:
  def __init__(self, name, breed):
    self.name = name  # Public attribute
    self.breed = breed  # Public attribute

  def bark(self):  # Public method
    print("Woof!")

# **2. Protected:**

# * Intended for internal use within a class and its subclasses.
# * Prefixed with a single underscore (_).
# * Access outside the class or subclasses is possible but discouraged by convention.

# **Example:**c

class Dog:
  def __init__(self, name, breed):
    self._name = name  # Protected attribute
    self._breed = breed  # Protected attribute

  def _get_breed(self):  # Protected method
    return self._breed

# **3. Private:**

# * Strongly restricted for internal use within a class only.
# * Prefixed with double underscores (__) (name mangling).
# * Cannot be accessed directly from outside the class or even subclasses.

# **Example:**

class Dog:
  def __init__(self, name, breed):
    self.__name = name  # Private attribute
    self.__breed = breed  # Private attribute

  def __secret_method(self):  # Private method
    print("This is a secret!")

# **Key Points:**

# * Python doesn't have strict access control like some other languages.
# * Conventions (single underscore for protected, double for private) guide visibility.
# * Name mangling for private members makes direct access difficult but not impossible.
# * Carefully consider access modifiers to promote encapsulation and maintainability.

