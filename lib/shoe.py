class Shoe:
    def __init__(self, brand, size, condition="New"):
        self._brand = brand
        self._size = size
        self._condition = condition

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Brand must be a non-empty string")
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            return
        if value <= 0:
            raise ValueError("Size must be a positive number")
        self._size = value

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        if value not in ["New", "Used", "Worn"]:
            raise ValueError("Condition must be New, Used, or Worn")
        self._condition = value

    def repair(self):
        self._condition = "New"
        return "Shoe repaired to New condition"

    def cobble(self):
        self._condition = "New"
        print("Your shoe is as good as new!")