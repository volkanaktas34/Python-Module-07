from ex0.creatures import Creature


class InvalidStrategyError(Exception):
    def __init__(self, creature: Creature, strategy: str) -> None:
        super().__init__("Invalid Creature "
                         f"'{creature.name}' for this {strategy} strategy")
