将对象计数.py文件中的cap = cv2.VideoCapture("./videos/test2.mp4")和video_writer = cv2.VideoWriter("object_counting_output.mp4", cv2.VideoWriter.fourcc(*"mp4v"), fps, (w, h))中的文件路径更改成自己需要输入的文件路径即可。
此代码将class限定为2是为了只检测车辆。这个代码可以完成车辆到检测、跟踪以及过线计数，但是存在一个显著问题就是当车辆被遮挡时再出现ID大概率改变，这个现象目前市面上没有太好的解决办法，即没有太好的解决reid问题的办法。
