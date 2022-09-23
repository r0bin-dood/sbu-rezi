from roboflow import Roboflow
rf = Roboflow(api_key="Ewijr1RiiiTYhmkAXpfn")
project = rf.workspace().project("sbu-hacks-chess-pieces-detection-demo")
model = project.version(1).model

# infer on a local image
print(model.predict("test_img.jpg", confidence=20, overlap=90).json())

# visualize your prediction
model.predict("test_img.jpg", confidence=20, overlap=90).save("prediction.jpg")

# infer on an image hosted elsewhere
#print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())