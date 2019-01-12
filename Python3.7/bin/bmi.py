#!/usr/bin/env python3.6

# BMI = (weight in kg / height in meters squared )
# Imperial version: BMI * 703

high_weight_ratio = {
    range(0, 16): 'Pronounced body mass deficit',
    range(16,18): 'Body weight deficit',
    range(18,25): 'Norm',
    range(25,30): 'Overweight',
    range(30,35): 'Obesity of the first stage',
    range(35,40): 'Obesity of the second stage',
    range(40,100): 'Obesity of the third stage'
}

def gather_info():
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    system = input("Are your mearsurements in metric or imperial systems? ").lower().strip()
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return the Body Mass Index (BMI) for the
    given weight, height, and measurement system.
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = int(calculate_bmi(weight, system='imperial', height=height))
        bmi_n = int(bmi / 703)
        for key in high_weight_ratio:
            if bmi_n in key:
                print(f"Your BMI is {bmi} - {high_weight_ratio[key]}")
                break
        break
    elif system.startswith('m'):
        bmi = int(calculate_bmi(weight, height))
        for key in high_weight_ratio:
            if bmi in key:
                print(f"Your BMI is {bmi} - {high_weight_ratio[key]}")
                break
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric.")
