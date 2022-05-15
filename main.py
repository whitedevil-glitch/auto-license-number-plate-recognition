import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# to detect where the car is from
cascade= cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
states={"AN":"Andaman and Nicobar","AP":"Andhra Pradesh","AR":"Arunachal Pradesh","AS":"Assam","BR":"Bihar","CH":"Chandigarh","DN":"Dadra and Nagar Haveli","DD":"Daman and Diu","DL":"Delhi","GA":"Goa","GJ":"Gujarat",
"HR":"Haryana","HP":"Himachal Pradesh","JK":"Jammu and Kashmir","KA":"Karnataka","KL":"Kerala","LD":"Lakshadweep","MP":"Madhya Pradesh","MH":"Maharashtra","MN":"Manipur","ML":"Meghalaya","MZ":"Mizoram","NL":"Nagaland","OD":"Odissa","PY":"Pondicherry","PN":"Punjab","RJ":"Rajasthan","SK":"Sikkim","TN":"TamilNadu","TR":"Tripura","UP":"Uttar Pradesh", "WB":"West Bengal","CG":"Chhattisgarh","TS":"Telangana","JH":"Jharkhand","UK":"Uttarakhand"}


# main code for reading image and detecting number plate

def extract_num(img_name):
    img = cv2.imread(img_name) ## Reading Image
    # Converting into Gray
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    # Detecting plate
    nplate = cascade.detectMultiScale(gray,1.1,4) # making the plate grey
    for (x,y,w,h) in nplate:
        # Crop a portion of plate
        a,b = (int(0.02*img.shape[0]), int(0.025*img.shape[1]))
        plate = img[y+a:y+h-a, x+b:x+w-b, :]
        # make image more darker to identify the Liscense Plate Register no.
        ## iMAGE PROCESSING {thresholding image for accuracy}
        kernel = np.ones((1, 1), np.uint8)
        plate = cv2.dilate(plate, kernel, iterations=1) # dilate technique
        plate = cv2.erode(plate, kernel, iterations=1) # erode technique
        plate_gray = cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY) #converting img to grey
        (thresh, plate) = cv2.threshold(plate_gray, 127, 255, cv2.THRESH_BINARY)
        # Feed Image to OCR engine
        read = pytesseract.image_to_string(plate) # reading the text and convertin to string
        read = ''.join(e for e in read if e.isalnum()) # cleaning string by is alpha num func
        print(read)
        stat = read[0:2] # returns first two letters of detected plate for recognizing state
        try:
        # Fetch the State information
            print('Car Belongs to',states[stat])
        except:
            print('State not recognised!!')
        print(read)
        cv2.rectangle(img, (x,y), (x+w, y+h), (51,51,255), 2)
        cv2.rectangle(img, (x, y - 40), (x + w, y),(51,51,255) , -1)
        cv2.putText(img,read, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('PLate',plate)
        # Save & display result image
        cv2.imwrite('plate.jpg', plate)

    cv2.imshow("Result", img)
    cv2.imwrite('result.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# function call
extract_num('./test_images/t4.jpg')
