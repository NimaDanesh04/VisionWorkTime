# VisionWorkTime: Computer Vision-Based Worker Hour Tracker

This project implements a computer vision pipeline that automatically estimates how long a worker has worked based on video input. It leverages deep learning models built with **TensorFlow** to detect worker presence and track their active duration.

---

## Overview
The goal of this project is to automate the process of measuring work hours by using visual data. Traditional time-tracking systems require manual input or wearable devices — this system eliminates that need by relying purely on computer vision.

The pipeline processes video footage, identifies the worker, and calculates the total duration of active presence.

---

## ⚙️ Features
- Detects and tracks workers in a video feed.  
- Calculates total work time automatically.  
- Uses TensorFlow-based deep learning models for detection and analysis.  
- Can be extended to multiple workers or real-time video feeds.

---

##  How It Works
1. The system takes input from a recorded or live video stream.  
2. It runs detection and tracking models to identify the worker.  
3. Based on time intervals when the worker is visible, it estimates total working hours.  


# this is the outpit of model for the video
[🎬 Watch Demo](https://github.com/NimaDanesh04/VisionWorkTime/blob/main/prediction/output_video5.mp4)
