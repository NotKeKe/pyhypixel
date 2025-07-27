from abc import ABC, abstractmethod
from aiohttp import ClientResponse

class API(ABC):
    @abstractmethod
    def get_rate(self, resp: ClientResponse) -> None:
        pass