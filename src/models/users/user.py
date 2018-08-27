import uuid
from src.common.utils import Utils
from src.common.database import Database
import src.models.users.errors as UserErrors


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """

        This method verifies that an email/password combo (sent by the site form) is valid
        :param email:
        :param password: a sha512 hashed password
        :return:
        """

        # check to see if user exists, by looking in database
        user_data = Database.find_one("users", {"email": email})
        if user_data is None:
            # Tell user their email doesn't exist
            raise UserErrors.UserNotExistsError("Your user does not exist")
        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell user that their password is wrong
            raise UserErrors.IncorrectPasswordError("Your password was wrong.")

        return True  # executes IF the password/email is correct
