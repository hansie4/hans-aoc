import os
from functools import cmp_to_key

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")

data = f.read().splitlines()

cardMap = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

cardMap2 = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,
}

handType = dict()


def compareCard(card1: str, card2: str):
    if cardMap[card1] > cardMap[card2]:
        return 1
    elif cardMap[card2] > cardMap[card1]:
        return -1
    else:
        return 0


def compareCard2(card1: str, card2: str):
    if cardMap2[card1] > cardMap2[card2]:
        return 1
    elif cardMap2[card2] > cardMap2[card1]:
        return -1
    else:
        return 0


def compareHands(hand1: tuple, hand2: tuple):
    hand1String = hand1[0]
    hand2String = hand2[0]

    hand1Counts = hand1[2].values()
    hand2Counts = hand2[2].values()

    # Five of a kind
    if 5 in hand1Counts and 5 not in hand2Counts:
        return 1
    elif 5 in hand2Counts and 5 not in hand1Counts:
        return -1

    # Four of a kind
    if 4 in hand1Counts and 4 not in hand2Counts:
        return 1
    elif 4 in hand2Counts and 4 not in hand1Counts:
        return -1

    # Full house
    hand1HasFullHouse = 3 in hand1Counts and 2 in hand1Counts
    hand2HasFullHouse = 3 in hand2Counts and 2 in hand2Counts
    if hand1HasFullHouse and not hand2HasFullHouse:
        return 1
    elif hand2HasFullHouse and not hand1HasFullHouse:
        return -1

    # Three of a kind
    if 3 in hand1Counts and 3 not in hand2Counts:
        return 1
    elif 3 in hand2Counts and 3 not in hand1Counts:
        return -1

    # Two pair
    x = [i for i in hand1Counts if i == 2]
    y = [i for i in hand2Counts if i == 2]
    if len(x) == 2 and len(y) != 2:
        return 1
    elif len(y) == 2 and len(x) != 2:
        return -1

    # One pair
    if 2 in hand1Counts and 2 not in hand2Counts:
        return 1
    elif 2 in hand2Counts and 2 not in hand1Counts:
        return -1

    for x in range(len(hand1String)):
        v1 = hand1String[x]
        v2 = hand2String[x]

        comp = compareCard(v1, v2)

        if comp != 0:
            return comp

    return 0


def compareHandStrings2(hand1String: str, hand2String: str):
    for x in range(len(hand1String)):
        v1 = hand1String[x]
        v2 = hand2String[x]

        comp = compareCard2(v1, v2)

        if comp != 0:
            return comp

    return 0


def getHandScore(handCards: list, numJokers: int):
    if len(handCards) == 1 or (len(handCards) == 0 and numJokers == 5):
        # Five of a kind
        return 7

    if len(handCards) == 5:
        # High Card
        return 1

    if len(handCards) == 4:
        # One pair
        return 2

    if len(handCards) == 3:
        # Could be a three of a kind or 2 pairs
        if numJokers == 0 and 3 not in handCards:
            # 2 Pairs
            return 3
        else:
            # Three of a kind
            return 4

    if len(handCards) == 2:
        # Could be Four of a kind or full house
        if 1 in handCards:
            # Four of a kind
            return 6
        else:
            # Full house
            return 5


def populatehandTypeDict(hands: list):
    for h in hands:
        handCards = list()
        numJokers = 0

        for x in h[2].keys():
            if x == "J":
                numJokers = h[2][x]
            else:
                handCards.append(h[2][x])

        handType[h[0]] = getHandScore(handCards, numJokers)


def compareHands2(hand1: tuple, hand2: tuple):
    h1Score = handType[hand1[0]]
    h2Score = handType[hand2[0]]

    if h1Score == h2Score:
        return compareHandStrings2(hand1[0], hand2[0])
    else:
        return h1Score - h2Score


def processHand(info: str):
    # print(info)

    t = info.split()

    hand = t[0]
    bid = t[1]

    valDict = dict()

    for x in hand:
        if x in valDict.keys():
            valDict[x] = valDict[x] + 1
        else:
            valDict[x] = 1

    # print(valDict.values())
    return (hand, bid, valDict)


def pt1():
    hands = list()

    for x in data:
        hands.append(processHand(x))

    # print(hands)

    handsRanked = sorted(hands, key=cmp_to_key(compareHands), reverse=False)

    # print(handsRanked)

    # for x in range(len(handsRanked)):
    #     print(f"{x+1} {handsRanked[x][0]} {handsRanked[x][1]}")

    ans = 0

    for x in range(len(handsRanked)):
        bid = int(handsRanked[x][1])
        # print(f"{str(bid)} * {x + 1}")
        ans += bid * (x + 1)

    print(ans)
    return ans


def pt2():
    hands = list()

    for x in data:
        hands.append(processHand(x))

    # print(hands)

    populatehandTypeDict(hands)
    # print(handType)

    handsRanked = sorted(hands, key=cmp_to_key(compareHands2), reverse=False)

    # print(handsRanked)

    # for x in range(len(handsRanked)):
    #     print(f"{x+1} {handsRanked[x][0]} {handsRanked[x][1]}")

    ans = 0

    for x in range(len(handsRanked)):
        bid = int(handsRanked[x][1])
        # print(f"{str(bid)} * {x + 1}")
        ans += bid * (x + 1)

    print(ans)
    return ans


print("Part 1 Answer:")
pt1()
print("Part 2 Answer:")
pt2()
