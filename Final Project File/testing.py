import DobotDllType as dType

# Load the Dobot API
api = dType.load()

# Connect to the Dobot
state = dType.ConnectDobot(api, "", 115200)
if state[0] != dType.DobotConnect.DobotConnect_NoError:
    print("Failed to connect to Dobot.")
    exit()

# Set velocity and acceleration
dType.SetPTPCommonParams(api, 100, 100)

# Define the Home and Pick Positions
home_position = [205.8110, -5.2308, 136.4629, -1.4559]   # [X, Y, Z, R]
pick_approach_position = [43.4997, -245.2267, -7.8068, -79.9412]   # [X, Y, Z, R]
pick_position = [30.5288, -242.5614, -58.7110, -82.8265]  # [X, Y, Z, R]
place_approach_position = [164.4465, -154.0132, 93.7008, -84.8912]   # [X, Y, Z, R]
place_position = [171.2271, -154.0132, 4.2309, -82.8265]  # [X, Y, Z, R]


# Move to the home Position
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, *home_position)
dType.dSleep(2000)  # Wait for 2 seconds to ensure the Dobot reaches the pick position

# Move to the pick_approach_position
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, *pick_approach_position)
dType.dSleep(2000)  # Wait for 2 seconds to ensure the Dobot reaches the pick position

# Move to the pick Position
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, *pick_position)
dType.dSleep(2000)  # Wait for 2 seconds to ensure the Dobot reaches the pick position

# Activate the suction cup to pick the object
dType.SetEndEffectorSuctionCup(api, True, True)
dType.dSleep(2000)

# Move to the pick_approach_position
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, *pick_approach_position)
dType.dSleep(2000)  # Wait for 2 seconds to ensure the Dobot reaches the pick position

# Move to the place_approach_position
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, *place_approach_position)
dType.dSleep(2000)  # Wait for 2 seconds to ensure the Dobot reaches the pick position

# Move to the place Position
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, *place_position)
dType.dSleep(2000)  # Wait for 2 seconds to ensure the Dobot reaches the pick position

# Activate the suction cup to pick the object
dType.SetEndEffectorSuctionCup(api, False, False)
dType.dSleep(2000) 

# Move to the home Position
dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, *home_position)
dType.dSleep(2000)  # Wait for 2 seconds to ensure the Dobot reaches the pick position


# Disconnect the Dobot
dType.DisconnectDobot(api)
