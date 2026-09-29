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
clues = []
accused_person = None

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

print_header("Approaching Old Bridge", "12:05 AM")
print("The streetlights become sparse. The road gets rougher.")
print("Uncle Rashid turns around in seat 4 and looks straight at you.\n")
print("Uncle Rashid: 'Son... did you see anyone get off back at Market?'")

act3_active = True
while act3_active:
    print("\nWhat do you do?")
    print("[1] 'No one got off. Seat 8 was just suddenly empty.'")
    print("[2] 'Why are you asking me?'")
    print("[3] Confront Sameer in seat 6")
    print("[4] Look around the bus seats")
    print("[5] Continue waiting in silence")
    
    choice = input("\n> ")

    if choice == "1":
        print("\nUncle Rashid frowns, lowering his voice.")
        print("Rashid: 'I thought so too. But Mariam over there claims Hina got off.'")
        print("He nods toward Mariam (Seat 12), who sits staring straight ahead.")
        if "Mariam contradicted Rashid" not in clues:
            clues.append("Mariam claims Hina left; Rashid says no one did")
    elif choice == "2":
        print("\nRashid gives a soft, nervous chuckle.")
        print("Rashid: 'Just checking if my old eyes are playing tricks on me.'")
    elif choice == "3":
        print("\nYou step toward Sameer. He has his earphones in, tapping his foot rapidly.")
        print("You pull one earphone aside: 'Did you know the girl in seat 8?'")
        print("Sameer flinches. 'I don't know her. I'm just trying to get home.'")
        print("As he reaches into his coat, his screen lights up with a message:")
        print("  [Hina: 'Are you still coming tonight?']")
        if "Sameer lied about Hina" not in clues:
            clues.append("Sameer claimed not to know Hina, but has texts from her")
    elif choice == "4":
        print("\nYou glance around. Ayesha in seat 2 has moved to seat 5.")
        print("You ask her: 'Didn't you sit near the front earlier?'")
        print("Ayesha looks down at her phone: 'No. I've been in seat 5 the whole time.'")
        print("Rashid speaks up from across the aisle: 'Yes, she was at the front.'")
        if "Ayesha seat change" not in clues:
            clues.append("Ayesha shifted seats and denied it")
    elif choice == "5":
        print("\nThe bus rattles over the expansion joints of Old Bridge.")
        print("No one speaks. The silence grows heavier.")
        act3_active = False
    else:
        print("\nInvalid choice.")

    if act3_active:
        input("\nPress ENTER to continue...")
time.sleep(1)
print_header("Blackwood Tunnel", "12:17 AM")

print("The bus plunges into a long, unlit mountain tunnel.")
print("The overhead lights flicker twice... then go completely pitch dark.")
print("The engine hums loudly inside the narrow space.\n")

print("*thud*")
print("*a quiet gasp*")
print("*footsteps shuffling in the dark*\n")

time.sleep(2)
print("The emergency lights buzz back on with a dull yellow glow.")

if "Bilal" in passengers:
    passengers.remove("Bilal")

print("You look down the aisle.")
print("Bilal's seat (Seat 10) is empty. His black backpack sits abandoned on the floor.")

act4_active = True
while act4_active:
    print_header("Blackwood Tunnel Exit", "12:20 AM")
    print("What do you want to do?")
    print("[1] Inspect Bilal's backpack")
    print("[2] Talk to the Unknown Man in the back")
    print("[3] Check your observations")
    print("[4] Call out the driver")
    print("[5] Move on")

    choice = input("\n> ")

    if choice == "1":
        print("\nYou open Bilal's backpack.")
        print("Inside are newspaper clippings from exactly one year ago:")
        print("  'TRAGEDY AT OLD BRIDGE: ROUTE 17-B BUS ACCIDENT CLAIMS LIVES.'")
        print("A handwritten note reads: 'Official report says 6 died. There were 7.'")
        if "Old Bridge crash clippings" not in clues:
            clues.append("Route 17-B crashed 1 year ago; 7th victim omitted from records")
    elif choice == "2":
        print("\nYou walk back to the Unknown Man (Seat 14), hood pulled low.")
        print("You: 'Who are you? What's happening on this bus?'")
        print("Unknown Man: 'I've never seen any of these people before... but neither have you.'")
        print("He looks up slightly. 'Are you sure you boarded this bus tonight?'")
    elif choice == "3":
        print("\n--- YOUR OBSERVATIONS ---")
        for idx, clue in enumerate(clues, 1):
            print(f" [{idx}] {clue}")
        if not clues:
            print(" No major clues recorded yet.")
    elif choice == "4":
        print("\nYou march up to the driver's cabin.")
        print("You: 'Two people are gone! Where are we going? Central was three miles back!'")
        print("The driver doesn't turn his head. 'Route 17-B was cancelled a year ago.'")
        print("You: 'Then why are you driving it?'")
        print("Driver: 'I only carry who's meant to be carried.'")
        if "Cancelled route confirmed" not in clues:
            clues.append("The driver confirmed Route 17-B was cancelled a year ago")
    elif choice == "5":
        print("\nYou return to your seat. The bus surges into the rain again.")
        act4_active = False
    else:
        print("\nInvalid choice.")

    if act4_active:
        input("\nPress ENTER to continue...")