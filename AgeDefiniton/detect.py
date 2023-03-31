import cv2

#* Yüz tanıma ve algılama fonksiyonu 
def highlightFace(net,frame,conf_thres=0.7):

    frameOpencvDnn=frame.copy()
    frameHeight=frameOpencvDnn.shape[0]
    frameWidth=frameOpencvDnn.shape[1]
    blod=cv2.dnn.blodFromImage(frameOpencvDnn,1.0,(300,300),[104,117,123],True,False)

    net.setInput(blod)
    detections=net.forward()
    faceBoxes=[]
    
    for i in range(detections.shape[0]):
        confidence=detections[0,0,i,2]
        if confidence>conf_thres:
            x1=int(detections[0,0,i,3]*frameWidth)
            y1=int(detections[0,0,i,4]*frameHeight)
            x2=int(detections[0,0,i,5]*frameWidth)
            y2=int(detections[0,0,i,6]*frameHeight)
            faceBoxes.append([x1,y1,x2,y2])
            cv2.rectangle(frameOpencvDnn,(x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)),8)
    return frameOpencvDnn,faceBoxes        

#* Hazır modellerin tanıtılması (yas ve cinsiyet algılaaycak ola nhazır kutuphane modelleri)
faceProto="opencv_face_detector.pbtx"
faceModel="opencv_face_detector_uint8.pb"
ageProto="age_deploy.prototxt"
ageModel="net.caffemodel"
genderProto="gender_deploy.prototxt"
genderModel="gender_net.caffemodel"

MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
ageList=['(0-2)','(4-6)','(8-12)','(15-20)','(25-32)','(38-43)','(48-53)','(60-100)'] #Yaş aralıkları
genderList=['Erkek','Kadın']

faceNet=cv2.dnn.readNet(faceModel,faceProto)
ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)

# Resmin tanıtılması algılanması ve tahminin yapıldıgı alan
video=cv2.VideoCapture("myFace.jpg" if "myFace.jpg" else 0)
padding=20
while cv2.waitKey(1)<0:
    hasFrame,frame=video.read()
    if not hasFrame:
        cv2.waitKey()
        break
     #Çizgilerin çizilecek fonk. çağırılması 
    resultImg,faceBoxes=highlightFace(faceNet,frame)
    if not faceBoxes:
        print("Yüz algılanmadı")

    for faceBox in faceBoxes:    
        face=frame[max(0,faceBox[1]-padding):
                   min(faceBox[3]+padding,frame.shape[0]-1),max(0,faceBox[0]-padding):
                   min(faceBox[2]+padding,frame.shape[1]-1)]
        
        blod=cv2.dnn.blodFromImage(face,1.0(227,227), MODEL_MEAN_VALUES,swapRB=False)
        genderNet.setInput(blod)
        genderPreds=genderNet.forward()
        gender=genderList[genderPreds[0].argmax()]
        print(f"Cinsiyeti: {gender}")

        ageNet.setInput(blod)
        agePreds=ageNet.forward()
        age=ageList[agePreds[0].argmax()]
        print(f"Yaşı: {age[1:-1]} yaşındadır")

        cv2.putText(resultImg,f'{gender},{age}',(faceBox[0],faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX,0.8, (0,255,255),2, cv2.LINE_AA)  
        cv2.imshow("Yaş ve Cinsiyet algılama ",resultImg)
