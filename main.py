from pytubefix import YouTube, Playlist
import ffmpeg
import os
import winreg
import time

def get_download_path():  #Returns local download folder path.

    if os.name == 'nt':
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')
ruta = get_download_path()

bad_chars = ['<', '>', ':', '"', '/','?', "*", '|'] 

def delay():
    time.sleep(3)




def audio(): #Audio download
    audio = input("Raw input to go back\nLink: \n>> ")
    if audio == '':
        os.system("cls")
        opcion()
    else:
        audio= YouTube(str(audio)) 

        # extract only audio 
        onlyaudio = audio.streams.get_audio_only()
        titulo_audio = audio.title
        for i in bad_chars:
            titulo_audio = titulo_audio.replace(i, '')


        # download the file 
        out_file = onlyaudio.download(output_path=ruta) 

        # save the file 
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file) 

        # result of success 
        print(titulo_audio,"'already on download's folder.")

        delay()
        os.system("cls")
        opcion()



def PLaudio(): #Download all the audio files from a playlist

    playlist = input("Raw input to go back\nLink: \n>> ")
    if playlist == '':
        os.system("cls")
        opcion()
    else:
        playlist = Playlist(playlist)

        # Loop through all videos in the playlist and download them
        for video in playlist.videos:
            pl = video.streams.get_audio_only()
            tit_audPL = pl.title
            for i in bad_chars:
                tit_audPL = tit_audPL.replace(i, '')
            archivo= pl.download(output_path=ruta, filename= tit_audPL+".mp3")
            print(tit_audPL +" Downloaded") 

        print("\n\nAll audio files will be on the Download's folder.")
        delay()
        os.system("cls")
        opcion()

def opcion(): #menu
    print(ruta)
    opc = str(input("DISCLAIMERS:Downloadings will last depending on your CPU. If the YT video is at 60fps, you wont be able to download it at 30, an viceversa.\n1- Download audio\n2- Download 720p video\n3- Download 1080p video\n0- Exit\n>> "))
    while opc != "0": 
        if opc == "1" or opc == "2" or opc == "3":  
            if opc == "1":
                os.system("cls")
                opc2 = str(input("1- One video\n2- Playlist\n0- Back\n>> "))
                while opc2 != "0":
                    if opc2 == "1" or opc2 == "2":
                        if opc2 == "1":
                            try:
                                os.system("cls")
                                audio()
                            except:
                                os.system("cls")
                                print("Error. Check if:\nIt's a YouTube link\nThe video it's private\nExists a file with the same name in the folder.")
                                os.system("pause")
                        elif opc2 == "2":
                            try:
                                os.system("cls")
                                PLaudio()
                            except:
                                os.system("cls")
                                print("Error. Check if:\nIt's a YouTube link\nThe video it's private\nExists a file with the same name in the folder.")
                                os.system("pause")   
                    else:
                        os.system("cls")
                        opc2 = str(input("Wrong option.\n1- One video\n2- Playlist\n0- Back\n>> "))
                os.system("cls")
                opcion()      
            
            
            elif opc == "2":
                try:
                    os.system("cls")
                    opc2=str(input('The video is in\n1- 30fps\n2- 60fps\n>>'))
                    if opc2 == '1':
                        os.system("cls")
                        video_download(136)   
                    elif opc2 == '2':
                        os.system("cls")
                        video_download(298)
                except:
                    os.system("cls")
                    print("Error. Check if:\nIt's a YouTube link\nThe video it's private\nExists a file with the same name in the folder.")
                    os.system("pause")   

                    
            elif opc == "3":
                try:
                    os.system("cls")
                    opc2=str(input('The video is in\n1- 30fps\n2- 60fps\n>>'))
                    if opc2 == '1':
                        os.system("cls")
                        video_download(399)
                    elif opc2 == '2':
                        os.system("cls")
                        video_download(299)
                except:
                    os.system("cls")
                    print("Error. Check if:\nIt's a YouTube link\nThe video it's private\nExists a file with the same name in the folder.")
                    os.system("pause")   

        else:
            os.system("cls")
            opc = str(input("Wrong option\n1- Download audio\n2- Download 720p video\n3- Download 1080p30 video\n0- Exit\n>> "))
    if opc =="0":
        quit()

#vidTag: 136: 720p30, 399: 1080p30, 298: 720p60, 299: 1080p60

def video_download(vidTag):
    yt = input("Raw input to go back.\nLink: \n>> ") 
    if yt == '':
        os.system("cls")
        opcion()
    else:
        os.system("cls")
        yt = YouTube(yt)
            

        video_stream= ffmpeg.input(yt.streams.get_by_itag(vidTag).download(output_path=ruta, filename= 'video temp.mp4'))
        audio_stream = ffmpeg.input(yt.streams.get_by_itag(140).download(output_path=ruta, filename='audio temp.m4a'))
        titulo_video= yt.title
        #video_stream= video720.download()
        #audio_stream= audio720.download()
        for i in bad_chars:
            titulo_video = titulo_video.replace(i, '')
        output_file= ruta + '/' + titulo_video + '.mp4'

        ffmpeg.output(audio_stream, video_stream,output_file).run()
        os.system("cls")
        os.remove(ruta+"/audio temp.m4a")
        os.remove(ruta+"/video temp.mp4")
        #result of success 
        print(titulo_video, "already on Download's folder.")
        delay()
        os.system("cls")
        opcion()


#Starup
opcion()
