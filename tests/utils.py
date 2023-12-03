import unittest
from domain.utils import dict_to_instance
from domain.objects import User

class TestUser(unittest.TestCase):
    def test_dict_to_instance(self):
        email = "test@test.com"
        first_name = "first_name"
        last_name = "last_name"

        user_dict = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name
        }
        user = User()
        dict_to_instance(user, user_dict)
        
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)

if __name__ == '__main__':
    unittest.main()