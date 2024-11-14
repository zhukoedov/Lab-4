ITEMS = {
    'r': {'w': 3, 'points': 25},  # 1
    'p': {'w': 2, 'points': 15},  # 2
    'a': {'w': 2, 'points': 15},  # 3
    'm': {'w': 2, 'points': 20},  # 4
    'i': {'w': 1, 'points': 5},   # 5
    'k': {'w': 1, 'points': 15},  # 6
    'x': {'w': 3, 'points': 20},  # 7
    't': {'w': 1, 'points': 25},  # 8
    'f': {'w': 1, 'points': 15},  # 9
    'd': {'w': 1, 'points': 10},  # 10
    's': {'w': 2, 'points': 20},  # 11
    'c': {'w': 2, 'points': 20}   # 12
}

EXTRA_POINTS = 15
LACK_OF_ALL_ITEMS = 0

for x in ITEMS.values():
    LACK_OF_ALL_ITEMS -= x['points']


def itd(i):  # index to dict-index
    if i == 1:
        return ('r')
    if i == 2:
        return ('p')
    if i == 3:
        return ('a')
    if i == 4:
        return ('m')
    if i == 5:
        return ('i')
    if i == 6:
        return ('k')
    if i == 7:
        return ('x')
    if i == 8:
        return ('t')
    if i == 9:
        return ('f')
    if i == 10:
        return ('d')
    if i == 11:
        return ('s')
    if i == 12:
        return ('c')
    print("-------INTRUSION ALERT!!! RED SPY IS IN THE BASE!!!-------")


def compare(table, line, slot):
    ans = 0
    if slot < ITEMS[itd(line)]['w']:
        ans = table[line - 1][slot]
    else:
        ans = max(
            table[line - 1][slot],
            table[line - 1][slot - ITEMS[itd(line)]['w']] +
            2 * ITEMS[itd(line)]['points']
        )
    return ans


def compare_back(table, line, slot):
    list_of_items = []
    while line != 0:
        if table[line][slot] != table[line - 1][slot]:
            list_of_items.append(line)
            slot = slot - ITEMS[itd(line)]['w']
        line -= 1
    return list_of_items


def collected_to_gui(collected):
    first_lane = []
    second_lane = []
    for x in collected:  # можно было поставить букву-ключ: число-значение и написать всего 3 условия вместо 8, но мне лень
        if x == 'r':
            if len(first_lane) <= 1:
                first_lane.append('r')
                first_lane.append('r')
                first_lane.append('r')
            else:
                second_lane.append('r')
                second_lane.append('r')
                second_lane.append('r')
        if x == 'x':
            if len(first_lane) <= 1:
                first_lane.append('x')
                first_lane.append('x')
                first_lane.append('x')
            else:
                second_lane.append('x')
                second_lane.append('x')
                second_lane.append('x')
        if x == 'p':
            if len(first_lane) <= 2:
                first_lane.append('p')
                first_lane.append('p')
            else:
                second_lane.append('p')
                second_lane.append('p')
        if x == 'a':
            if len(first_lane) <= 2:
                first_lane.append('a')
                first_lane.append('a')
            else:
                second_lane.append('a')
                second_lane.append('a')
        if x == 'm':
            if len(first_lane) <= 2:
                first_lane.append('m')
                first_lane.append('m')
            else:
                second_lane.append('m')
                second_lane.append('m')
        if x == 's':
            if len(first_lane) <= 2:
                first_lane.append('s')
                first_lane.append('s')
            else:
                second_lane.append('s')
                second_lane.append('s')
        if x == 'c':
            if len(first_lane) <= 2:
                first_lane.append('c')
                first_lane.append('c')
            else:
                second_lane.append('c')
                second_lane.append('c')
        if x == 'i':
            if len(first_lane) <= 3:
                first_lane.append('i')
            else:
                second_lane.append('i')
        if x == 'k':
            if len(first_lane) <= 3:
                first_lane.append('k')
            else:
                second_lane.append('k')
        if x == 't':
            if len(first_lane) <= 3:
                first_lane.append('t')
            else:
                second_lane.append('t')
        if x == 'f':
            if len(first_lane) <= 3:
                first_lane.append('f')
            else:
                second_lane.append('f')
        if x == 'd':
            if len(first_lane) <= 3:
                first_lane.append('d')
            else:
                second_lane.append('d')
    gui_first_lane = ""
    gui_second_lane = ""
    for x in first_lane:
        gui_first_lane += f'[{x}],'
    gui_first_lane = gui_first_lane[:len(gui_first_lane) - 1]
    print(gui_first_lane)

    for x in second_lane:
        gui_second_lane += f'[{x}],'
    gui_second_lane = gui_second_lane[:len(gui_second_lane) - 1]
    print(gui_second_lane)


def zomdbe_apocalypsis_ver7():
    inventory = 8  # 2x4 inventory
    table = [[LACK_OF_ALL_ITEMS for c in range(
        inventory + 1)] for _ in range(len(ITEMS) + 1)]
    # build
    for line in range(1, len(ITEMS) + 1):
        for slot in range(1, inventory + 1):
            table[line][slot] = compare(table, line, slot)
    # print(table)

    # backup
    list_of_items = compare_back(table, len(ITEMS), inventory)
    # print(list_of_items)

    collected = [itd(x) for x in list_of_items]
    # print(collected)
    collected_to_gui(collected)
    print(f"Очков выживания: {table[len(ITEMS)][inventory] + EXTRA_POINTS}")


if __name__ == "__main__":
    zomdbe_apocalypsis_ver7()
