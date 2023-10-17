from abc import ABC, abstractmethod
from domain.video import Video


class ScriptExtractor(ABC):
    @abstractmethod
    def execute(self, video: Video):
        pass
