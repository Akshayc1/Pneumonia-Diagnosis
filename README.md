NOTE : Sometimes github fails to render the ipynb notebooks, I believe that is some temporary (and recurring) issue with their backend.
Try to open that notebook using nbviewer online, you don't need to install it. Just copy the jupyter notebook URL to  below link.

Link :  "https://nbviewer.jupyter.org/"


You can download dataset from following kagggle link : 
https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia

The dataset is organized into 3 folders (train, test, val) and contains subfolders for each image category (Pneumonia/Normal). 
There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal).

Performance Metrics : 

        1. Confusion Matrix
        2. Precision, Recall
        
Precision also cannot be taken as single metric and has less significance than recall for this dataset because we want to minimize 
false negative.

False negative has to be intuitively minimized because falsely diagnosing a patient of pneumonia as not having a pneumonia is a much larger
deal than falsely diagnosing a healthy person as a pneumonia patient which is our major concern . That is why we are making this model .
To reduce the mistakes done by doctors accidentally .

You can download 'model.h5' file from my google drive : https://drive.google.com/open?id=1-8FVKSNeDXzsQ3QoyJKS19MRH57X4E75


Web Application Template: 


![Capture](https://user-images.githubusercontent.com/39961205/56297201-8f88e400-614d-11e9-8ea8-3004cc0869a1.PNG)




