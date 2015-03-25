SERVER = False
if SERVER:
    print "enter here the server URL"
else:
    FORGOT_PASSWORD_URL = 'http://127.0.0.1:8000/confirmpassword/'


# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 1025
# EMAIL_USE_TLS = True
#  
# DEFAULT_FROM_EMAIL = 'shebeer@toobler.com'
class Collection:
    pass

#registration
REG_PASSWORD_SUBJECT = 'Subject:You Account Password \n'
REG_PASSWORD_BODY_USERNAME = '\n this is kitchen cabinet \n\n username :  '
REG_PASSWORD_BODY_PASS = '\n\n activation_password : '

FORGET_PASSWORD = 'Subject:Forgot Password \n'
REG_PASSWORD_BODY_EMAIL = '\n this is kitchen cabinet \n\n username :  '
REG_PASSWORD_BODY_NEW_LINK = '\n\n activation_password : '


EMAIL_VALIDATION = 'Entered email is not valid'


EMAIL_HOST_USER = 'shebeer@toobler.com'
EMAIL_HOST_PASSWORD = 'justforfun118'

ENCRYPTION_KEY = "1234567890123456"

#paging
LIST_COUNT = 10

ADMIN = 'admin@toobler.com'
# constant for already exist
CATEGORY_EXISTS = 'Category already exists'
SUB_CATEGORY_EXISTS = 'Subcategory already exists'
SUB_CATEGORY_EXISTS_FOR_CATEGORY = 'Subcategory already exists under the same category'
DOOR_EXIST = 'Door already exists'
PRODUCT_EXIST = 'Product already exists'
TAX_EXISTS = 'Tax already exists'



# constant for success creation
CATEGORY_SUCCESS = 'The category has been added successfully'
SUB_CATEGORY_SUCCESS = 'The subcategory has been added successfully'
DOOR_SUCCESS = 'The door has been added successfully'
PRODUCT_SUCCESS = 'The product has been added successfully'
TAX_SUCCESS = 'The tax has been added successfully'

#constants for edit success
TAX_EDIT_SUCCESS = 'The tax has been updated successfully'
SUB_CATEGORY_EDIT_SUCCESS ='The subcategory has been updated successfully'
CATEGORY_EDIT_SUCCESS = 'The category has been updated successfully'
PRODUCT_EDIT_SUCCESS = 'The product has been updated successfully'
HINGES_SUCCESS = 'The hinge has been added successfully'
HINGES_EDIT_SUCCESS = 'The hinge has been updated successfully'
HINGES_EXISTS = 'Hinge already exists'
DOOR_EDIT_SUCCESS = 'The door has been updated successfully'
CABINET_SUCCESS = 'The cabinet has been added successfully'
CABINET_EDIT_SUCCESS = 'The cabinet has been updated successfully'
CABINET_EXISTS = 'Cabinet already exists'

MATERIAL_SUCCESS = 'The material has been added successfully'
MATERIAL_EXISTS = 'Material already exists'
MATERIAL_EDIT_SUCCESS = 'The material has been updated successfully'

DRAWER_SUCCESS = 'The drawer has been added successfully'
DRAWER_EDIT_SUCCESS = 'The drawer has been updated successfully'
DRAWER_EXISTS = 'Drawer already exists'
