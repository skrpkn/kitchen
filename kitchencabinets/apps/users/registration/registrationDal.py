from django.contrib.auth.models import User

def createUser(usersObj):
    user = User(username=usersObj.email,first_name=usersObj.first_name,last_name=usersObj.last_name,email=usersObj.email)
    password = User.objects.make_random_password()
    user.set_password(password)
    user.save()
    return password


def resetPassword(usersObj):
    """
    function is used to list user details
    """
    users = User.objects.get(username=usersObj.currentUser)
    print users.password
    var = users.check_password(usersObj.old_password)
    if var:
        users.set_password(usersObj.confirm_password)
        users.save()
    
    
def forgotPassword(email):
    """
    function is used to list user details
    """
    user = User.objects.get(email=email)
    password = User.objects.make_random_password()
    user.set_password(password)
    user.save()
    return password

def getUserName(email):
    """
    function to find user name of given email
    """
    user = User.objects.get(email=email)
    return user.username

def checkEmailValidation(usersObj):
    """
    """
    details = User.objects.get(email=usersObj.email)
    return details
   
    
