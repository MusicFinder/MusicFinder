# MusicFinder

Project of music recognition

### File Description

* algorithm_code: code for preprocessing data
* MusicFinder: iOS App code for recording, documents [here](https://github.com/syedhali/EZAudio) 
* server.ipynb: the server code to perform music identification 

### Package Requirement

* Python2.7
* [openCV >= 3.0](https://opencv.org)
* [dejavu](https://github.com/worldveil/dejavu/blob/master/INSTALLATION.md) 
* [librosa](https://librosa.github.io/librosa/install.html)
* [pydub](https://github.com/jiaaro/pydub#installation)

### Set Up

* Run mySQL server
* Modify the config of dejavu to make it connect to your local database
** Run `djv.fingerprint_directory("your wav data directory", [".wav"])` to generate fingerprint
** Generate mel-spectrogram then SURF descriptor using code in /algorithm_code and put the SURF descriptor into '/graph' directory
* You can directly download required preprocessing results above [see our homepage](https://musicfinder.github.io/MusicFinder/)
* Use the MusicFinder.xcworkspace to open the iOS App
* Modify the ip address in server and iOS APP ViewController.h to be the same valid address 

