import abc
from typing import Optional, List
from domain import Pet

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, pet: Pet):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, pet_id: str) -> Optional[Pet]:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self) -> List[Pet]:
        raise NotImplementedError