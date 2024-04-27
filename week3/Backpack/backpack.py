'''Packing backpacks'''

class Item:
    '''
    Item info.
    '''
    def __init__(self, name: str, weight: int | float, value: int | float) -> None:
        '''
        Item object attributes.
        '''
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self) -> str:
        '''
        Display Item object.
        '''
        return f'{self.name} ({self.weight} kg, ${self.value})'

    def __repr__(self) -> str:
        return self.name

class Backpack:
    '''
    Backpack info.
    '''
    _Backpack__capacity = 10

    @classmethod
    def set_capacity(cls, value: int):
        '''
        Set capacity of the backpack.
        '''
        cls._Backpack__capacity = value

    def __init__(self) -> None:
        '''
        Backpack object attributes.
        '''
        self._items = []

    @property
    def items(self):
        '''
        Items attribute.
        '''
        return self._items

    @items.setter
    def items(self, items_list: list[Item]):
        '''
        Pack backpack.
        '''
        for item in items_list:
            self.add_item(item)

    @items.deleter
    def items(self):
        '''
        Delete items.
        '''
        self._items = []

    @property
    def total_value(self) -> int | float:
        '''
        Find total value of items.
        '''
        if self._items:
            return sum(item.value for item in self._items)
        return 0

    @property
    def total_weight(self) -> int | float:
        '''
        Find total weight of items.
        '''
        if self._items:
            return sum(item.weight for item in self._items)
        return 0

    def add_item(self, item: Item) -> str:
        '''
        Add item to object items.
        '''
        if self.is_item_valid(item):
            if item.weight + self.total_weight > self._Backpack__capacity:
                return f"Item '{item.name}' is too heavy for the backpack."
            self._items.append(item)
            return 'Object added!'
        return 'Item is not valid'

    @staticmethod
    def is_item_valid(item: str | Item) -> bool:
        '''
        Check whether item is valid.
        '''
        return isinstance(item, Item) and item.weight > 0 and item.value > 0

    def remove_item(self, item: Item):
        '''
        Remove item from object items.
        '''
        if item in self.items:
            self._items.remove(item)
            return 'Object succesfully removed.'
        return None

    def __str__(self) -> str:
        '''
        Display Backpack object.
        '''
        if len(self.items) in {0, 1}:
            plural = 'item'
        else:
            plural = 'items'
        return f'Backpack contains {len(self.items)} {plural} with total \
weight {self.total_weight} kg and total value ${self.total_value}'
