//
//  ViewController.h
//  MusicFinder
//  Refer to EZAudio Example https://github.com/syedhali/EZAudio
//

#import <UIKit/UIKit.h>


#include <EZAudio/EZAudio.h>
#include <AFNetworking.h>
#define AudioFilePath @"audio.wav"
#define ip @"192.168.*.*"
//make sure this one is the same as the server ip

@interface ViewController : UIViewController <EZAudioPlayerDelegate, EZMicrophoneDelegate, EZRecorderDelegate>

@property (nonatomic, weak) IBOutlet UILabel *currentTimeLabel;
@property (nonatomic, weak) IBOutlet EZAudioPlotGL *recordingAudioPlot;
@property (nonatomic, assign) BOOL isRecording;
@property (nonatomic, strong) EZMicrophone *microphone;
@property (nonatomic, strong) EZRecorder *recorder;
@property (nonatomic, weak) IBOutlet UILabel *recordingStateLabel;
@property (nonatomic, weak) IBOutlet UISwitch *recordSwitch;


- (IBAction)toggleRecording:(id)sender;

@end


