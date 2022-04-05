from utils.validations import name_validation


class Ingredient:
    def __init__(self, name: str, quantity: int, measure_unit: str, id=None):
        self.name = name
        self.quantity = quantity
        self.measure_unit = measure_unit
        self.id = id
        self._module = self.__class__.__module__
        self._class = self.__class__.__name__

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'quantity': self.quantity, 'measure unit': self.measure_unit,
                '_class': self._class, '_module': self._module}

    @classmethod
    def from_json(cls, jsdict):
        name = jsdict['name']
        quantity = jsdict['quantity']
        measure_unit = jsdict['measure unit']
        id = jsdict['id']
        _module = jsdict['_module']
        _class = jsdict['_class']
        return cls(name, quantity, measure_unit, id)
