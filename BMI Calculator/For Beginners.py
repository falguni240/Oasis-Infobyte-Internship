# Beginner CLI-based BMI Calculator

def calculate_bmi(weight, height):
    """Calculate BMI using the standard formula"""
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """Classify the BMI into health categories"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_user_input():
    """Get and validate user input"""
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return None, None
        return weight, height

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None

def main():
    """Main function to run the BMI calculator"""
    weight, height = get_user_input()
    if weight is not None and height is not None:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

# Run the program
main()
