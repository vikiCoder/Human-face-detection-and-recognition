from firebase import firebase
import json
import identify
import lcd,time
import subprocess

smileThreshold = 0.25

def findMaxEmotion(emotionDict):
    maxEmotionValue = 0
    for emot in emotionDict:
        if maxEmotionValue <= int(float(emotionDict[emot])*100):
            maxEmotionValue = int(float(emotionDict[emot])*100)
            maxEmotion = emot
    return maxEmotion

def isSmiling(smileValue):
    if smileValue >= smileThreshold:
        return "Yes"
    else:
        return "No"

ageDict = {
    0 : "0-10",
    1 : "10-20",
    2 : "20-30",
    3 : "30-40",
    4 : "40-50",
    5 : "50-60",
    6 : "60+",
    7 : "60+",
    8 : "60+",
    9 : "60+"
}

def findAge(oldAge):
    return ageDict[int(oldAge/10)]

URL = 'https://el213-project.firebaseio.com/'

def main():
    d = identify.Identify()
    lcd.lcd_init()

    if d == -1:
        lcd.lcd_print("No Face Found")
        time.sleep(1)
        return 1

    if d == -2:
        lcd.lcd_print("No Internet Connection")
        return 1

    name = d['name']
    gender = d['gender']
    age = findAge(d['age'])
    smile = isSmiling(d['smile'])
    glasses = d['glasses']
    confidence = d['confidence']
    emotion = findMaxEmotion(d['emotion'])

    lcd.lcd_string("Uploading Data...")
    
    with open("index.xml", 'r+') as f:
        line = f.readline()
        index = int(line)

    fb = firebase.FirebaseApplication(URL)
    imageName = str(index)+".jpg"

    result = fb.put('/',index,{'name':name, 'gender':gender ,'age':age, 'smile':smile, 'glasses':glasses, 'confidence':confidence, 'emotion':emotion})

    status = 1

    try:
        status = subprocess.check_call(["./storage.sh",imageName])
    except:
        pass
    
    while status!=0:
        try:
            status = subprocess.check_call(["./storage.sh",imageName])
        except:
            pass

    index += 1
    with open("index.xml", 'w+') as f:
        f.write(str(index))

    lcd.lcd_string(name)
    if smile == "Yes":
        smile = "Smiling"
    else:
        smile = "Not Smiling"
    printString = "Age Range:" + str(age) + " " + str(gender) + " " + str(smile) + " " + str(glasses) + " Emotion:" + str(emotion)
    lcd.lcd_print(printString,2)
    lcd.lcd_clear()
    return 0
