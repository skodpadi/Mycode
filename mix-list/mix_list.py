#!/usr/bin/env python3

# Create list

my_list = ["192.168.0.5", 5060, "UP"]

# Print elements from the list

print("The first item in the list (IP): " + my_list[0])
print("The second item in the list (port): " + str(my_list[1]))
print("The last itwm in the list (state): " + my_list[2])

new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

print("When I ssh into IP addresses {0} or {1} I am unable to ping ports {2}, {3}, or {4}.".format(new_list[3],new_list[4],new_list[0],new_list[1],new_list[2]))

