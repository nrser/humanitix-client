from enum import Enum


class HiddenOptionsWhen(str, Enum):
    ALWAYS = "always"
    CONDITIONAL = "conditional"
    CUSTOMDATE = "customDate"
    NOTONSALE = "notOnSale"
    SOLDOUT = "soldOut"

    def __str__(self) -> str:
        return str(self.value)
