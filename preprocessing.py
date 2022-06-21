import numpy as np
import cv2


# Input: data_dir(str) -- the path of data.
#        cate2Idx(dict) -- mapping the category name to class index.
# Return: x(array) -- the images data, the shape in this task should be (15178, 28, 28, 3).
#         y(array) -- the label of images, the shape in this task should be (15178,).
def data_preprocessiong(data_dir, cate2Idx):
    x = None
    y = None
    #### TODO HERE
    t=list(cate2Idx.keys())
    t1=list(cate2Idx.values())
    k=[data_dir+r"/"+data for data in t]
    files=[os.listdir(k[i]) for i in range(len(k))]
    df=[k[dir]+r"/"+h for dir in range(len(k)) for h in files[dir]]
    y=[t1[dir] for dir in range(len(k)) for h in range(len(files[dir]))] 
    img=[cv2.imread(f) for f in df]
    img=np.array(img)
    img1=[cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB) for i in range(img.shape[0])]
    img1=np.array(img1)
    x=[cv2.resize(img1[i], (28, 28)) for i in range(img1.shape[0])]
    x=np.array(x)
    y=np.array(y)
    #### END TODO
    return x, y