//
//  ViewController.m
//  MusicFinder
//  Refer to EZAudio Example https://github.com/syedhali/EZAudio

#import "ViewController.h"

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];

    AVAudioSession *session = [AVAudioSession sharedInstance];
    
    //[session setMode:AVAudioSessionModeDefault error:nil];
    [session setCategory:AVAudioSessionCategoryRecord error:nil];
    [session setActive:YES error:nil];
    self.recordingAudioPlot.backgroundColor = [UIColor colorWithRed: 0.25 green: 0.7 blue: 0.9 alpha: 0.95];
    self.recordingAudioPlot.color = [UIColor colorWithRed: 0.9 green: 0.9 blue: 0.9 alpha: 0.95];
    self.recordingAudioPlot.plotType = EZPlotTypeBuffer;
    self.recordingAudioPlot.shouldMirror = YES;
    self.recordingAudioPlot.shouldFill = YES;
    
    
    self.microphone = [EZMicrophone microphoneWithDelegate:self];
    [session overrideOutputAudioPort:AVAudioSessionPortOverrideSpeaker error:nil];
    self.recordingStateLabel.text = @"Not Recording";


}

- (void)toggleRecording:(id)sender
{
    if ([sender isOn])
    {
        self.recordingStateLabel.text = @"Recording";
        [self.recordingAudioPlot clear];
        [self.microphone startFetchingAudio];
        self.recorder = [EZRecorder recorderWithURL:[self wavFilePathURL]
                                       clientFormat:[self.microphone audioStreamBasicDescription]
                                           fileType:EZRecorderFileTypeWAV
                                           delegate:self];
        self.isRecording = YES;
    }
    else
    {
        self.recorder.delegate = nil;
        self.isRecording = NO;
        [self.microphone stopFetchingAudio];
        self.recordingStateLabel.text = @"Not Recoding";
    }
}

-(void) upload
{
    self.recordSwitch.on = NO;
    self.recordingStateLabel.text = @"Identifying";
    NSURL *filePath = [self wavFilePathURL];
    NSData *audioData = [NSData dataWithContentsOfURL:filePath];
    NSString *dataStr = [audioData base64EncodedStringWithOptions: 4];
    //NSLog(@"%@", dataStr);
    //NSLog(@"%lu", dataStr.length);
    AFHTTPSessionManager * manager =[AFHTTPSessionManager manager];
    
    manager.responseSerializer.acceptableContentTypes = [NSSet setWithObject:@"text/plain"];
    manager.responseSerializer = [AFHTTPResponseSerializer serializer];
    NSDictionary *parameters = @{@"length":[NSString stringWithFormat:@"%lu", (unsigned long)dataStr.length], @"taudio" : dataStr};
    NSLog(@"Uploading");
    [manager POST:ip parameters:parameters progress:nil success:^(NSURLSessionDataTask * _Nonnull task, id _Nullable responseObject){
        NSLog(@"success");
        NSString* s = [[NSString alloc] initWithData: responseObject encoding:NSUTF8StringEncoding];
        UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Result" message:s delegate:nil   cancelButtonTitle:@"OK" otherButtonTitles:nil];
        alert.alertViewStyle = UIAlertViewStyleDefault;
        [alert show];
        NSLog(@"%@", s);
        
    } failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error) {
        NSLog(@"~~~~~~~~%@",error);
    }];
    
    
}

- (void)recorderUpdatedCurrentTime:(EZRecorder *)recorder
{
    NSString *formattedCurrentTime = [recorder formattedCurrentTime];
    dispatch_async(dispatch_get_main_queue(), ^{
        self.currentTimeLabel.text = formattedCurrentTime;
    });
    //NSLog(@"%@", formattedCurrentTime);
    if([formattedCurrentTime isEqualToString:@"00:07"]){
        self.isRecording = NO;
        self.recorder.delegate = nil;
        [self.microphone stopFetchingAudio];
        [self upload];
        
    }
}

- (NSURL *)wavFilePathURL
{
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *basePath = [paths objectAtIndex:0];
    return [NSURL fileURLWithPath:[NSString stringWithFormat:@"%@/%@",
                                   basePath,
                                   AudioFilePath]];
}


- (void)  microphone:(EZMicrophone *)microphone hasAudioReceived:(float **)buffer withBufferSize:(UInt32)bufferSize withNumberOfChannels:(UInt32)numberOfChannels
{
    
    dispatch_async(dispatch_get_main_queue(), ^{
        [self.recordingAudioPlot updateBuffer:buffer[0]
                                   withBufferSize:bufferSize];
    });
}

//------------------------------------------------------------------------------

- (void) microphone:(EZMicrophone *)microphone hasBufferList :(AudioBufferList*)bufferList withBufferSize:(UInt32)bufferSize
withNumberOfChannels:(UInt32)numberOfChannels
{
    if (self.isRecording)
    {
        [self.recorder appendDataFromBufferList:bufferList
                                 withBufferSize:bufferSize];
    }
}

//not used
/*
-(void)convetM4aToWav:(NSURL *)originalUrl  destUrl:(NSURL *)destUrl {
    
    AVURLAsset *songAsset = [AVURLAsset URLAssetWithURL:originalUrl options:nil];
    
    NSError *error = nil;
    
    AVAssetReader *assetReader = [AVAssetReader assetReaderWithAsset:songAsset error:&error];
    
    if(error) {
            
            NSLog
            (@"error: %@", error);
            
            return;
            
            
        }
    
    
    AVAssetReaderOutput *assetReaderOutput = [AVAssetReaderAudioMixOutput assetReaderAudioMixOutputWithAudioTracks:songAsset.tracks audioSettings: nil];
    
    if (![assetReader canAddOutput:assetReaderOutput])
    {
        
        NSLog (@"can't add reader output... die!");
        
        return;
        
    }
    
    [assetReader addOutput:assetReaderOutput];
    
    AVAssetWriter *assetWriter = [AVAssetWriter assetWriterWithURL:destUrl
                                                          fileType:AVFileTypeCoreAudioFormat error: &error];
    
    if (error) {
        
        NSLog (@"error: %@", error);
        
        return;
        
    }
    
    AudioChannelLayout channelLayout;
    
    memset(&channelLayout, 0, sizeof(AudioChannelLayout));
    
    channelLayout.mChannelLayoutTag = kAudioChannelLayoutTag_Stereo;
    
    NSDictionary *outputSettings = [NSDictionary dictionaryWithObjectsAndKeys:
                                    
                                    [NSNumber numberWithInt:kAudioFormatLinearPCM], AVFormatIDKey,[NSNumber
                                                                                                   numberWithFloat:16000.0], AVSampleRateKey, [NSNumber numberWithInt:2], AVNumberOfChannelsKey, [NSData dataWithBytes:&channelLayout length:sizeof(AudioChannelLayout)], AVChannelLayoutKey, [NSNumber numberWithInt:16], AVLinearPCMBitDepthKey,[NSNumber numberWithBool:NO],
                                    AVLinearPCMIsNonInterleaved,[NSNumber numberWithBool:NO],AVLinearPCMIsFloatKey,[NSNumber numberWithBool:NO], AVLinearPCMIsBigEndianKey,nil];
    
    AVAssetWriterInput *assetWriterInput = [AVAssetWriterInput assetWriterInputWithMediaType:AVMediaTypeAudio
                                                                              outputSettings:outputSettings];
    
    if ([assetWriter canAddInput:assetWriterInput]) {
        
        [assetWriter addInput:assetWriterInput];
        
    } else {
        
        NSLog (@"can't add asset writer input... die!");
        
        return;
        
    }
    
    assetWriterInput.expectsMediaDataInRealTime = NO;
    
    [assetWriter startWriting];
    
    [assetReader startReading];
    
    AVAssetTrack *soundTrack = [songAsset.tracks objectAtIndex:0];
    
    CMTime startTime = CMTimeMake (0, soundTrack.naturalTimeScale);
    
    [assetWriter startSessionAtSourceTime:startTime];
    
    __block UInt64 convertedByteCount = 0;
    
    dispatch_queue_t mediaInputQueue = dispatch_queue_create("mediaInputQueue", NULL);
    
    [assetWriterInput requestMediaDataWhenReadyOnQueue:mediaInputQueue usingBlock: ^{
        
        while (assetWriterInput.readyForMoreMediaData) {
            
            CMSampleBufferRef nextBuffer = [assetReaderOutput copyNextSampleBuffer];
            
            if (nextBuffer) {
                
                // append buffer
                
                [assetWriterInput appendSampleBuffer: nextBuffer];
                
                NSLog (@"appended a buffer (%zu bytes)",CMSampleBufferGetTotalSampleSize
                       (nextBuffer));
                
                convertedByteCount += CMSampleBufferGetTotalSampleSize
                (nextBuffer);
                
            } else {
                
                [assetWriterInput markAsFinished];
                
                [assetWriter finishWritingWithCompletionHandler:^{
                    
                }];
                
                [assetReader cancelReading];
                
                NSDictionary *outputFileAttributes = [[NSFileManager defaultManager]
                                                      attributesOfItemAtPath:[destUrl path] error:nil];
                
                NSLog (@"FlyElephant %lld",[outputFileAttributes fileSize]);
                
                break;
                
            }
            
        }
        
    }];
    
}
*/
@end
