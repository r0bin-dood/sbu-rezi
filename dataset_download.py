from roboflow import Roboflow
rf = Roboflow(api_key="YOUR-KEY-HERE")
project = rf.workspace("sbu-hacks-2022-demo").project("sbu-hacks-chess-pieces-detection-demo")
dataset = project.version(1).download("yolov5")




model = project.version(1).model

# infer on a local image
print(model.predict("your_image.jpg", confidence=40, overlap=30).json())

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())



