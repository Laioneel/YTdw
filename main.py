from pytubefix import YouTube, Playlist
from moviepy import  VideoFileClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip
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




def milochenta(): #Download at 1080p 30fps
    link3 = input("Remember to only use videos at 1080p 30fps.\n\n Raw input to return\nLink: \n>> ")
    if link3 ==  '':
        os.system("cls")
        opcion()
    else:
        link3 = YouTube(link3)
        video1080 = link3.streams.filter(res="1080p")
        input(print(video1080))

        os.system("cls")

        videodescargado=video1080.get_by_itag(299).download(output_path=ruta, filename= 'video temp.mp4')
        #os.rename(videodescargado,ruta+"/video TEMP.mp4")

        audio1080 = link3.streams.filter(only_audio=True).first()
        elaudio=audio1080.download(output_path=ruta, filename='audio temp.m4a')
        #os.rename(elaudio, ruta+"/audio TEMP.mp3") 


        #titulo = str(input("indica el nombre que quieras ponerle al archivo: \n>>"))
        titulo = video1080.title        
        for i in bad_chars:
            titulo = titulo.replace(i, '')


        os.system("cls")
        print("This might take a while depending on your pc.\nWARNING: temporal files might stay in the download's folder if this process interrupts")

        # Open the video and audio
        video_clip = VideoFileClip(ruta+"/video temp.mp4")
        audio_clip = AudioFileClip(ruta+"/audio temp.m4a")
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile('termino.mp4')	


        os.system("cls")
        os.remove(ruta+"/audio temp.m4a")
        os.remove(ruta+"/video temp.mp4")
        print("",titulo," already on download's folder.")
        delay()
        os.system("cls")
        opcion()


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

def sieteveinte60(): #Download videos at 720p 60fps
    link2 = input("Raw input to go back.\nLink: \n>> ") 
    if link2 == '':
        os.system("cls")
        opcion()
    else:
        link2 = YouTube(link2)
            

        streamsVid= link2.streams.filter(adaptive= True, res='720p')
        input(print(streamsVid))
        streamsAudio= link2.streams.filter(adaptive= True, mime_type="audio/mp4")
        input(print(streamsAudio))

        video_stream= ffmpeg.input(link2.streams.get_by_itag(298).download(output_path=ruta, filename= 'video temp.mp4'))
        audio_stream = ffmpeg.input(link2.streams.get_by_itag(140).download(output_path=ruta, filename='audio temp.m4a'))
        titulo_video= link2.title
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
    opc = str(input("1- Download audio\n2- Download 720p60 video\n3- Download 1080p30 video\n0- Exit\n>> "))
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
                    sieteveinte60()
                except:
                    os.system("cls")
                    print("Error. Check if:\nIt's a YouTube link\nThe video it's private\nExists a file with the same name in the folder.")
                    os.system("pause")   

                    
            elif opc == "3":
                try:
                    os.system("cls")
                    milochenta()
                except:
                    os.system("cls")
                    print("Error. Check if:\nIt's a YouTube link\nThe video it's private\nExists a file with the same name in the folder.")
                    os.system("pause")   

        else:
            os.system("cls")
            opc = str(input("Wrong option\n1- Download audio\n2- Download 720p video\n3- Download 1080p30 video\n0- Exit\n>> "))
    if opc =="0":
        quit()



#Starup
opcion()
