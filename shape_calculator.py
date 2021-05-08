import math


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # I would use @property decorator, but the rule is to use set_width name
    def set_width(self, new_width):
        self._width = new_width

    def set_height(self, new_height):
        self._height = new_height

    def get_area(self) -> float:
        return self._width * self._height

    def get_perimeter(self) -> float:
        return (2 * self._width) + (2 * self._height)

    def get_diagonal(self) -> float:
        return (self._width ** 2 + self._height ** 2) ** .5

    def get_picture(self) -> str:
        if self._width > 50 or self._height > 50:
            return 'Too big for picture.'

        symbol_line = '*' * self._width + '\n'
        picture = ''
        for line in range(self._height):
            picture += symbol_line
        return picture

    def get_amount_inside(self, rect_obj):
        return math.floor(self.get_area() / rect_obj.get_area())

    def __str__(self):
        return f'Rectangle(width={self._width}, height={self._height})'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self._side = side

    def set_side(self, new_side):
        super().set_height(new_side)
        super().set_width(new_side)
        self._side = new_side

    def set_width(self, new_width):
        self.set_side(new_width)

    def set_height(self, new_height):
        self.set_side(new_width)

    def __str__(self):
        return f'Square(side={self._side})'
