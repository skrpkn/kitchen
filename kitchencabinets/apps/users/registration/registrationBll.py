import registrationDal
import smtplib
from constants import  EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, ENCRYPTION_KEY

def createUser(usersObj):
    """
    function is used to create user
    """
    
    password = registrationDal.createUser(usersObj)
    return password


def sendMail(usersObj):
    """
    function to send emails to the new users
    to activate the account
    """
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    header = 'To:' + usersObj.email + '\n' + 'From: ' + EMAIL_HOST_USER + '\n' + usersObj.subject
    msg = header + usersObj.msg
    smtpserver.sendmail(EMAIL_HOST_USER, usersObj.email, msg)
    smtpserver.close()
    
def checkEmailValidation(usersObj):
    """
    """
    return registrationDal.checkEmailValidation(usersObj)
     
def resetPassword(usersObj):
    """
    function to reset passwword
    """
    
    users = registrationDal.resetPassword(usersObj)
    return users

def forgotPassword(email):
    """
    function to reset passwword
    """
    
    return registrationDal.forgotPassword(email)
    
def getUserName(email):
    return registrationDal.getUserName(email)

def encrypt(usersObj):
    """
    function to encrypt the given data
    """
    
    from Crypto.Cipher import AES
    from urllib import quote
    
    encryption_obj = AES.new(ENCRYPTION_KEY)
    
    mismatch = len(usersObj.email) % 16
    if mismatch != 0:
        padding = (16 - mismatch) * ' '
        usersObj.email+= padding
        
    ciph = encryption_obj.encrypt(usersObj.email)
    
    return quote(ciph)
    
def decrypt(qouted_ciph):
    """
    function to decrypt the given data
    """
    from urllib import unquote
    
    ciph = unquote(quoted_ciph)
    return encryption_obj.decrypt(ciph)


    
    