import logging
from datetime import datetime

# Configure the logging
logging.basicConfig(
    filename="age_verification.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def main():
    while True:
        try:
            # Ask for the user's age
            age = int(input("Enter your age: "))
            
            # Check the age and log the message
            if age > 18:
                print(f"Age is {age}.")
                logging.info(f"User's age is {age}.")
            else:
                print("Error: Age is less than 18.")
                logging.error(f"Age is less than 18. Provided age: {age}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            logging.error("Invalid input for age. Non-numeric value entered.")

if __name__ == "__main__":
    main()


