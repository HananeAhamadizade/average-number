
# GitHub Repository:https://github.com/HananeAhamadizade/average-number.git

def average(numbers):
    return sum(numbers) / len(numbers)


while True:
    try:
        user_input = input()

        numbers = [float(num) for num in user_input.split()]

        result = average(numbers)

        print(f"{result:.2f}")

        break

    except ValueError:
        print("Invalid Input! Enter a valid input.")
        
