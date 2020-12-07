import pyaudio
import wave

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
				channels=channels,
				rate=fs,
				frames_per_buffer=chunk,
				input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds












# Python program to save a 
# video using OpenCV 


import cv2 


# Create an object to read 
# from camera 
video = cv2.VideoCapture(0) 

# We need to check if camera 
# is opened previously or not 
if (video.isOpened() == False): 
	print("Error reading video file") 

# We need to set resolutions. 
# so, convert them from float to integer. 
frame_width = int(video.get(3)) 
frame_height = int(video.get(4)) 

size = (frame_width, frame_height) 

# Below VideoWriter object will create 
# a frame of above defined The output 
# is stored in 'filename.avi' file. 
result = cv2.VideoWriter('filename.avi', 
						cv2.VideoWriter_fourcc(*'MJPG'), 
						10, size) 
	
while(True): 
	ret, frame = video.read() 

	if ret == True: 

		# Write the frame into the 
		# file 'filename.avi' 
		result.write(frame) 
		data = stream.read(chunk)
		frames.append(data)

		# Display the frame 
		# saved in the file 
		cv2.imshow('Frame', frame) 

		# Press S on keyboard 
		# to stop the process 
		if cv2.waitKey(1) & 0xFF == ord('s'): 
			break

	# Break the loop 
	else: 
		break

# When everything done, release 
# the video capture and video 
# write objects 
video.release() 
result.release() 
	
# Closes all the frames 
cv2.destroyAllWindows() 

print("The video was successfully saved") 
# for i in range(0, int(fs / chunk * seconds)):


# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

