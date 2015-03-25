from settings import MEDIA_URL,IMAGE_FILE_PATH
def uploadImage(commonObj):
    """
    """
    image = commonObj.image
    commonObj.filename=image.name    
    commonObj.filename = str(commonObj.id)+'_'+commonObj.filename
    commonObj.filePath=MEDIA_URL+commonObj.image_for+commonObj.filename
    destination = open(commonObj.filePath,'wb+')              
    for chunk in image.chunks():    
        destination.write(chunk)
        destination.close()  
    commonObj.filePath = IMAGE_FILE_PATH+commonObj.image_for+commonObj.filename
    return commonObj.filePath
