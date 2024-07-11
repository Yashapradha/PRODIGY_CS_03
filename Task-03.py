import re

def password_complexity_checker(password):

    # Initialize scores
    length_score = len(password) >= 8
    uppercase_score = bool(re.search(r'[A-Z]', password))
    lowercase_score = bool(re.search(r'[a-z]', password))
    number_score = bool(re.search(r'[0-9]', password))
    special_char_score = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate total score
    total_score = sum([length_score, uppercase_score, lowercase_score, number_score, special_char_score])

    # Generate feedback messages
    criteria_feedback = []
    if length_score:
        criteria_feedback.append("✓ Length is at least 8 characters")
    else:
        criteria_feedback.append("✗ Length is less than 8 characters")

    if uppercase_score:
        criteria_feedback.append("✓ Contains uppercase letters")
    else:
        criteria_feedback.append("✗ No uppercase letters")

    if lowercase_score:
        criteria_feedback.append("✓ Contains lowercase letters")
    else:
        criteria_feedback.append("✗ No lowercase letters")

    if number_score:
        criteria_feedback.append("✓ Contains numbers")
    else:
        criteria_feedback.append("✗ No numbers")

    if special_char_score:
        criteria_feedback.append("✓ Contains special characters")
    else:
        criteria_feedback.append("✗ No special characters")

    # Determine password strength
    if total_score >= 5:
        strength = "Very Strong password"
    elif total_score == 4:
        strength = "Strong password"
    elif total_score == 3:
        strength = "Moderate password"
    else:
        strength = "Weak password"

    # Combine feedback
    feedback = "\n".join(criteria_feedback)
    return f"{strength}\n{feedback}"

password = input("Enter your password: ").strip()
if password:
    strength = password_complexity_checker(password)
    print(f"Password strength:\n{strength}")
else:
    print("No password entered. Please try again.")