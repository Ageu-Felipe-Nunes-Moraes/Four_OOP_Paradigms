# Object-Oriented Programming: Fundamental Concepts

In this code, I explore the essential principles of Object-Oriented Programming (OOP) through the implementation of classes in Python. We will examine each of these concepts and how they are applied in the provided code:

## Abstraction

Abstraction is the process of highlighting important information while hiding unnecessary details. In the code, we see that the classes and methods are designed to focus on the essential functionalities of each object, such as making a specific sound, without worrying about the internal implementation.

## Encapsulation

Encapsulation organizes the code to protect its internal components, allowing future changes with minimal impact on other parts of the system. In the code, the properties of the classes are defined as private (`_name`) to control external access, following the principle of encapsulation.

## Polymorphism

Polymorphism allows objects of different classes to be treated uniformly, enabling methods with the same name to behave differently in each class. In the example, each animal has a `make_sound()` method, which is polymorphic, producing different sounds for each type of animal.

## Inheritance

Inheritance allows a child class to inherit attributes and methods from a parent class, promoting code reuse and facilitating the hierarchical organization of objects. In the code, we see the class hierarchy where `WildAnimal` and `DomesticAnimal` inherit from `Animal`, and `Snake`, `Dog`, and `Cat` inherit from `WildAnimal` and `DomesticAnimal`, respectively.

## Installation Requirements

- Python 3.x

## How to Run

1. Ensure Python is installed on your system.
2. Clone or download the repository of this code.
3. Run the main file.

## Contributions

If you wish to contribute to the development of this code:

1. Fork the repository.
2. Make your modifications and improvements to the code.
3. Test your changes to ensure correct functionality.
4. Submit a pull request describing the changes made and your justifications.

## Author

This project was developed by Ageu Felipe Nunes Moraes (me) with the purpose of synthesizing one of the OOP contents as much as possible, as part of a personal project dedicated to strengthening and maturing coding skills. For any questions or suggestions, please contact me at [ageumoraes67@gmail.com].

## Disclaimer

This is a software project developed by an individual, inspired by a past academic activity during a class.
