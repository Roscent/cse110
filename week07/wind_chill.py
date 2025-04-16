def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return celsius * (9/5) + 32

def calculate_wind_chill(temp_f, wind_speed):
    """Calculate wind chill using the National Weather Service formula"""
    return 35.74 + (0.6215 * temp_f) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp_f * (wind_speed ** 0.16))

def main():
    temp = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").upper()
    
    if unit == 'C':
        temp_f = celsius_to_fahrenheit(temp)
        print(f"At temperature {temp_f:.1f}F, and wind speed 5 mph, the windchill is: {calculate_wind_chill(temp_f, 5):.2f}F")
    else:
        temp_f = temp
        print(f"At temperature {temp_f:.1f}F, and wind speed 5 mph, the windchill is: {calculate_wind_chill(temp_f, 5):.2f}F")
    
    
    for wind_speed in range(10, 61, 5):
        wind_chill = calculate_wind_chill(temp_f, wind_speed)
        print(f"At temperature {temp_f:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

if __name__ == "__main__":
    main()