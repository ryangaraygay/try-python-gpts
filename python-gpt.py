from collections import deque
import random
import time

# Constants
WINDOW_SIZE = 10  # Size of the moving average window
THRESHOLD = 5  # Threshold for change detection

# Simulated data source: generates random temperature readings
def data_source():
    while True:
        yield random.normalvariate(20, 5)  # Mean = 20, SD = 5
        time.sleep(1)  # Simulate sensor delay

# Moving average filter
def moving_average(window):
    def inner(new_value):
        window.append(new_value)
        if len(window) > WINDOW_SIZE:
            window.popleft()
        return sum(window) / len(window)
    return inner

# Detect significant changes
def detect_change(last_value, current_value, threshold):
    if abs(current_value - last_value) > threshold:
        return True
    return False

# Logging function
def log_event(message):
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

# Main function to process the data stream
def process_data_stream():
    data_gen = data_source()
    avg_calculator = moving_average(deque())
    last_stable_value = next(data_gen)  # Initialize with the first data point
    
    for data in data_gen:
        current_avg = avg_calculator(data)
        if detect_change(last_stable_value, current_avg, THRESHOLD):
            last_stable_value = current_avg  # Update the last stable value
            log_event(f"Significant change detected: {current_avg:.2f}")
        else:
            log_event(f"Current average: {current_avg:.2f}")

# Uncomment below line to run the simulation in an appropriate environment
# process_data_stream()
def main():
    process_data_stream()

if __name__ == '__main__':
    main()
