from abc import abstractmethod, ABC


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.positive_effects = base.positive_effects
        self.negative_effects = base.negative_effects
        self.stats = base.stats

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    @abstractmethod
    def get_positive_effects(self):
        pass


class AbstractNegative(AbstractEffect):
    @abstractmethod
    def get_negative_effects(self):
        pass


class Berserk(AbstractPositive):
    def get_positive_effects(self):
        self.positive_effects.append('Berserk')
        return self.positive_effects.copy()

    def get_stats(self):
        for key in "Strength", "Endurance", "Agility", "Luck":
            self.stats[key] += 7
        self.stats["HP"] += 50
        for key in "Intelligence", "Charisma", "Perception":
            self.stats[key] -= 3
        return self.stats.copy()


class Blessing(AbstractPositive):
    def get_positive_effects(self):
        self.positive_effects.append('Blessing')
        return self.positive_effects.copy()

    def get_stats(self):
        for key in self.stats:
            self.stats[key] += 2
        return self.stats.copy()


class Weakness(AbstractNegative):
    def get_negative_effects(self):
        self.negative_effects.append('Weakness')
        return self.negative_effects.copy()

    def get_stats(self):
        for key in 'Strength', 'Endurance', 'Agility':
            self.stats[key] -= 4
        return self.stats.copy()


class EvilEye(AbstractNegative):
    def get_negative_effects(self):
        self.negative_effects.append('EvilEye')
        return self.negative_effects.copy()

    def get_stats(self):
        self.stats['Luck'] -= 10
        return self.stats.copy()


class Curse(AbstractNegative):
    def get_negative_effects(self):
        self.negative_effects.append('Curse')
        return self.negative_effects.copy()

    def get_stats(self):
        for key in self.stats:
            self.stats[key] -= 2
        return self.stats.copy()


if __name__ == '__main__':
    hero = Hero()
    print(hero.get_stats())

    hero = Berserk(hero)
    print(hero.get_stats())

    hero = Blessing(hero)
    print(hero.get_stats())
    print(hero.get_positive_effects())
