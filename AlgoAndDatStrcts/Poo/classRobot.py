class RobotBluePrint:

    milk = 903

    def __init__(self, color = "", weight =0, batteryLevel = 0):
        print("The cookie its ready bitch" )
        self.color = color
        self.weight = weight
        self.batteryLevel = batteryLevel

    
    def enter_charge_mode(self):
        self.batteryLevel += 1



robot_a = RobotBluePrint()

robot_b = RobotBluePrint("red", 12)


robot_a.weight = 15
robot_a.color = "Red"

print(robot_a.weight)
print(robot_a.color)

print(robot_b.weight)
print(robot_b.color)
print(robot_b.milk)
print(robot_b.batteryLevel)
robot_b.enter_charge_mode()
print(robot_b.batteryLevel)
