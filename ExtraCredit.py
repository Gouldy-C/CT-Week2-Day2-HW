player_lvl = 10

enemies = [
    ['Slimes', 3],
    ['Goblins', 5],
    ['Skeleton', 8],
    ['Zombie', 9],
    ['Dragon', 25],
    ['Troll', 20],
    ['Giant', 20],
    ['Vampire', 15],
    ['Ghost', 15],
    ['Wolves', 1],
    ['Zombies', 14],
]

test_lst = [1,11,14,5,8,9]

def enemies_within(lst, lvl):
    return [n for n in lst if n < lvl]

print(enemies_within([n[1] for n in enemies], player_lvl))

print(enemies_within(test_lst, player_lvl))


l_1 = [1, 2, 3, 4, 5, 6]
l_2 = [3, 4, 5, 6, 7, 8, 10]
max_inventory_size = 8

def inventory_max_max(lst1, lst2, size):
    return sorted(lst1 + lst2, reverse = True)[:size]

print(inventory_max_max(l_1, l_2, max_inventory_size))