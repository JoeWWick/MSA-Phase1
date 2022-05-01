fact = "The Moon has no atmosphere."
twofacts = fact + " No sound can be heard on the Moon."
print(twofacts)

print("temperatures and facts about the moon".title())

temperatures = """Daylight: 260 F 
Nighttime: -280 F"""
print(temperatures .split())
print(temperatures .split('\n'))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
print(temperatures.find("Moon"))


mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
     if item.isnumeric():
        print(item)

print("""Both sides of the %s get the same amount of sunlight,
but only one side is seen from %s because
the %s rotates around its own axis when it orbits %s. \n\n""" % ("Moon", "Earth", "Moon", "Earth"))

mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} 
you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))


