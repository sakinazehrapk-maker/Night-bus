import time

def print_header(location, clock_time):
    print("\n" + "=" * 40)
    print("╔══════════════════════════════════════╗")
    print("║              NIGHT BUS               ║")
    print("║             Route 17-B               ║")
    print("╚══════════════════════════════════════╝")
    print(f"Time: {clock_time}  |  Location: {location}")
    print("=" * 40 + "\n")
phone_battery = 87
passengers = [
    "Ayesha",
    "Uncle Rashid",
    "Sameer",
    "Hina",
    "Bilal",
    "Mariam",
    "Unknown Man"
]
hina_missing = False

print_header("University Road", "11:38 PM")
print("It's raining heavily outside.")
print("You board the last bus home, shaking the water off your coat.")
print("The bus is quiet except for the steady low hum of the engine.\n")

print("Passengers on board:")
for p in passengers:
    print(f" - {p}")
input("\nPress ENTER to sit down near the back...")

stop_active = True
while stop_active:
    print_header("University Road", "11:38 PM")
    print("What do you want to do?")
    print("[1] Look around")
    print("[2] Talk to someone")
    print("[3] Check your phone")
    print("[4] Look out the window")
    print("[5] Sit quietly")
    print("[6] Wait for the next stop")
    
    choice = input("\n> ")

    if choice == "1":
        print("\nYou scan the aisle. Seven passengers scattered in silence.")
        print("A girl in seat 2 (Ayesha) keeps checking her phone nervously.")
    elif choice == "2":
        print("\nYou open your mouth to speak, but no one looks up.")
        print("Maybe wait until you have a reason to talk.")
    elif choice == "3":
        phone_battery -= 1
        print(f"\nYou pull out your phone. Battery: {phone_battery}%")
        print("Signal: 1 Bar. No new messages.")
    elif choice == "4":
        print("\nRain streaks down the dirty window glass, blurring the streetlights.")
    elif choice == "5":
        print("\nYou close your eyes for a moment, letting the bus vibration rest your eyes.")
    elif choice == "6":
        print("\nThe bus hums as it pulls away from the curb and drives into the night...")
        stop_active = False
    else:
        print("\nInvalid choice. Pick a number from 1 to 6.")
    
    if stop_active:
        input("\nPress ENTER to continue...")

time.sleep(1)
print_header("Market Stop", "11:51 PM")

print("*doors open with a hiss*")
print("Cold air blows into the bus. Someone gets off, shoes splashing in a puddle.")
print("The doors hiss shut, and the driver immediately pulls away.\n")

if "Hina" in passengers:
    passengers.remove("Hina")
    hina_missing = True

stop_active = True
while stop_active:
    print_header("Market Stop", "11:52 PM")
    print("What do you want to do?")
    print("[1] Check the passengers around you")
    print("[2] Ask the driver who got off")
    print("[3] Check your phone")
    print("[4] Look out the rear window")
    print("[5] Wait for the next stop")
    
    choice = input("\n> ")

    if choice == "1":
        print("\nYou look toward the middle of the bus.")
        print("Seat 8 is completely empty.")
        print("Didn't a young woman (Hina) sit there just a minute ago?")
    elif choice == "2":
        print("\nYou call out to the front: 'Excuse me, who just got off?'")
        print("The driver doesn't turn around. 'Whoever bought a ticket,' he mutters.")
    elif choice == "3":
        phone_battery -= 2
        print(f"\nBattery: {phone_battery}%. Still 1 bar.")
        print("An unread broadcast notification: 'WEATHER WARNING: Flash flooding near Old Bridge.'")
    elif choice == "4":
        print("\nYou look out the back window. The Market stop fades into dark rain.")
        print("You don't see anyone standing under the bus stop shelter.")
    elif choice == "5":
        print("\nThe bus picks up speed, heading toward the darker outskirts of town...")
        stop_active = False
    else:
        print("\nInvalid choice. Pick a number from 1 to 5.")
    
    if stop_active:
        input("\nPress ENTER to continue...")
