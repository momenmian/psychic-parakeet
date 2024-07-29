import getpass
import win32security

def authenticate_user(username, password):
    """
    Authenticates the user with the provided username and password for windows.
    :param username: The username to authenticate.
    :param password: The password to authenticate.
    :return: None
    """

    try:
        win32security.LogonUser(
            username,
            None,  # Domain (None for local machine or specify the domain name)
            password,
            win32security.LOGON32_LOGON_NETWORK,
            win32security.LOGON32_PROVIDER_DEFAULT
        )
        print("Authenticated successfully!")
    except win32security.error:
        print("Authentication failed.")

if __name__ == "__main__":
    entered_username = input("Enter your Windows username: ")
    entered_password = getpass.getpass("Enter your Windows password: ")

    authenticate_user(entered_username, entered_password)
