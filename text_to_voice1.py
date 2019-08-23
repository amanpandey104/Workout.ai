import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voices = engine.getProperty('voices')
engine.setProperty('rate',123)
engine.setProperty('volume',1.0)
engine.setProperty('voice',voices[0].id)

keypoint_score_Nose= 0.35
keypoint_score_LEye= 0.134
keypoint_score_REye= 0.134
keypoint_score_LEar= 0.34556
keypoint_score_REar= 0.2
keypoint_score_LShoulder= 0.35
keypoint_score_RShoulder= 0.35
keypoint_score_LElbow= 0.15
keypoint_score_RElbow= 0.5
keypoint_score_LWaist= 0.334
keypoint_score_RWaist= 0.35
keypoint_score_LHip= 0.003
keypoint_score_RHip= 0.1
keypoint_score_LKnee= 0.15
keypoint_score_RKnee= 0.55
keypoint_score_LAnkle= 0.45
keypoint_score_RAnkle= 0.15

#Left Side of Body
if keypoint_score_LAnkle>0.25:
    engine.say("Your Left Ankle is not in correct position")
if keypoint_score_LKnee>0.25:
    engine.say("Your Left knee is not in correct position")
if keypoint_score_LHip>0.25:
    engine.say("Your Left Hip is not in correct position")
if keypoint_score_LWaist>0.25:
    engine.say("Your Left Waist is not in correct position")
if keypoint_score_LElbow>0.25:
    engine.say("Your Left Elbow is not in correct position")
if keypoint_score_LShoulder>0.25:
    engine.say("Your Left Shoulder is not in correct position")

#Right Side of Body
if keypoint_score_RAnkle>0.25:
    engine.say("Your Right ankle is not in correct position")
if keypoint_score_RKnee>0.25:
    engine.say("Your Right Knee is not in correct position")
if keypoint_score_RHip>0.25:
    engine.say("Your Right hip is not in correct position")
if keypoint_score_RWaist>0.25:
    engine.say("Your Right Waist is not in correct position")
if keypoint_score_RElbow>0.25:
    engine.say("Your Right Elbow is not in correct position")
if keypoint_score_RShoulder>0.25:
    engine.say("Your Right Shoulder is not in correct position")

engine.runAndWait()
