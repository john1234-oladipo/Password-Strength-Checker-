import re
import getpass
from typing import List, Tuple

def check_password_strength(password: str) -> Tuple[int, List[str]]:
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")
    
    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    # Number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    # Special character check
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Add special characters")
    
    # Common password check (simplified)
    common_passwords = ['password', '123456', 'qwerty', 'letmein']
    if password.lower() in common_passwords:
        score = 0
        feedback.append("Avoid common passwords")
    
    # Repeated characters check
    if re.search(r'(.)\1{2,}', password):
        score -= 1
        feedback.append("Avoid repeated characters")
    
    return score, feedback

def get_strength_description(score: int) -> str:
    if score <= 1:
        return "Very Weak"
    elif score == 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"

def main():
    print("Password Strength Checker")
    print("Enter your password for analysis (input will be hidden):")
    
    password = getpass.getpass()
    
    score, feedback = check_password_strength(password)
    strength = get_strength_description(score)
    
    print(f"\nPassword Strength: {strength} ({score}/5)")
    
    if feedback:
        print("\nSuggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nYour password is strong!")

if __name__ == "__main__":
    main()