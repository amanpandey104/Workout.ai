import cv2 
import json
import pandas as pd
import cv2 as cv
import numpy as np
def subject_capture():
    #Input Prompt 
    inp=int(input("Please enter the Exercise you want to do :(1-4)"))
    cap1 = cv2.VideoCapture(r"C:\Users\movva\Desktop\ML\Workout.ai\model\examples\exercise\{}\{}.mp4".format(inp,inp))
    rat1, frame1 = cap1.read()
    frame_count = cap1.get(cv2.CAP_PROP_FRAME_COUNT)
    print(frame_count)
    cap = cv2.VideoCapture(0)

    (grabbed, frame) = cap.read()
    fshape = frame.shape
    fheight = fshape[0]
    fwidth = fshape[1]
    print  (fwidth , fheight)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(r'C:\Users\movva\Desktop\ML\Workout.ai\model\output\output.avi',fourcc, 23.0, (fwidth,fheight))
    
    while frame_count >2:
        ret, frame = cap.read()
        ret1, frame1 = cap1.read()
        if ret==True:

            # write the flipped frame
            out.write(frame)
            frame_count-=1
            try:
                cv2.imshow('frame',frame)
                cv2.imshow('frame1',frame1)
            except:
                pass
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    # Release everything if job is finished
    cap.release()
    cap1.release()
    out.release()
    cv2.destroyAllWindows()
    return inp


def cosine_compare(jpath1,jpath2):
    

    data1 = json.load(open(jpath1))
    data2 = json.load(open(jpath2))
    big_l1=[]
    big_l2=[]

    for i in data1:
        #print(i)
        ll=data1[i]['people'][0]['pose_keypoints_2d']
        ll=[ll[i:i+3] for i in range(0, len(ll), 3)]
        for x in range(len(ll)):
            ll[x].pop(2)
        big_l1.append(ll)
        
    for i in data2:
        #print(i)
        ll=data2[i]['people'][0]['pose_keypoints_2d']
        ll=[ll[i:i+3] for i in range(0, len(ll), 3)]
        for x in range(len(ll)):
            ll[x].pop(2)
        big_l2.append(ll)
    
    big_l1=(np.array(big_l1).astype('int64'))
    big_l2=(np.array(big_l2).astype('int64'))
    BODY_PARTS = {"Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4, "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8,
              "RKnee": 9, "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14, "LEye": 15, "REar": 16, "LEar": 17, "Background": 18}

    POSE_PAIRS = [["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"], ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
                  ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"]]

    PAIR_COLORS = [(230, 25, 75), (60, 180, 75), (255, 225, 25), (0, 130, 200), (245, 130, 48), (145, 30, 180), (70, 240, 240),
                   (240, 50, 230), (210, 245, 60), (250, 190, 190), (0, 128, 128), (230, 190, 255), (170, 110, 40)]
    
    
    
        

    def compare(frame_vectors, template_vectors):
        return [dot_or_none(i, t) for i, t in zip(frame_vectors, template_vectors)]


    def dot_or_none(vec1, vec2):
        return np.dot(vec1, vec2) if vec1 is not None and vec2 is not None else None

    def get_pose_vectors(points, pose_pairs, body_parts):
        normalized_vectors = []

        for pair in pose_pairs:

            part_from = pair[0]
            part_to = pair[1]

            id_from = body_parts[part_from]
            id_to = body_parts[part_to]

            if points[id_from].any() and points[id_to].any():

                vector = np.array(points[id_to]) - np.array(points[id_from])
                normalized_vectors.append(vector / np.linalg.norm(vector, axis=0))
            else:
                normalized_vectors.append(None)

        return normalized_vectors
    length = 0
    if len(big_l1) < len(big_l2):
        length = len(big_l1)
    else:
        length = len(big_l2)
    count = 0
    
    vec_list = []
    for a in range(length):
        vec = get_pose_vectors(big_l1[a],POSE_PAIRS,BODY_PARTS)
        vec1 = get_pose_vectors(big_l2[a],POSE_PAIRS,BODY_PARTS)
        comp = compare(vec,vec1)
        vec_list.append(comp)
        count+=1
    return vec_list


def voice(thr_counter,thr_val):
    import pyttsx3
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    voices = engine.getProperty('voices')
    engine.setProperty('rate',123)
    engine.setProperty('volume',1.0)
    engine.setProperty('voice',voices[1].id)
    dict1 = {}
    l=[["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"], ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
              ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"]]
    for k,v in zip(l,thr_counter):
        dict1[k[1]]=v
    print(dict1)
    #Left Side of Body
    if dict1['LAnkle']>thr_val:
        engine.say("Your Left Ankle is not in correct position")
        thr_counter[11]=0
    if dict1['LKnee']>thr_val:
        engine.say("Your Left knee is not in correct position")
        thr_counter[10]=0
    if dict1['LHip']>thr_val:
        engine.say("Your Left Hip is not in correct position")
        thr_counter[9]=0
    if dict1['LWrist']>thr_val:
        engine.say("Your Left Wrist is not in correct position")
        thr_counter[6]=0
    if dict1['LElbow']>thr_val:
        engine.say("Your Left Elbow is not in correct position")
        thr_counter[5]=0
    if dict1['LShoulder']>thr_val:
        engine.say("Your Left Shoulder is not in correct position")
        thr_counter[1]=0

    #Right Side of Body
    if dict1['RAnkle']>thr_val:
        engine.say("Your Right ankle is not in correct position")
        thr_counter[8]=0
    if dict1['RKnee']>thr_val:
        engine.say("Your Right Knee is not in correct position")
        thr_counter[7]=0
    if dict1['RHip']>thr_val:
        engine.say("Your Right hip is not in correct position")
        thr_counter[6]=0
    if dict1['RWrist']>thr_val:
        engine.say("Your Right Wrist is not in correct position")
        thr_counter[3]=0
    if dict1['RElbow']>thr_val:
        engine.say("Your Right Elbow is not in correct position")
        thr_counter[2]=0
    if dict1['RShoulder']>thr_val:
        engine.say("Your Right Shoulder is not in correct position")
        thr_counter[0]=0

    engine.runAndWait()
    return thr_counter



if __name__ == '__main__':
    inp = subject_capture()
    !python video_demo.py --video "C:\Users\movva\Desktop\ML\Workout.ai\model\output\output.avi" --outdir C:\Users\movva\Desktop\ML\Workout.ai\model\output\alphapose\ --save_video  --vis --format open --sp
    v_list = cosine_compare(r"C:\Users\movva\Desktop\ML\Workout.ai\model\output\alphapose\alphapose-results.json",r"C:\Users\movva\Desktop\ML\Workout.ai\model\examples\exercise\{}\alphapose-results.json".format(inp))
    thr = 0.8
    thr_counter = np.zeros(13) # counts for crossing threshold in a ccomparision


    #face_cascade = cv2.CascadeClassifier("C:/Users/Choudhary/haarcascades/haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(r"C:\Users\movva\Desktop\ML\Workout.ai\model\examples\exercise\{}\AlphaPose_{}.avi".format(inp,inp))
    #cap.set(cv2.CAP_PROP_FPS,2)
    rat, frame = cap.read()
    cap1 = cv2.VideoCapture(r"C:\Users\movva\Desktop\ML\Workout.ai\model\output\alphapose\AlphaPose_output.avi")
    #cap1.set(cv2.CAP_PROP_FPS,2)
    rat1, frame1 = cap1.read()
    count = 0
    for i in range(len(v_list)):
        """vecval = v_list[count]
        for x in range(vec)"""
        for j in range(len(v_list[count])):
            if v_list[count][j] <thr:
                thr_counter[j]+=1
        rat, frame = cap.read()
        rat1, frame1 = cap1.read()
        count+=1
        if(i%300==0):
            voice(thr_counter,75)# thr_val
        try:
            cv2.imshow('img',frame)
            cv2.imshow('img1',frame1)
        except:
            pass
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break


    cap.release()   
    cap1.release()    
    cv2.destroyAllWindows()