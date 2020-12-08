import os
import json
from components.video import eye_tracker,face_spoofing,head_pose_estimation
from components.video import mouth_distance,person_and_phone
from components.text.src import text_main
#from components.audio import testpro
#from components.audio import audio_main
from components.video.Emotion_detection.src import emotions
import main
def evaluate_video(path,result):
    result["eye_tracker"]+=eye_tracker.eye_tracker_f(path)
    result["face_spoofing"]+=face_spoofing.face_spoofing_f(path)
    result["head_pose"]+=head_pose_estimation.head_pose_estimation_f(path)
    result["mouth_distance"]+=mouth_distance.mouth_distance_f(path)
    result["emotions"]+=emotions.emotions_f(path)

def combine_f(candidate="tejas@gmail"):
    result={
        "eye_tracker":0,
        "face_spoofing":0,
        "head_pose":0,
        "mouth_distance":0,
        "emotions":0,
        "text":0,
        "audio":0
    }
    local_path = os.getcwd()
    parent_path = os.path.dirname(local_path)
    print(parent_path)
    path = os.path.join( str(parent_path),"student_interview_data",candidate,"\")
    print(path)
    questions = open(r"./questions copy.json", 'r')
    q=json.load(questions)
    print(q)
    l_questions_text=[4]
    for q_id in q:
        evaluate_video(path+str(q[q_id])+"_reading.avi",result)
        evaluate_video(path+str(q[q_id])+"_answering.avi",result)
        #result["audio"]+=
        #if(q_id in l_questions_text):
            #result["text"]+=text_main.text_analysis(path+str(q[q_id])+"_answering.wav",result)
    
    with open(path+'result.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
combine_f()