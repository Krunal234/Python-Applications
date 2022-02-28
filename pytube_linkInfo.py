from pytube import YouTube


video_url =input("Enter your Youtube video Link: ")
my_video = YouTube(str(video_url))
print("Video title is: ",my_video.title)
resolutionList = ['144p','360p','480p','720p','1080p']
print("Available Resolutions with audio: ")
# streamList = my_video.streams.filter(res='720p',progressive=True).first()

# print("Streams are : ",streamList)
for resolution in resolutionList:
    try:
        video = my_video.streams.filter(res=resolution,progressive=True).first()
        fileSize = int(video.filesize)
        fileSize/=1024
        fileSize/=1024
        
    except Exception as e:
        x = 0
    else:
        print(video.resolution," ",fileSize, " MB")
# print("Available Captions: ",my_video.captions.all())

# for e in my_video.captions.all():
#     captionList.append(e.code)
# for e in captionList:
#     print(e)
print("Now which resolution you want to download? ")
print("Enter your resolution in number+p format eg. 360p or write 'q' to end the process")
requestedResolution = input()
if(str(requestedResolution)=='q'):
    print("You Cancelled the download. Thank you for using this application")

else:
    video = my_video.streams.filter(res = str(requestedResolution),progressive=True).first()
    video.download()
    print("Your ",requestedResolution," quality Video is downloaded.")