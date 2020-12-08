import os
#from components.video import eye_tracker,face_spoofing,head_pose_estimation
#from components.video import mouth_distance,person_and_phone
#from components.audio import testpro
#from components.audio import audio_main
#from components.video.Emotion_detection.src import emotions

def combine_f(candidate="tejas@gmail"):
    local_path = os.getcwd()
    parent_path = os.path.dirname(local_path)
    print(parent_path)
    c = os.path.join( str(parent_path),"student_interview_data",candidate,"1_")
    print(c)
combine_f()