import abc

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self):
        raise NotImplementedError


class InMemoryRepository(AbstractRepository):
    def __init__(self):
        self._data = {}
        self._id_counter = 1

    def add(self, entity):
        entity_id = self._id_counter
        self._data[entity_id] = entity
        self._id_counter += 1
        return entity_id

    def get(self, id):
        return self._data.get(id)

    def list(self):
        return list(self._data.values())


class FakeRepository(AbstractRepository):
    def __init__(self, items):
        self._items = list(items)

    def add(self, entity):
        self._items.append(entity)

    def get(self, id):
        try:
            return self._items[id]
        except IndexError:
            return None

    def list(self):
        return self._items
