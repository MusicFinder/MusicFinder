# MusicFinder

Project of music recognition

### File Description

* algorithm_code: code for preprocessing data
* MusicFinder: iOS App code for recording, documents [here](https://github.com/syedhali/EZAudio) 
* server.ipynb: the server code to perform music identification 

### Package Requirement

* Python2.7
* Xcode
* [openCV >= 3.0](https://opencv.org): `sudo pip install opencv-python `, `sudo pip install opencv-contrib-python `
* [dejavu](https://github.com/worldveil/dejavu/blob/master/INSTALLATION.md): `pip install PyDejavu`
* [librosa](https://librosa.github.io/librosa/install.html): `pip install liborsa`
* [pydub](https://github.com/jiaaro/pydub#installation): `pip install pydub` 

### Set Up

1. Run mySQL server `mysql.server start`
2. Modify the config of dejavu to make it connect to your local database
3. Run `djv.fingerprint_directory("your wav data directory", [".wav"])` to generate fingerprint
4. Generate mel-spectrogram then SURF descriptor using code in /algorithm_code and put the SURF descriptor into '/graph' directory
 * step 3 and 4 canbe skiped by directly downloading the preprocessed results of our data [see our homepage](https://musicfinder.github.io/MusicFinder/)
5. Use the MusicFinder.xcworkspace to open the iOS App
6. Modify the ip address in server and iOS APP ViewController.h to be the same valid address 

