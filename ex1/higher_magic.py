from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return (lambda s: (spell1(s), spell2(s)))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return (lambda s: base_spell(s) * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return (lambda s: spell(s) if condition(s) else "Spell fizzled")


def spell_sequence(spells: list[Callable]) -> Callable:
    def run(s):
        result = []
        for sp in spells:
            result.append(sp(s))
        return (result)
    return (run)


if (__name__ == "__main__"):
    print("\nTesting spell combiner...")
    comb = spell_combiner(
        lambda s: f"Fireball hits {s}", lambda s: f"Heals {s}")("Dragon")
    print(f"Combined spell result: {comb[0]}, {comb[1]}")
    print("\nTesting power amplifier...")
    def ori(s): return 10
    amp = power_amplifier(ori, 3)("test")
    print(f"Original: {ori('test')}, Amplified: {amp}")
