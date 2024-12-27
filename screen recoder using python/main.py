import cv2
import numpy as np
import pyautogui

# set the screen resolution to record
screen_width, screen_height = pyautogui.size()
resolution = (screen_width, screen_height)

# set the output video filename
output_filename = "screen_recording.mp4"

# set the frames per second for the recording
fps = 30.0

# define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_filename, fourcc, fps, resolution)

# define the recording duration in seconds
recording_duration = 5 

# start the screen recording
for _ in range(int(fps * recording_duration)):
    # capture the screen
    screen = pyautogui.screenshot()

    # convert the screenshot to the numpy array and BGR format for opencv
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # write the frame to the output video
    out.write(frame)

# release the VideoWriter
out.release()