class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
      return 2 * self.width + 2 * self.height

  def get_diagonal(self):
      return ((self.width ** 2 + self.height ** 2) ** .5)

  def __build_picture(self):
    shape = ""
    for i in range(self.height):
      shape += self.width * '*' + '\n'
    return shape
    
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      return self.__build_picture()

  def get_amount_inside(self, shape):
    shape_area = shape.get_area()
    my_rectangle_area = self.get_area()
    proportion = my_rectangle_area / shape_area
    if proportion > 1:
      return int(proportion)
    else:
      return 0
      
  def __str__(self):
    print_version = f"Rectangle(width={self.width}, height={self.height})"
    return print_version


class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
    self.side = side

  def set_side(self, side):
    self.width = side
    self.height = side
    self.side = side

  def set_width(self, side):
    self.width = side
    self.height = side
    self.side = side

  def set_height(self, side):
    self.width = side
    self.height = side
    self.side = side

  def __str__(self):
    print_version = f"Square(side={self.side})"
    return print_version