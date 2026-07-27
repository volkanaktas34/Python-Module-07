from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self):
        return "Sproutling uses Vine Whip!"

    def heal(self):
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self):
        return "Bloomelle uses Petal Dance!"

    def heal(self):
        return "Bloomelle heals itself and others for a large amount\n"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")
        self._transformed = False

    def transform(self) -> str:
        self._transformed = True
        return "Shiftling shifts into a sharper form!"

    def attack(self):
        if self._transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def revert(self):
        self._transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        self._transformed = False

    def transform(self):
        self._transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def attack(self):
        if self._transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def revert(self):
        self._transformed = False
        return "Morphagon stabilizes its form."
