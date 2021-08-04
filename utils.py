import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
def check_directory():
    for dir in os.listdir(SCRIPT_DIR):
        if dir == "videos":
            return True
    return False

def get_videos_dict():
    vid_dict = {}
    if check_directory() == False:
        return False
    for vid in os.listdir(os.path.join(SCRIPT_DIR, "videos")):
        vid_dict[vid] = os.path.join(SCRIPT_DIR, "videos", vid)
    
    return vid_dict       
    














