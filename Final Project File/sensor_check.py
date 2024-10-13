import DobotDllType as dType
import time

# Load the Dobot API
api = dType.load()

# Connect to the Dobot
state = dType.ConnectDobot(api, "", 115200)
if state[0] != dType.DobotConnect.DobotConnect_NoError:
    print("Failed to connect to Dobot.")
    exit()

# Enable the infrared sensor on GP4
infraredPort = 2  # GP4 port is represented by 2 as per your system
version = 1 # Assuming version 0 for this sensor
dType.SetInfraredSensor(api, True, infraredPort, version)

try:
    while True:
        # Read the sensor value from GP4
        sensor_value = dType.GetInfraredSensor(api, infraredPort)

        # Print the sensor status (0 means object detected, 1 means no object)
        print(f"Sensor Status: {sensor_value[0]}")

        # Check the sensor value and control the suction accordingly
        if sensor_value[0] == 1:
            print("Object detected! Activating suction.")
            # Activate suction cup
            dType.SetEndEffectorSuctionCup(api, True, True)
        else:
            print("No object detected. Suction off.")
            # Deactivate suction cup
            dType.SetEndEffectorSuctionCup(api, False, False)

        # Sleep for a short time before checking again
        time.sleep(1)

finally:
    # Disconnect the Dobot when done
    dType.DisconnectDobot(api)
    print("Dobot operation completed.")
