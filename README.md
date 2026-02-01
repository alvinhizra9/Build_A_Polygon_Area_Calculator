# OOP Geometry Calculator 📐

This project is a Python-based library that models and manipulates 2D geometric shapes (Rectangles and Squares) using **Object-Oriented Programming (OOP)**. A solution of freecodecamp python certification project. It demonstrates the application of clean code principles, inheritance, and algorithmic logic to solve geometric problems.

## 🚀 Key Features

*   **Geometric Calculations:** Precisesly calculates area, perimeter, and diagonal length.
*   **Visual Rendering:** Generates visual representations of shapes using ASCII art.
*   **Containment Logic:** Algorithms to calculate how many smaller shapes fit into a larger one.
*   **Dynamic Resizing:** Runtime modification of shape dimensions maintaining geometric integrity.

## 🛠️ Software Engineering & Python Skills

This project was built to demonstrate proficiency in the following technical areas:

### 1. Object-Oriented Architecture (OOP)
*   **Inheritance:** The `Square` class inherits from `Rectangle`, adhering to the **DRY (Don't Repeat Yourself)** principle by reusing logic for area, perimeter, and rendering.
*   **Polymorphism:** Implemented method overriding in the `Square` class (specifically `set_width` and `set_height`) to enforce the definition of a square (width must equal height) without breaking the interface.
*   **Super() Implementation:** usage of `super()` to handle parent class initialization efficiently.

### 2. Python Internals & Magic Methods
*   **Dunder Methods:** Custom implementation of `__str__` to provide human-readable string representations of objects, facilitating easier debugging and logging.
*   **Math Module Integration:** Utilization of the standard `math` library for precise diagonal calculations.

### 3. Defensive Programming & Validation
*   **Input Validation:** The constructor (`__init__`) implements guards against invalid data (e.g., negative dimensions) by raising specific `ValueError` exceptions.
*   **Edge Case Handling:** The visualization method includes guards to prevent rendering excessively large shapes that would clutter the output.

### 4. Algorithmic Logic
*   **Spatial Calculation:** The `get_amount_inside()` method uses floor division (`//`) logic to determine spatial capacity without rotation.
*   **String Manipulation:** Efficient use of loops and f-strings to render the ASCII "picture" of the shapes.

## 💻 Usage

### Prerequisites
*   Python 3.x

### Running the Project
Save the code in a file (e.g., `main.py`) and run:

```bash
python main.py
