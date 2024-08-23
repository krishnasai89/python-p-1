from zxcvbn import zxcvbn
import getpass

def check_password_strength():
    password = getpass.getpass("Enter your password: ")
    result = zxcvbn(password)
    
    print(f"Password: {result['password']}")
    print(f"Score: {result['score']}/4")
    print(f"Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
    print("Feedback:")
    for suggestion in result['feedback']['suggestions']:
        print(f"- {suggestion}")

if __name__ == "__main__":
    check_password_strength()
