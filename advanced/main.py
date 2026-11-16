mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

while True:
    destination = input("Please enter the destination: ")
    if destination.strip().lower().title() in mission_route:
        print(f"{destination} is in the mission route.\n")
        print(f"{destination} is {mission_route.index(destination.strip().lower().title())} stops away from the start.\n")
        print(f"{destination} is {len(mission_route) - mission_route.index(destination.strip().lower().title()) - 1} stops away from the end.\n")
        if len(mission_route) - mission_route.index(destination.strip().lower().title()) - 1 != 0:
            print(f"The next stop is {mission_route[mission_route.index(destination.strip().lower().title()) + 1]}\n")
        else:
            print("This is the final stop.\n")
    else:
        print(f"{destination} is not in the mission route.\n")
