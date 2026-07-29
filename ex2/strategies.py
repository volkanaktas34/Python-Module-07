from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealCapability, TransformCapability
from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        raise NotImplementedError

    @abstractmethod
    def act(self, creature: Creature) -> str:
        raise NotImplementedError


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature, "normal")
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if (
            not self.is_valid(creature)
            or not isinstance(creature, TransformCapability)
        ):
            raise InvalidStrategyError(creature, "aggressive")
        return (
            creature.transform() + "\n"
            + creature.attack() + "\n" + creature.revert()
        )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if (
            not self.is_valid(creature)
            or not isinstance(creature, HealCapability)
        ):
            raise InvalidStrategyError(creature, "defensive")
        return creature.attack() + "\n" + creature.heal()
