from ex0 import CreatureFactory, FlameFactory, AquaFactory


def factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.decribe())
    print(base.attack())
    print(evolved.decribe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print(creature1.decribe())
    print("vs. ")
    print(creature2.decribe())
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()

    factory(flame)
    factory(aqua)
    battle(flame, aqua)


if __name__ == "__main__":
    main()
