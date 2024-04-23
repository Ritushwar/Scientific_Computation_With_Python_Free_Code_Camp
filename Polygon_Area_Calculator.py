class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    
    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2* self.width + 2* self.height

    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**.5)

    def get_picture(self):
        picture = ""
        if self.height > 50 or self.width > 50:
            picture = "Too big for picture."
        else:
            for h in range(self.height):
                picture = picture + "*"*self.width + "\n"
        return picture

    def get_amount_inside(self,obj):
        first = (self.width) // (obj.width)
        second = (self.height) // (obj.height)
        return first*second

class Square(Rectangle):
    def __init__(self,length):
        self.width = length
        self.height = length

    def __str__(self):
        return f"Square(side={self.width})"
    def set_side(self,length):
        self.width = length
        self.height = length

    def set_width(self,width):
        self.width = width
        self.height = width

    def set_height(self,height):
        self.width = height
        self.height = height

rect = Rectangle(10, 5)
print(rect.get_picture())   
