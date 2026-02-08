import time
state = "off"
while True:
    switches = ["left_switch", "right_switch", "left_switch_sec"]
    left_switch = "emergency light"
    left_switch_sec = "main light"
    right_switch = "OFF all light"
    answer = input(f"R'You press {left_switch}?").lower()
    if answer == "on" and state == "off":
        state = "emergency"
        if state == "emergency":
           print(f"{left_switch} is ON")
    elif answer == "off" and state == "off":
        state = "off"
        if state == "off":
           print(f"{left_switch} is OFF")
    time.sleep(10)
    input(f"{left_switch_sec}")
    print(f"{left_switch_sec} is ON")
    time.sleep(1)
    switches = ["left_switch", "right_switch", "left_switch_sec"]
    answer = input(f"R'you press {right_switch}?").lower()
    state = "main"
    if answer == "off" and state == "main":
        state = "main"
        if state == "main":
            print("Light is ON")
    elif answer == "on" and state == "main":
        state = "off"
        if state == "off":
            print(f"{right_switch}")
    break
