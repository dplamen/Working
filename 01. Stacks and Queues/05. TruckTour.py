from collections import deque

n = int(input())
pumps = []
for i in range(n):
    petrol, distance = input().split()
    pumps.append((int(petrol), int(distance)))

for k in range(n):
    pump_set = deque(pumps)
    pump_set.rotate(-k)
    power = 0
    while pump_set:
        petrol, distance = pump_set.popleft()
        if power + petrol >= distance:
            power += petrol - distance
            continue
        break
    if not pump_set:
        print(k)
        break
