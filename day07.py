from functools import cmp_to_key, partial
import common as c



def part(data, joker):
    hands = parse_input(data, joker=joker)
    hands = sorted(hands, key=cmp_to_key(partial(hand_cmp, joker=joker)))
    total = 0
    for r, hb in enumerate(hands, 1):
        total += r * hb[1]
    return total


def hand_cmp(h1, h2, joker):
    h1, h2 = h1[0], h2[0]
    if hand_type(h1, joker) < hand_type(h2, joker):
        return -1
    elif hand_type(h1, joker) > hand_type(h2, joker):
        return 1
    elif h1 < h2:
        return -1
    else:
        return h1 > h2
 

def hand_type(hand, joker) -> int:
    cgs = card_groups(hand)
    jg = joker_group(cgs) if joker else -1
    if is_five_kind(cgs, jg):
        return 7
    if is_four_kind(cgs, jg):
        return 6
    if is_full_house(cgs, jg):
        return 5
    if is_three_kind(cgs, jg):
        return 4
    if is_two_pair(cgs, jg):
        return 3
    if is_one_pair(cgs, jg):
        return 2
    return 1


def card_groups(hand):
    sorted_hand = sorted(hand)
    res = [[]]
    for card in sorted_hand:
        if len(res[-1]) == 0 or res[-1][0] == card:
            res[-1].append(card)
        else:
            res.append([card])
    return sorted(res, key=lambda x: len(x), reverse=True)


def is_five_kind(cgs, jg):
    """
    >>> is_five_kind(card_groups(parse_hand("JJJJA", True)), 0)
    True
    >>> is_five_kind(card_groups(parse_hand("AAAAJ", True)), 1)
    True
    >>> is_five_kind(card_groups(parse_hand("TJTJT", True)), 1)
    True
    """
    if len(cgs) == 1:
        return True
    if len(cgs) == 2 and jg >= 0:
        return True
    return False


def is_four_kind(cgs, jg):
    """
    >>> is_four_kind(card_groups(parse_hand("JJKJA", True)), 0)
    True
    >>> is_four_kind(card_groups(parse_hand("KJKKA", True)), 1)
    True
    >>> is_four_kind(card_groups(parse_hand("KTJJT", True)), 1)
    True
    """
    if len(cgs[0]) == 4:
        return True
    if len(cgs[0]) == 3 and jg >= 0:
        return True
    if len(cgs[0]) == len(cgs[1]) == 2 and (jg == 0 or jg == 1):
        return True
    return False


def is_full_house(cgs, jg):
    """
    >>> is_full_house(card_groups(parse_hand("KJKAK", True)), 1)
    True
    >>> is_full_house(card_groups(parse_hand("323J2", True)), 2)
    True
    """
    if len(cgs[0]) == 3 and len(cgs[1]) == 2:
        return True
    if (len(cgs[0]) == 3 and jg > 0) or (len(cgs[0]) == len(cgs[1]) == 2 and jg == 2):
        return True
    return False


def is_three_kind(cgs, jg):
    """
    >>> is_three_kind(card_groups(parse_hand("23456", True)), -1)
    False
    >>> is_three_kind(card_groups(parse_hand("2J456", True)), 1)
    False
    >>> is_three_kind(card_groups(parse_hand("2J4J6", True)), 0)
    True
    >>> is_three_kind(card_groups(parse_hand("464QJ", True)), 2)
    True
    """
    if len(cgs[0]) == 3:
        return True
    if len(cgs[0]) == 2 and jg >= 0:
        return True
    return False


def is_two_pair(cgs, jg):
    """
    >>> is_two_pair(card_groups(parse_hand("23456", True)), -1)
    False
    >>> is_two_pair(card_groups(parse_hand("2J456", True)), 1)
    False
    >>> is_two_pair(card_groups(parse_hand("2J455", True)), 1)
    True
    """
    if len(cgs[0]) == 2 and len(cgs[1]) == 2:
        return True
    if len(cgs[0]) == 2 and jg > 0:
        return True
    return False


def is_one_pair(cgs, jg):
    if len(cgs[0]) == 2 or jg >= 0:
        return True
    return False


def joker_group(card_groups):
    for i in range(len(card_groups)):
        if 1 in card_groups[i]:
            return i
    return -1


def parse_input(data, joker: bool) -> list[tuple[tuple, int]]:
    hands = []
    for line in c.strings(data):
        h, b = line.split()
        hands.append((parse_hand(h, joker), int(b)))
    return hands


def parse_hand(hand_str, joker: bool) -> tuple[int]:
    res = []
    for card in hand_str:
        match card:
            case "T":
                res.append(10)
            case "J":
                res.append(1 if joker else 11)
            case "Q":
                res.append(12)
            case "K":
                res.append(13)
            case "A":
                res.append(14)
            case _:
                res.append(int(card))
    return tuple(res)
     

print(part(c.day(7), joker=False))
print(part(c.day(7), joker=True))
