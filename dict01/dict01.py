#!/usr/bin/env python3

## create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2','vendor': 'cisco'}

## display parts of the dictionary
print(switch['hostname'])
print(switch['ip'])

# Request a fake key
# print(switch['lynx'])

## request a fake key with .get() method
print("Firs test - .get()")
print(switch.get("lynx"))

## second test
print(switch.get("lynx", "The key is in some other castle."))

## third test
print(switch.get("version"))

print(switch)

print("Fourth test - .keys()")
print(switch.keys())
print(switch.values())

print("sixth test - .pop()")
switch.pop("version")

print(switch.keys())
print(switch.values())

switch["password"] = "qwerty"
print(switch.keys())
print(switch.values())