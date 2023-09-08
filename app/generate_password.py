import random
import string


class Utils():
    def generate_password(self, n):
        password = ''.join(
            random.choices(
                string.ascii_uppercase
                + string.ascii_lowercase
                + string.digits,
                k=n,
            )
        )
        return password
