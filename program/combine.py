import os
import json
from components.video import eye_tracker,face_spoofing,head_pose_estimation
from components.video import mouth_distance,person_and_phone
#from components.audio import testpro
#from components.audio import audio_main
from components.video.Emotion_detection.src import emotions
def evaluate_video(path):
    res_eye_tracker=eye_tracker_f(path)
    res_face_spoofing=face_spoofing_f(path)
    res_head_pose=head_pose_estimation_f(path)
    res_mouth_destance=mouth_distance_f(path)
    res={}
    #res_emotions=emotions_f(path)

def combine_f(candidate="tejas@gmail"):
    local_path = os.getcwd()
    parent_path = os.path.dirname(local_path)
    print(parent_path)
    path = os.path.join( str(parent_path),"student_interview_data",candidate,"\")
    print(path)

    questions = open(r"./questions copy.json", 'r')
    q=json.load(questions)
    print(q)
    l_questions_text=[1,2]
    for q_id in q:
        evaluate_video(path+str(q[q_id])+"_reading")
        if(q_id in l_questions_text):
            
combine_f()