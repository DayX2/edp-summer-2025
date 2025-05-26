messages = []

print(messages)

messages.append("Hello")
messages.append("How R U")


for message in messages:
    print(message)

x = messages.pop(0)
print(messages, x)

messages.pop(0)
print(messages)

class Sensor:
    def __init__(self, name, id, sensor_type, animal):
        self.name = name
        self.id = id
        self.sensor_type = sensor_type
        self.animal = animal

s1 = Sensor("Temp", 215, "Electronic", "Tiger")