#!/usr/bin/env python3
easy= ["science", "turbo", ["goggles", "eyes"], "nothing"]


medium= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


hard= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


print(f"My {easy[2][1]}! The {medium[2][1]} do {hard[-1]}")

