import math  # Import the math module (though not directly used in this PID controller).
import time  # Import the time module for sleep functionality, used to simulate time passing.

# PID constants (Proportional, Integral, Derivative gains)
kp = 8.0   # Proportional gain: determines the immediate response to the error. Set to 8.0.
ki = 0.5   # Integral gain: helps eliminate steady-state errors over time. Set to 0.5.
kd = 0.5   # Derivative gain: anticipates future errors by considering the rate of change of the current error. Set to 0.5.

# Target temperatures for testing the PID controller
targets = [200]  # A list containing the desired target temperature(s) in degrees Celsius.
current = 10   # The initial current temperature, starting at 10°C.
last_error = 0     # Stores the error from the previous control loop iteration, used for the derivative term.
integral_sum = 0  # Accumulates the error over time, used for the integral term.

def pid_controller(current, target):
    """
    Calculates the control output based on the Proportional-Integral-Derivative (PID) algorithm.

    Args:
        current (float): The current measured value (e.g., temperature).
        target (float): The desired target value (e.g., target temperature).

    Returns:
        float: The calculated control output, which dictates how to adjust the system.
    """
    global last_error, integral_sum  # Access the global variables for the last error and integral sum.

    # Calculate the current error: the difference between the target and the current value.
    error = target - current

    # Proportional term: directly proportional to the current error.
    p = kp * error

    # Integral term: accumulates the error over time to eliminate steady-state errors.
    integral_sum += error  # Add the current error to the running sum.
    if abs(error) < 5:  # Anti-windup: only integrate when the error is within a certain threshold.
        i = ki * integral_sum
    else:
        i = 0  # Reset the integral sum if the error is large to prevent integral windup.

    # Derivative term: proportional to the rate of change of the error.
    d = kd * (error - last_error)

    # Update the last error with the current error for the next iteration.
    last_error = error

    # Calculate the total control output by summing the P, I, and D terms.
    output = p + i + d

    # Limit the output to a maximum and minimum value to prevent the system from overreacting.
    output = max(min(output, 100), -100)  # Clamps the output between -100 and 100.

    return output  # Return the calculated control output.

# Example usage: iterate through the list of target temperatures.
for target in targets:
    print(f"\nSetting target to {target}°C")
    # Continue the control loop until the current temperature is very close to the target.
    while abs(current - target) > 1:
        # Calculate the control output using the PID controller.
        output = pid_controller(current, target)

        # Simulate the system responding to the control output by updating the current temperature.
        # The output is scaled by 0.1 to represent a gradual change.
        current += output * 0.1

        # Introduce a small delay to simulate the time it takes for the system to react.
        time.sleep(0.5)  # Pause for 0.5 seconds.

        # Print the current state of the system: current temperature, control output, and target temperature.
        print(f"Current: {current:.2f}, Output: {output:.2f}, Target: {target}")

    # Once the current temperature is close to the target, print a success message.
    print(f"Reached target temperature: {current:.2f}\n")