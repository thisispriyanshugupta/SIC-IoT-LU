from gpiozero import OutputDevice
from time import sleep

# Define the GPIO pins connected to the water pump and soil moisture sensor
pump_pin = 17
sensor_pin = 18

# Set up the water pump as an OutputDevice and turn it off initially
pump = OutputDevice(pump_pin)
pump.off()

# Define a function to read the soil moisture level from the sensor
def read_soil_moisture():
    # Read the analog value from the soil moisture sensor
    # Convert the value to a moisture level (0-100%)
    # Return the moisture level as an integer
    return int(100 * (1 - (analog_value / 1023)))

# Define a loop to continuously monitor the soil moisture level and turn the water pump on or off
while True:
    # Read the soil moisture level from the sensor
    moisture_level = read_soil_moisture()

    # Check if the moisture level is below a certain threshold
    if moisture_level < 50:
        # If the moisture level is low, turn on the water pump
        pump.on()
    else:
        # If the moisture level is high enough, turn off the water pump
        pump.off()

    # Sleep for a short time to avoid excessive polling
    sleep(1)
