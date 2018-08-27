from passlib.hash import pbkdf2_sha512


class Utils(object):

    @staticmethod
    def encrypt_password(password):
        """

        The password comes in as  hashed password, so we're 'encrypting' with pbk
        :param password:
        :return:
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, encrypted_password):
        """

        password (user's password from site), matches database's password version
        The password that's in database, is actually "encrypted" (with pbf)
        :param password: sha512-hashed password
        :param encrypted_password: pbk encrypted password
        :return: True if passwords match
        """

        return pbkdf2_sha512.verify(password, encrypted_password)
