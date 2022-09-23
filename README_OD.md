# Steps for Object Detection

Note: The following example commands assume you are in the yolov5 directory within this project.

Note 2: There is a sample Google Colab network that is setup for working through training a custom ML model. You can make a copy of it and use it
instead of an IDE or terminal. Take a look here: 

1. Acquire dataset

   For our tutorial, we will be using this chess piece data set: https://universe.roboflow.com/joseph-nelson/chess-pieces-new
   It is also attached as a zip here. 
   
   Additional datasets can be found here: https://universe.roboflow.com/

2. Annotate and prep data (using Roboflow in this example)

   For our tutorial, we will use Roboflow to annotate and prepare our dataset for training. 
   
   Our workspace: https://app.roboflow.com/sbu-hacks-2022-demo/sbu-hacks-chess-pieces-detection-demo/1
   
3. Export dataset

    Once dataset is ready, copy code snippet and paste into 'dataset_download.py'.
    Execute by running 'python dataset_download.py' in terminal. 
    You should now see that there is a folder that contains your image files with annotations.

4. Train model on dataset

    It is preferable to train on a cloud service (Colab, Jupyter notebook, AWS) in order to speed up the training process. You can also do it relatively quickly on a machine with a GPU.
    It will take a long time to train on a machine without a GPU, so try to avoid this.
    You can also train on Roboflow, which will give you code snippets you can throw in your applications. 
    
    This command is for training from the terminal:
    
    python train.py --img 416 --batch 16 --epochs 150 --data ../SBU-Hacks-Chess-Pieces-Detection-Demo-1/data.yaml --cache
    
    Note: From testing, we have found that the data.yaml file does not always point to the location of the dataset correctly. 

5. Test and evaluate model
    
    Test model using static images:
    
    python detect.py --weights ../chess_model.pt --conf .5 --source ../test_img.jpg
    
    Test model using video:
    
    python detect.py --weights ../chess_model.pt --conf .5 --source https://youtu.be/wpfSxSb6ZtM
        
6. Integrate with notification system

    All that needs to be done is to change our 'python detect.py ...' command from above to
    'python detect-rezi.py'
    
    python detect-rezi.py --weights ../chess_model.pt --conf .5 --source https://youtu.be/wpfSxSb6ZtM
