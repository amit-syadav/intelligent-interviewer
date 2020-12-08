import os
import json
from components.video import eye_tracker,face_spoofing,head_pose_estimation
from components.video import mouth_distance,person_and_phone
from components.text.src import text_main
from components.audio import testpro
from components.audio import audio_main
from components.video.Emotion_detection.src import emotions
#import main
def evaluate_video(path,result):
    result["eye_tracker"].append(eye_tracker.eye_tracker_f(path))
    result["face_spoofing"].append(face_spoofing.face_spoofing_f(path))
    result["head_pose"].append(head_pose_estimation.head_pose_estimation_f(path))
    result["mouth_distance"].append(mouth_distance.mouth_distance_f(path))
    result["emotions"].append(emotions.emotions_f(path))
    print(result)

def combine_f(candidate="keval@gmail"):
    result={
        "eye_tracker":[],
        "face_spoofing":[],
        "head_pose":[],
        "mouth_distance":[],
        "emotions":[],
        "text":[],
        "audio":[[],[],[],[]]
    }
    local_path = os.getcwd()
    parent_path = os.path.dirname(local_path)
    #print(parent_path)
    c = os.path.join(str(parent_path),"student_interview_data",candidate)
    c=c+"\\"
    print("printing c"+c)
    questions = open(r"./questions.json", 'r')
    q=json.load(questions)
    l_questions_text=["4"]
    for q_id in q:
        print(q_id,end="\n")
        print(c+str(q_id)+"_reading.avi")
        evaluate_video(c+str(q_id)+"_reading.avi",result)
        evaluate_video(c+str(q_id)+"_answering.avi",result)
        Gend_value, bal_value, pronoun_value, acc_value=testpro.speech_analysis(c+str(q_id)+"_answering.wav")
        result["audio"][0].append(Gend_value)
        result["audio"][1].append(bal_value)
        result["audio"][2].append(pronoun_value)
        result["audio"][3].append(acc_value)
        if(q_id in l_questions_text):
            result["text"].append(text_main.text_analysis(c+str(q_id)+"_answering.wav"))
    
    with open(c+'result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
#combine_f(student_folder_directory)
combine_f()