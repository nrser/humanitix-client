from enum import Enum


class CategoryOtherCategory(str, Enum):
    HOBBIESANDSPECIALINTEREST = "hobbiesAndSpecialInterest"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
