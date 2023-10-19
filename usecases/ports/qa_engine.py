from abc import ABC, abstractmethod
from domain.video import Video


class QaEngine(ABC):

    @abstractmethod
    def send_message(self, message: str) -> None:
        pass

    @abstractmethod
    def get_response(self) -> str:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
