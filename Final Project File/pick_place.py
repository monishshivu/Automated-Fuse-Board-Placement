import DobotDllType as dType
import time

# Load the Dobot API
api = dType.load()

# Connect to the Dobot
state = dType.ConnectDobot(api, "", 115200)
if state[0] != dType.DobotConnect.DobotConnect_NoError:
    print("Failed to connect to Dobot.")
    exit()

# Set velocity and acceleration for the Dobot
dType.SetPTPCommonParams(api, 100, 100)

# Define the Home and Pick Positions
home_position = [205.8110, -5.2308, 136.4629, -1.4559]   # [X, Y, Z, R]
pick_approach_position = [43.4997, -245.2267, -7.8068, -79.9412]   # [X, Y, Z, R]
pick_position = [30.5288, -242.5614, -58.7110, -82.8265]  # [X, Y, Z, R]
place_approach_position = [164.4465, -154.0132, 93.7008, -84.8912]   # [X, Y, Z, R]
place_position = [171.2271, -154.0132, 4.2309, -82.8265]  # [X, Y, Z, R]

# Enable the infrared sensor on GP4
infraredPort = 2  # GP4 port is represented by 2 as per your system
version = 1  # Assuming version 0 for this sensor
dType.SetInfraredSensor(api, True, infraredPort, version)

try:
    while True:
        # Read the sensor value from GP4
        sensor_value = dType.GetInfraredSensor(api, infraredPort)

        # Print the sensor status (0 means object detected, 1 means no object)
        print(f"Sensor Status: {sensor_value[0]}")

        # Check the sensor value and control the suction accordingly
        if sensor_value[0] == 1:
            print("Object detected! Starting pick-up sequence.")

            # Move Dobot to home position
            print("Moving Dobot to home position.")
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, *home_position)
            dType.dSleep(2000)  # Wait for Dobot to reach the home position

            # Move Dobot to pick_approach_position
            print("Moving Dobot to pick_approach_position.")
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, *pick_approach_position)
            dType.dSleep(2000)  # Wait for Dobot to reach the approach position

            # Move Dobot to pick position
            print("Moving Dobot to pick position.")
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, *pick_position)
            dType.dSleep(2000)  # Wait for Dobot to reach the pick position

            # Activate suction cup to pick the object
            print("Activating suction cup to pick the object.")
            dType.SetEndEffectorSuctionCup(api, True, True)
            dType.dSleep(2000)  # Wait for the suction to activate

             # Move Dobot to pick_approach_position
            print("Moving Dobot to pick_approach_position.")
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, *pick_approach_position)
            dType.dSleep(2000)  # Wait for Dobot to reach the approach position

            # Move Dobot to place_approach_position
            print("Moving Dobot to place_approach_position.")
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, *place_approach_position)
            dType.dSleep(2000)  # Wait for Dobot to reach the approach position

            # Move Dobot to place_position
            print("Moving Dobot to place position.")
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, *place_position)
            dType.dSleep(2000)  # Wait for Dobot to reach the place position

            # Deactivate suction cup to release the object
            print("Deactivating suction cup.")
            dType.SetEndEffectorSuctionCup(api, False, False)
            dType.dSleep(2000)  # Wait for the suction to deactivate

            # Move Dobot to home position again
            print("Moving Dobot to home position.")
            dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, *home_position)
            dType.dSleep(2000)  # Wait for Dobot to reach the home position

            print("Pick-and-place sequence completed.")
        else:
            print("No object detected. Waiting...")
        time.sleep(1)  # Check the sensor every second

finally:
    # Disconnect the Dobot when the script is stopped or exited
    dType.DisconnectDobot(api)
    print("Dobot operation completed.")
