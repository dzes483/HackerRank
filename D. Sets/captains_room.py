group_size = int(input())
total_rooms = [int(i) for i in (input().split())]

unique_rooms = set()
group_rooms = set()

for room_num in total_rooms:
    if room_num not in unique_rooms:
        unique_rooms.add(room_num)
    else:
        group_rooms.add(room_num)

captains_room = unique_rooms.difference(group_rooms)

print(str(captains_room)[1:-1])
