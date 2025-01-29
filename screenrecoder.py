# in this program i am gonna create a python program to make a screen recorder.
import cv2
import numpy as np
import pyautogui
import keyboard
from datetime import datetime

screen_size=pyautogui.size()
fps=30
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output_file=f"screen_recording_{datetime.now().strftime('%y%m%d_%H%M%S')}.mp4"
out=cv2.VideoWriter(output_file,fourcc,fps,(screen_size.width,screen_size.height))

print("The video is currently recording....... Press q to stop recording.")

# opening the while loop to do the recording until the program 

while True:
    screen=pyautogui.screenshot()
    frame=np.array(screen)
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    out.write(frame)

    if keyboard.is_pressed('q'):
        print("' q ' is pressed!!")
        break
out.release()
print(f"Video saved to {output_file}")

def explaination():
    """Explanation of the Code

        Imports:
        cv2: OpenCV library for video processing.
        numpy: Library for numerical operations.
        pyautogui: Library for taking screenshots.
        keyboard: Library for detecting key presses.
        datetime: Library for handling date and time.
        
        Screen Size and FPS:
        screen_size = pyautogui.size(): Gets the screen size.
        fps = 30: Sets the frames per second for the video.
        
        Video Writer Setup:
        fourcc = cv2.VideoWriter_fourcc(*"XVID"): Specifies the codec for the video.
        output_file = f"screen_recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4": Creates a unique filename using the current date and time.
        out = cv2.VideoWriter(output_file, fourcc, fps, (screen_size.width, screen_size.height)): Initializes the video writer with the specified parameters.
        
        Recording Loop:
        while True: Starts an infinite loop for recording.
        screen = pyautogui.screenshot(): Takes a screenshot.
        frame = np.array(screen): Converts the screenshot to a NumPy array.
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR): Converts the color format from RGB to BGR.
        out.write(frame): Writes the frame to the video file.
        
        Stopping the Recording:
        if keyboard.is_pressed('q'): Checks if the 'q' key is pressed.
        print("' q ' is pressed!!"): Prints a message if 'q' is pressed.
        break: Exits the loop if 'q' is pressed.
        
        Releasing Resources:
        out.release(): Releases the video writer.
        print(f"Video saved to {output_file}"): Prints the location of the saved video file."""
    
if __name__ == "__main__":
    explaination()