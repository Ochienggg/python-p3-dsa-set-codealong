class MySet:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.dictionary = {}
        for element in elements:
            self.dictionary[element] = True

    def has(self, element):
        return element in self.dictionary

    def add(self, element):
        self.dictionary[element] = True
        return self

    def delete(self, element):
        self.dictionary.pop(element, None)
        return self

    def size(self):
        return len(self.dictionary)
