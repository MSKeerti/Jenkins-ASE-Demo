import sys

def check_even(number):
    if number % 2 == 0:
        print(f"Build Success: {number} is even.")
        sys.exit(0)  # Success exit code
    else:
        print(f"Build Failure: {number} is odd.")
        sys.exit(1)  # Failure exit code

if __name__ == "__main__":
    num = 5# Change this to an odd number to simulate failure in Jenkins
    check_even(num)
