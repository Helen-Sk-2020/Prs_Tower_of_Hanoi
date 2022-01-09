def move(towers, from_tower, dest_tower):
    disk = towers[from_tower].pop()
    towers[dest_tower].append(disk)
    return towers


def print_towers(towers, n):
    for i in range(n, 0, -1):
        for tower in towers:
            if len(tower) >= i:
                print(tower[i - 1], end='  ')
            else:
                print('|', end='  ')
        print()
    print('-------')


def solve_tower_hanoi(towers, n, disks, start_tower, dest_tower, aux_tower):
    if n == 0:
        return
    # Move subproblem of n - 1 disks from start_tower to aux_tower.
    solve_tower_hanoi(towers, n - 1, disks, start_tower, aux_tower, dest_tower)
    # Move disk n to dest_tower.
    move(towers, start_tower, dest_tower)
    print_towers(towers, disks)
    # Move subproblem of n - 1 disk from aux_tower to dest_tower.
    solve_tower_hanoi(towers, n - 1, disks, aux_tower, dest_tower, start_tower)


# Simple example:)
my_towers = [[5, 4, 3, 2, 1], [], []]
my_disks = len(my_towers[0])
print_towers(my_towers, my_disks)
solve_tower_hanoi(my_towers, my_disks, my_disks, 0, 2, 1)
