import easyocr
from PIL import Image
import requests
from io import BytesIO


def analyse(config, image):
    try:
        response = requests.get(image)
        img = Image.open(BytesIO(response.content))

        IMAGE_PATH = 'C:\\Users\\Furkan\\Desktop\\ImageAnalyse\\Functions\\pictures\\2.jpg'
        
        reader = easyocr.Reader(['en'])
        ocr_result = reader.readtext(IMAGE_PATH, paragraph="False")

        # filtering the results
        # config = ['Milk', "Juice", "Yoghurt", "Egg", "Cheese", "Chocolate"]

        newConfig = convertArrayToLowerCase(config)

        products_result = []
        for i in ocr_result:
            if i[1].isupper():
                products_result.append(i[1])

        lowerProductResult = convertArrayToLowerCase(products_result)
        return (list(set(newConfig) - set(lowerProductResult)))

    except:
        return("Error")


def convertArrayToLowerCase(arr):
    newArr = []
    for i in arr:
        newArr.append(i.lower())
    return newArr
