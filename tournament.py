from ex0 import CreatureFactory, AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy,
                 AggressiveStrategy, DefensiveStrategy, InvalidStrategyError)

opponents = list[tuple[CreatureFactory, BattleStrategy]]


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            first = factory1.create_base()
            second = factory2.create_base()
            print("\n* Battle *")
            print(first.describe())
            print("vs.")
            print(second.describe())
            print("now fight!")

            try:
                print(strategy1.act(first))
                print(strategy2.act(second))
            except InvalidStrategyError as error:
                print("Battle error, aborting tournament:", error)
                return


def tournament() -> None:
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(FlameFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy())])
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(FlameFactory(), AggressiveStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy())])
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(AquaFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
            (TransformCreatureFactory(), AggressiveStrategy())])


def main() -> None:
    tournament()


if __name__ == "__main__":
    main()
