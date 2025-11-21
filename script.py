#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Temperature Converter"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

if __name__ == "__main__":
    temp_c = 33
    temp_f = celsius_to_fahrenheit(temp_c)
    temp_k = celsius_to_kelvin(temp_c)
    
    print(f"{temp_c}°C = {temp_f:.2f}°F")
    print(f"{temp_c}°C = {temp_k:.2f}K")
