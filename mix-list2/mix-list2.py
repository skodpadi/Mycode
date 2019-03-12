#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
print(proto[1])
proto.extend('dns') ## this line will add 'd', 'n' and 's' to the end of our list
print(proto)

proto.append('dns')
proto.append('dns')
proto.append('dns'*2)
print(proto)

proto2 = [22,80,443,53]
proto.extend(proto2)
print(proto)
protoa.append(proto2)
print(protoa)

#deleting the second element of the list

del proto[1]
print(proto)