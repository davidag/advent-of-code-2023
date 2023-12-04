from collections import defaultdict
import common as c


def part_one(data):
    card_numbers = parse_input(data)
    points = 0
    for winning, mine in card_numbers:
        num_matches = card_matches(winning, mine)
        if num_matches > 0:
            points += 1 << num_matches - 1
    return points


def part_two(data):
    card_numbers = parse_input(data)
    scratchcards = defaultdict(lambda: 1)
    for i, (winning, mine) in enumerate(card_numbers, 1):
        num_cards = scratchcards[i]
        for j in range(1, card_matches(winning, mine) + 1):
            scratchcards[i + j] += num_cards
    return sum(card for card in scratchcards.values())


def card_matches(winning, mine):
    return len(winning & mine)


def parse_input(data: str) -> list[tuple[frozenset, frozenset]]:
    card_numbers = []
    for card in c.strings(data):
        numbers = card.split(":")[1]
        winning, mine = numbers.split("|")
        card_numbers.append(
            (set(c.ints(winning)), set(c.ints(mine)))
        )
    return card_numbers


print(part_one(c.day(4)))
print(part_two(c.day(4)))
