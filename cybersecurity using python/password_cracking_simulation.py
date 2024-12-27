import hashlib

def simulate_password_cracking(hashed_password, password_list):
    for password in password_list:
        if hashlib.sha256(password.encode()).hexdigest() == hashed_password:
            return f"password_cracked: {password}"
        return "password not found"
    
hashed_password_to_crack = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
common_passwords = ["password", "123456", "qwerty", "admin"]

result = simulate_password_cracking(hashed_password_to_crack, common_passwords)
print(result)