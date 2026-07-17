import math
import time
import config


def calculate_speed(previous_position, current_position, previous_time):

    if previous_position is None:
        return 0, time.time()


    current_time = time.time()


    time_difference = current_time - previous_time


    pixel_distance = math.sqrt(
        (current_position[0] - previous_position[0]) ** 2 +
        (current_position[1] - previous_position[1]) ** 2
    )


    # Convert pixels to metres
    metres = pixel_distance / config.PIXELS_PER_METRE


    # metres per second
    metres_per_second = metres / time_difference


    # Convert to km/h
    kmh = metres_per_second * 3.6


    return kmh, current_time