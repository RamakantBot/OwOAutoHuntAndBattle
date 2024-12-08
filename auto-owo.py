import time
import random
import pyautogui
from datetime import datetime

# --------------------------------------------------------------------------------------------------------------------------

# Default cooldown times in seconds
HUNT_COOLDOWN = random.uniform(15, 16)
BATTLE_COOLDOWN = random.uniform(15, 16)
PRAY_COOLDOWN = random.uniform(300, 330)
RANDOM_COMMAND_COOLDOWN = random.uniform(120, 240)  # Cooldown for random commands

# Last execution times
last_hunt_time = 0
last_battle_time = 0
last_pray_time = 0
last_custom_time = 0
last_random_command_time = 0

# List of random OwO commands
random_commands = [
    "inv", "cash", "z", "q", "cl","z d", "w", "my", "team", "top", "top 25 c"
]

# --------------------------------------------------------------------------------------------------------------------------

print("\nStarting OwO bot automation. Press Ctrl+C to stop.\n")
time.sleep(1)
# Get user-defined prefix or use default
user_prefix = input("Enter the bot prefix (optional): ") or 'owo '

# Ask if the user wants to add the default pray command
add_pray_command = input("Do you want to add the 'pray' command? (yes/no, default is yes): ").strip().lower() or 'yes'
if add_pray_command in ['yes', 'y']:
    # Use the default pray command cooldown
    custom_pray_cooldown = PRAY_COOLDOWN
else:
    custom_pray_cooldown = None
    print("No pray command will be added.\n")

# Ask if the user wants to add a custom command
while True:
    add_custom_command = input("Do you want to add a custom command? (yes/no): ").strip().lower()
    if add_custom_command in ['yes', 'y']:
        # Get custom command and cooldown from the user
        custom_command = input("Enter a custom command: ")
        custom_cooldown = input(f"Enter the delay for '{custom_command}' in seconds (default is 60): ")

        # Convert custom cooldown to integer or use default
        custom_cooldown = int(custom_cooldown) if custom_cooldown.isdigit() else 60
        break
    elif add_custom_command in ['no', 'n']:
        custom_command = None
        custom_cooldown = None
        print("No custom command will be added.\n")
        break
    else:
        print("Invalid input. Please enter (yes/no): ")

# --------------------------------------------------------------------------------------------------------------------------

def main():
    global last_hunt_time, last_battle_time, last_pray_time, last_custom_time, last_random_command_time

    start_time = time.time()  # Record the start time

    # Countdown timer for 10 seconds
    for i in range(10, 0, -1):
        print(f"Starting in {i} seconds...", end='\r')
        time.sleep(1)
    print("\nStarting now!\n")
    
    while True:
        current_time = time.time()

        # Check if we can perform the hunt command
        if current_time - last_hunt_time >= HUNT_COOLDOWN:
            hunt(start_time)
            last_hunt_time = current_time
            time.sleep(random.uniform(1, 4))  # Random delay up to 3 seconds

        # Check if we can perform the battle command
        if current_time - last_battle_time >= BATTLE_COOLDOWN:
            # Ensure at least 6 seconds have passed since the last hunt
            if current_time - last_hunt_time >= 6:
                battle(start_time)
                last_battle_time = current_time
                time.sleep(random.uniform(1, 4))  # Random delay up to 3 seconds

        # Check if we can perform the pray command
        if custom_pray_cooldown and current_time - last_pray_time >= custom_pray_cooldown:
            pray(start_time)
            last_pray_time = current_time
            time.sleep(random.uniform(1, 4))  # Random delay up to 3 seconds

        # Check if we can perform the custom command
        if custom_command and current_time - last_custom_time >= custom_cooldown:
            custom(start_time)
            last_custom_time = current_time
            time.sleep(random.uniform(1, 4))  # Random delay up to 3 seconds

        # Check if we can perform a random command
        if current_time - last_random_command_time >= RANDOM_COMMAND_COOLDOWN:
            random_command(start_time)
            last_random_command_time = current_time
            time.sleep(random.uniform(1, 4))  # Random delay up to 3 seconds

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

def random_command(start_time):
    command = random.choice(random_commands)  # Select a random command from the list
    pyautogui.write(f"{user_prefix}{command}", interval=0.2)
    pyautogui.press('enter')
    print(f"{get_relative_time(start_time)} - Executed: {command}!")

# --------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()