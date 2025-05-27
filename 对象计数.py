import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("./videos/test2.mp4")
assert cap.isOpened(), "Error reading video file"

frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 获取宽度
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 获取高度
region_points = [(int(frame_width/4), 0), (int(frame_width/4), int(frame_height))]      # line counting


# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("object_counting_output.mp4", cv2.VideoWriter.fourcc(*"mp4v"), fps, (w, h))

# Initialize object counter object
counter = solutions.ObjectCounter(
    show=True,  # display the output
    region=region_points,  # pass region points
    model="yolo11n.pt",  # model="yolo11n-obb.pt" for object counting with OBB model.
    classes=[2],  # count specific classes i.e. person and car with COCO pretrained model
    tracker="botsort.yaml",  # choose trackers i.e "bytetrack.yaml"
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = counter(im0)

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows


