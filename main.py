import math

# =============================================================================
# Rectangle Class
# A class representing a rectangle shape with width and height properties
# =============================================================================
class Rectangle:
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle object with given width and height.
        
        Args:
            width: The width of the rectangle (must be non-negative)
            height: The height of the rectangle (must be non-negative)
        
        Raises:
            ValueError: If width or height is negative
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height
    
    def set_width(self, new_width):
        """Set a new width for the rectangle."""
        self.width = new_width
    
    def set_height(self, new_height):
        """Set a new height for the rectangle."""
        self.height = new_height
    
    def get_area(self):
        """
        Calculate and return the area of the rectangle.
        Formula: width × height
        """
        return self.width * self.height
    
    def get_perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        Formula: 2 × (width + height)
        """
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        """
        Calculate and return the diagonal length of the rectangle.
        Uses Pythagorean theorem: √(width² + height²)
        """
        return math.sqrt(
            self.width ** 2 +
            self.height ** 2
        )
    
    def get_picture(self):
        """
        Generate a string representation of the rectangle using asterisks (*).
        
        Returns:
            A string with asterisks forming the rectangle shape,
            or an error message if dimensions exceed 50.
        """
        # Check if dimensions are too large to display
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        # Build the picture row by row
        result = ''
        for i in range(self.height):
            result += f"{'*' * self.width}\n"
        return result
    
    def get_amount_inside(self, shape):
        """
        Calculate how many times another shape can fit inside this rectangle.
        
        Args:
            shape: Another Rectangle or Square object
        
        Returns:
            The number of shapes that can fit (without rotation)
        """
        # Calculate how many fit horizontally and vertically
        horizontal_fit = self.width // shape.width
        vertical_fit = self.height // shape.height
        return horizontal_fit * vertical_fit
    
    def __str__(self):
        """Return a string representation of the Rectangle object."""
        return f'Rectangle(width={self.width}, height={self.height})'


# =============================================================================
# Square Class (inherits from Rectangle)
# A specialized rectangle where width equals height
# =============================================================================
class Square(Rectangle):
    
    def __init__(self, side):
        """
        Initialize a Square object with given side length.
        
        Args:
            side: The length of each side of the square
        """
        # Call parent constructor with equal width and height
        super().__init__(side, side)
    
    def set_width(self, new_side):
        """
        Set a new side length (overrides Rectangle method).
        Updates both width and height to maintain square property.
        """
        self.width = new_side
        self.height = new_side
    
    def set_height(self, new_side):
        """
        Set a new side length (overrides Rectangle method).
        Updates both width and height to maintain square property.
        """
        self.width = new_side
        self.height = new_side
    
    def set_side(self, new_side):
        """
        Set a new side length for the square.
        This is the preferred method for changing square dimensions.
        """
        self.width = new_side
        self.height = new_side
    
    def __str__(self):
        """Return a string representation of the Square object."""
        return f'Square(side={self.width})'


# =============================================================================
# Main Program - Testing the Rectangle and Square classes
# =============================================================================
if __name__ == '__main__':
    # ----- Testing Rectangle -----
    rect = Rectangle(10, 5)
    print(rect.get_area())       # Expected: 50
    
    rect.set_height(3)
    print(rect.get_perimeter())  # Expected: 26 (2 × (10 + 3))
    print(rect)                  # Expected: Rectangle(width=10, height=3)
    print(rect.get_picture())    # Display 10×3 rectangle with asterisks

    # ----- Testing Square -----
    sq = Square(9)
    print(sq.get_area())         # Expected: 81 (9 × 9)
    
    sq.set_side(4)
    print(sq.get_diagonal())     # Expected: 5.656... (√32)
    print(sq)                    # Expected: Square(side=4)
    print(sq.get_picture())      # Display 4×4 square with asterisks

    # ----- Testing get_amount_inside -----
    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))  # Expected: 8 (4×2 squares fit inside)
