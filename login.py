
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_login(self):
        if self.username == "Vinitha" and self.password == "Test123":
            return "Login successful"
        else:
            return "Invalid username or password"


Ecommerce = Login("Vinitha", "Test123")
print(Ecommerce.check_login())