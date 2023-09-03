class Rectangle:
    def __init__(self, width, height):
        self.height = height
        # if width:
        self.width = width
        # else:
        #     self.width = height

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def get_perimetr(self):
        return 2 * (self.height + self.width)

    def get_area(self):
        return self.width * self.height

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.width)

    def __sub__(self, other):
        return Rectangle(abs(self.width - other.width), abs(self.height - other.width))

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __str__(self):
        return f'прямоугольник: ({self.height}x{self.width}), S= {self.get_area()}, P= {self.get_perimetr()}'


    def __repr__(self):
        return f'{self.get_area()}'


if __name__ == "__main__":
    rect = Rectangle(2, 5)
    print(type(rect.get_area()))
    print(rect)
