class Encapsulation:
    def __init__(self):
        self.public = "I am Public"
        self._protected = "I am Protected"
        self.__private = "I am private"

    @property
    def protected(self):
        return self._protected

    @property
    def private(self):
        return self.__private

    @private.setter
    def private(self, value):
        self.__private = value


Encapsulation_object = Encapsulation()
print(Encapsulation_object.public)
print(Encapsulation_object.protected)
Encapsulation_object.private = "I have been  changed"
print(Encapsulation_object.private)