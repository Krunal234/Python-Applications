from pytube import YouTube

video_url =input("Enter your Youtube video Link: ")
my_video = YouTube(str(video_url))
print("Video title is: ",my_video.title)
resolutionList = ['144p','360p','480p','720p','1080p']
for resolution in resolutionList:
    try:
        video = my_video.streams.filter(res=resolution).first()
        fileSize = int(video.filesize)
        fileSize/=1024
        fileSize/=1024
        
    except Exception as e:
        print("Not available")
    else:
        print(video.resolution," ",fileSize, " MB")
print("Now which resolution you want to download? ")
print("Enter your resolution in number+p format eg. 360p")
requestedResolution = input()

video = my_video.streams.filter(res = str(requestedResolution)).first()
video.download()
print("Your ",requestedResolution," quality Video is downloaded.")