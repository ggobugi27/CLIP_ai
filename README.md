# CLIP ai

*TECH in entertainment*

Have you ever wanted to optimize video watching experience by cutting out parts you don't want? Clip will smartly curate through the clip and remove all the parts you don't need to watch

## Motivated

CLIP is motivated by a business idea pitch at CJ E&M to implement image recognition on a video platform to provide optimal user experience.

## Description

CLIP is an AI that is trained for selected individuals, and runs facial recognition on youtube videos to provide users with more optimized contents such as video clips on each individual, and image files of video frames with recognized individual. 

## Features 

User can select a youtube video on webpage, and CLIP video or images. 
When CLIP video is selected, CLIP subclips the video for each individual so the user can experience optimal video consumption. When CLIP image is selected, CLIP provides collection of images where a face is detected and the name of individual.


## Tech / Framework Used

Python modules are used for video processing. OpenCV is used to capture video frames, face_recognition is used to detect a face, Tensorflow is used to recognize an individual, and moviepy is used to write a video file of subclips. 

Node.js is used to create server. Python-shell module was used to run python scripts with arguments, Express.js to set up routes, Nunjucks to display responsive front-end.

Lastly, youtube API is used for video display and to get video url.  


## How to use

```
git clone https://github.com/ggobugi27/CLIP_ai
cd web
node app.js
```
Now connect to localhost guided in the command line. 
Play the youtube video and click on CLIP IMAGES button. 
Play the youtube video and click on CLIP VIDEO button. 

