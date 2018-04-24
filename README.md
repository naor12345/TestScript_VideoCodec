# TestScript_VideoCodec
python script for hevc video coding test

These script is running on linux with python 3.
Folder stucture:
Test
 |-  cfg: cfg of yuv sequences
 |-  per-sequence: config files of each yuv sequences
 |-  cmdtxt: command txt files, sequences for test
 |-  runable: executable files of encoder
 |-  script: folders containing py test scripts
 |-  Result: log for test result
 |

### An example of command txt (all.txt)
ClassB BasketballDrive\_1920x1080\_50.yuv
ClassB BQTerrace\_1920x1080\_60.yuv
ClassB Cactus\_1920x1080\_50.yuv
ClassB Kimono\_1920x1080\_24.yuv
ClassB ParkScene\_1920x1080\_24.yuv
ClassC BasketballDrill\_832x480\_50.yuv
ClassC BQMall\_832x480\_60.yuv
ClassC PartyScene\_832x480\_50.yuv
ClassC RaceHorsesC\_832x480\_30.yuv
ClassD BasketballPass\_416x240\_50.yuv
ClassD BlowingBubbles\_416x240\_50.yuv
ClassD BQSquare\_416x240\_60.yuv
ClassD RaceHorses\_416x240\_31.yuv
ClassE FourPeople\_1280x720\_60.yuv
ClassE Johnny\_1280x720\_60.yuv
ClassE KristenAndSara\_1280x720\_60.yuv
