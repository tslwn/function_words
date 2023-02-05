from abc import ABC, abstractmethod
from typing import List, Tuple

TaggedWord = Tuple[str, str]

TaggedDocument = List[TaggedWord]


class AbstractTagger(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def _function_word_tags(self) -> List[str]:
        pass

    @property
    @abstractmethod
    def _removed_tags(self) -> List[str]:
        pass

    def is_function_word_tag(self, tag: str) -> bool:
        return tag in self._function_word_tags

    def is_removed_tag(self, tag: str) -> bool:
        return tag in self._removed_tags