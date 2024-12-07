import time
import random
import pyautogui
from datetime import datetime

# --------------------------------------------------------------------------------------------------------------------------

# Default cooldown times in seconds
HUNT_COOLDOWN = 15
BATTLE_COOLDOWN = 15
PRAY_COOLDOWN = 300

# Last execution times
last_hunt_time = 0
last_battle_time = 0
last_pray_time = 0
last_custom_time = 0


# --------------------------------------------------------------------------------------------------------------------------

print("\nStarting OwO bot automation. Press Ctrl+C to stop.\n")

# Get user-defined prefix or use default
user_prefix = input("Enter the bot prefix (optional): ") or 'owo '

# Ask if the user wants to add a custom command
while True:
    add_custom_command = input("Do you want to add a custom command? (yes/no): ").strip().lower()
    if add_custom_command in ['yes', 'y']:
        # Get custom command and cooldown from the user
        custom_command = input("Enter a custom command (e.g., zoo, pets, wepons, daily): ")
        custom_cooldown = input(f"Enter the dealy for '{custom_command}' in seconds (default is 69): ")

        # Convert custom cooldown to integer or use default
        custom_cooldown = int(custom_cooldown) if custom_cooldown.isdigit() else 69
        break
    elif add_custom_command in ['no', 'n']:
        custom_command = None
        custom_cooldown = None
        print("No custom command will be added.")
        break
    else:
        print("Invalid input. Please enter (yes/no): ")


# --------------------------------------------------------------------------------------------------------------------------

def main():
    global last_hunt_time, last_battle_time, last_pray_time, last_custom_time

    start_time = time.time()  # Record the start time
    # print("\nStarting OwO bot automation. Press Ctrl+C to stop.\n")

    # Countdown timer for 15 seconds
    for i in range(15, 0, -1):
        print(f"Starting in {i} seconds...", end='\r')
        time.sleep(1)
    print("\nStarting now!\n")
    
    while True:
        current_time = time.time()

        # Check if we can perform the hunt command
        if current_time - last_hunt_time >= HUNT_COOLDOWN:
            hunt(start_time)
            last_hunt_time = current_time
            time.sleep(random.uniform(0, 3))  # Random delay up to 3 seconds

        # Check if we can perform the battle command
        if current_time - last_battle_time >= BATTLE_COOLDOWN:
            # Ensure at least 6 seconds have passed since the last hunt
            if current_time - last_hunt_time >= 6:
                battle(start_time)
                last_battle_time = current_time
                time.sleep(random.uniform(0, 3))  # Random delay up to 3 seconds

        # Check if we can perform the pray command
        if current_time - last_pray_time >= PRAY_COOLDOWN:
            pray(start_time)
            last_pray_time = current_time
            time.sleep(random.uniform(0, 3))  # Random delay up to 3 seconds

        # Check if we can perform the custom command
        if custom_command and current_time - last_custom_time >= custom_cooldown:
            custom(start_time)
            last_custom_time = current_time
            time.sleep(random.uniform(0, 3))  # Random delay up to 3 seconds

        # Wait for a short time before checking again
        time.sleep(1)  # Check every second

# --------------------------------------------------------------------------------------------------------------------------

def get_relative_time(start_time):
    elapsed_time = time.time() - start_time
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}:{milliseconds:03}"


# --------------------------------------------------------------------------------------------------------------------------

def hunt(start_time):
    pyautogui.write(f"{user_prefix}h", interval=0.2)
    pyautogui.press('enter')
    print(f"{get_relative_time(start_time)} - Hunted!")

def battle(start_time):
    pyautogui.write(f"{user_prefix}b", interval=0.2)
    pyautogui.press('enter')
    print(f"{get_relative_time(start_time)} - Battled!")

def pray(start_time):
    pyautogui.write(f"{user_prefix}pray", interval=0.2)
    pyautogui.press('enter')
    print(f"{get_relative_time(start_time)} - Prayed!")

def custom(start_time):
    pyautogui.write(f"{user_prefix}{custom_command}", interval=0.2)
    pyautogui.press('enter')
    print(f"{get_relative_time(start_time)} - Executed: {custom_command}!")


# --------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()


