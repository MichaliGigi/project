from abc import ABC, abstractmethod
from imageSelector.Image import *


class ImageQuality(ABC):

    @abstractmethod
    def calculateGrade(self, image):
        pass
