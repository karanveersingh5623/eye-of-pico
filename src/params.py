"""Set Parameters for the APP here...."""

import os

MAIN_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

"""General Parameters"""
# BROADCAST KNOWN FACE ENCODINGS OR PEOPLE TO FIND
TARGET_FACE_TOPIC = "target-face-topic"
# TOPIC USED TO PUBLISH ALL FRAME OBJECTS
FRAME_TOPIC = "raw-frame-topic"
# TOPIC USED TO PUBLISH ALL FRAME OBJECTS
PROCESSED_FRAME_TOPIC = "processed-frame-topic"
ORIGINAL_PREFIX = "predicted"
PREDICTED_PREFIX = "predicted"
# PREDICTION TOPIC PREFIX, EACH CAMERA GETS NEW TOPIC FOR PUBLISHED PREDICTIONS
PREDICTION_TOPIC_PREFIX = "{}_{}".format("predicted_object", FRAME_TOPIC)

"""Performance Parameters"""
# USE RAW CV2 STREAMING or FAST BUT LESS FRAMES
USE_RAW_CV2_STREAMING = False
# TOPIC PARTITIONS
SET_PARTITIONS = 16
# PARTITIONER
ROUND_ROBIN = False

"""Demo Specific Parameters"""
LOG_DIR = "logs"
CLEAR_PRE_PROCESS_TOPICS = True
# ENDPOINT FOR VIDEO STREAMS: URL WHERE VIDEOS ARE HOSTED
C_FRONT_ENDPOINT = "http://194.167.137.11:32599"
# CAMERA URL INDEXES: Videos are named as number.mp4 where number is in following list
CAMERAS = [0]
# TOTAL CAMERAS TO BE USED --> USED FOR FULL URL
TOTAL_CAMERAS = len(CAMERAS)

HM_PROCESSESS = SET_PARTITIONS // 8