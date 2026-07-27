from ex1 import HealingCreatureFactory, TransformCreatureFactory


def healing() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    base = factory.create_base()
    print("base:")
    print(base.decribe())
    print(base.attack())
    print(base.heal())

    evolved = factory.create_evolved()
    print("evolved")
    print(evolved.decribe())
    print(evolved.attack())
    print(evolved.heal())


def transform() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    base = factory.create_base()
    print("base:")
    print(base.decribe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    evolved = factory.create_evolved()
    print("evolved:")
    print(evolved.decribe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    healing()
    transform()


if __name__ == "__main__":
    main()
