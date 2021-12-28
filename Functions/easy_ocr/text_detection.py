import easyocr
from PIL import Image
from flask import json


def analyse(f, config):
    try:
        img = Image.open(f)
        configArray = json.loads(config)

        reader = easyocr.Reader(['en'])
        ocr_result = reader.readtext(img, paragraph="False")
       
        newConfig = convertArrayToCapitalizeCase(configArray)

        products_result = []
        for i in ocr_result:
            if i[1].isupper():
                products_result.append(i[1])

        capitalizeProductResult = convertArrayToCapitalizeCase(products_result)
        return (list(set(newConfig) - set(capitalizeProductResult)))

    except Exception as err:
        print(str(err))
        return(str(err))


def convertArrayToCapitalizeCase(arr):
    newArr = []
    for i in arr:
        newArr.append(i.title())
    return newArr
