def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return (lambda s: (spell1(s), spell2(s)))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return (lambda s: base_spell(s) * multiplier)


def conditional_caster(condition: callable, spell: callable) -> callable:
    return (lambda s: spell(s) if condition(s) else "Spell fizzled")


def spell_sequence(spells: list[callable]) -> callable:
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
