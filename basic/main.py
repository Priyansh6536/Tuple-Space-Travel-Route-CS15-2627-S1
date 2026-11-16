mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)
print(f"The first destination in the mission route is {mission_route[0]}\n")
print(f"The last destination in the mission route is {mission_route[5]}\n")
print(f"The length of the list is {len(mission_route)}\n")
for i in range(len(mission_route)):
    print(mission_route[i])
print("")
if "Europa" in mission_route:
    print("Europa is in the mission route")