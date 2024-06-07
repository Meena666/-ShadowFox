def calculate_speed(distance,time_minutes):
    time_seconds = time_minutes*60
    speed = distance/time_seconds
    return speed
distance = 490
time_minutes = 7
speed = calculate_speed(distance,time_minutes)
print(f" The Speed is {int(speed)} meters per second")
