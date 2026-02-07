def calculate_efficiency(input_power, output_power):
    efficiency = (output_power / input_power) * 100
    loss = input_power - output_power
    return efficiency, loss


try:
    input_power = float(input("Enter input power (W): "))
    output_power = float(input("Enter output power (W): "))

    if input_power <= 0 or output_power < 0:
        print("Power values must be positive.")
    elif output_power > input_power:
        print("Output power cannot be greater than input power.")
    else:
        eff, loss = calculate_efficiency(input_power, output_power)
        print(f"\nMotor Efficiency: {eff:.2f}%")
        print(f"Power Loss: {loss:.2f} W")

except ValueError:
    print("Please enter valid numeric values.")
