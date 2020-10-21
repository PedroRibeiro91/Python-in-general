import cv2

# build a model (a classifier) based on the file haarcascade_frontalface_default.xml  
face_detection_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# load an image
test_image = cv2.imread('imagem001.jpg')

# the haar cascade works only with grayscale images so we convert our test_image to grayscale
grayscaled_test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# "identifies the scale of our image and applies our model" to return the coordinates of a rectangle countaining the face on the image 
face_coordinates = face_detection_model.detectMultiScale(grayscaled_test_image) 
#print(face_coordinates)

# some images have more than one face
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(test_image, (x,y), (x+w, y+h), (0,255,0),2)

# show the image
cv2.imshow('This is me', test_image)
# wait until a key is pressed to it closes the image
cv2.waitKey()


print("I'm working ;)")