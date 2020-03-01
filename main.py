from imageai.Detection import ObjectDetection
import os
from win32com.client import Dispatch

speak=Dispatch("SAPI.SpVoice")

execution_path=os.getcwd()

detection=ObjectDetection()
detection.setModelTypeAsRetinaNet()
detection.setModelPath(os.path.join(execution_path,"resnet50_coco_best_v2.0.1.h5"))
detection.loadModel()
detectors=detection.detectObjectsFromImage(input_image=os.path.join(execution_path,"al.jpg"),output_image_path=os.path.join(execution_path,"detected_image.jpg"))                       

speak.Speak("The image contains")

for eachObject in detectors:
    print(eachObject["name"],":",eachObject["percentage_probability"])

    speak.Speak(eachObject["name"])
    
