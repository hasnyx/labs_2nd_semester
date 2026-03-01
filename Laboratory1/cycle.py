from longest_peak import longest_peak

def analyze_training():
    print("=== Cycling Power Analysis System ===")
    print("Goal: Identify the longest cycle (warmup, peak, recovery).")
    
    try:
        user_input = input("\nEnter power data points (Watts per min): ")
        power_data = [int(x) for x in user_input.split()]
        
        if len(power_data) < 3:
            print("Error: Insufficient data for analysis (minimum 3 values required).")
            return

        length, summit_min = longest_peak(power_data)

        if length > 0:
            print(f"\nTraining Session Results:")
            print(f"- Longest cycle duration: {length} min.")
            print(f"- Peak load recorded at: minute {summit_min + 1}.")
        else:
            print("\nNo valid peak cycles identified in this session.")
            
    except ValueError:
        print("Error: Please enter integers separated by spaces.")

if __name__ == "__main__":

    analyze_training()
