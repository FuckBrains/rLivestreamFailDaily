import os
from moviepy.editor import *
import datetime
def editClips():
    linenum = 0
    editedClips = [] 
    with open("dailyVideoData.txt",'r', encoding='utf-8') as fin: #save dailyVideoData as a list
        dailyVideoData = fin.readlines()
    #print(dailyVideoData)
    t = datetime.datetime.now()
    title = TextClip("The top clips of /r/Livestreamfail for " + t.strftime('%b %d, %Y'),fontsize=70,color='white',align='center')
    title = title.set_fps(60)
    title = title.set_duration(5)
    editedClips.append(title) #add title to edited clips list
    for line in dailyVideoData: 
        if(linenum%4 == 0): #if it is the video file name that was parsed 
            #print(linenum)
            vfc = VideoFileClip(line[:-1]) #grab the video file (minus the end line character)
            #print(dailyVideoData[linenum + 2] + " posted by: " + dailyVideoData[linenum+1])
            tc = TextClip(dailyVideoData[linenum + 2] + " posted by: " + dailyVideoData[linenum+1], fontsize=70,color='black',align="South", stroke_color='white')
            tc = tc.set_fps(60)
            tc = tc.set_duration(5)
            editedClips.append(CompositeVideoClip([vfc, tc])) #add the composite of the video and text to the clips list
        linenum+=1 #iteration
    final_clip = concatenate_videoclips(editedClips, method="compose") #concat edited clips together
    final_clip.write_videofile("dailyClips.mp4") 
    for clip in editedClips: #close all of our clips so we dont get in use errors
        clip.close()
    final_clip.close()



def deleteOldVideos():
    forDeletion = open("dailyVideoData.txt", "r") #read our text file for the last time

    linenum = 0 

    for line in forDeletion:
        if(linenum%4 == 0):
            os.remove(line[:-1]) #remove all the old downloaded videos
        linenum+=1
    forDeletion.close()
    os.remove("dailyVideoData.txt")


