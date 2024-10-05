from pytube import YouTube, Playlist
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
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
    link3 = input("Tené en cuenta que esta opción SOLO ACEPTA videos a 1080 y 30fps.El tiempo de descarga depende de tu procesador y el largo del video\n\nPoné enter solo para volver atras\nIngresa el link: \n>> ")
    if link3 ==  '':
        os.system("cls")
        opcion()
    else:
        link3 = YouTube(link3)
        video1080 = link3.streams.filter(res="1080p").desc().first()

        os.system("cls")
        if video1080 == None:
            print("El video no tiene opción 1080p 30fps")
            os.system("pause")
        else:
            videodescargado=video1080.download(output_path=ruta)
            os.rename(videodescargado,ruta+"/video TEMP.mp4")
    
            audio1080 = link3.streams.filter(only_audio=True).first()
            elaudio=audio1080.download(output_path=ruta)
            os.rename(elaudio, ruta+"/audio TEMP.mp3") 


            #titulo = str(input("indica el nombre que quieras ponerle al archivo: \n>>"))
            titulo = video1080.title        
            for i in bad_chars:
                titulo = titulo.replace(i, '')
    

            os.system("cls")
            print("IMPORTANTE: Si interrumpis este proceso cerrando el programa, se te van a quedar archivos de audio y video temporales en la carpeta de descargas,\nborralos para evitar errores al volver a ejecutar el programa (y por comodidad)\n\n")

            # Open the video and audio
            video_clip = VideoFileClip(ruta+"/video TEMP.mp4")
            audio_clip = AudioFileClip(ruta+"/audio TEMP.mp3")
            final_clip = video_clip.set_audio(audio_clip)
            final_clip.write_videofile(ruta+"/"+titulo + ".mp4",threads = 8)	


            os.system("cls")
            os.remove(ruta+"/audio TEMP.mp3")
            os.remove(ruta+"/video TEMP.mp4")
            print("Listo. Podes encontrar el video '",titulo,"' en la carpeta de descargas")
            delay()
            os.system("cls")
            opcion()


def audio(): #Audio download
    # url input from user 
    audio = input("Poné enter solo para volver atras\nIngresa el link: \n>> ")
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
        print("Ya tenes en la carpeta de descargas el audio de '",titulo_audio,"'.")

        delay()
        os.system("cls")
        opcion()

def sieteveinte(): #Download videos at 720p 30fps
    link2 = input("Poné enter solo para volver atras\nIngresa el link: \n>> ") 
    if link2 == '':
        os.system("cls")
        opcion()
    else:
        link2 = YouTube(link2)

        video720= link2.streams.get_highest_resolution().download(output_path=ruta)
        titulo_video= link2.title
        for i in bad_chars:
            titulo_video = titulo_video.replace(i, '')

        # result of success 
        print("Ya tenes en la carpeta de descargas el video",titulo_video,)
        delay()
        os.system("cls")
        opcion()

def PLaudio(): #Download all the audio files from a playlist

    playlist = input("Poné enter solo para volver atras\nIngresa el link: \n>> ")
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
            print(tit_audPL +" Descargado") 

        print("\n\nTodos los audios de la playlist están en la carpeta de Descargas.")
        delay()
        os.system("cls")
        opcion()

def opcion(): #menu
    
    opc = str(input("QUÉ QUERES HACER?\n1- Descargar audio\n2- Descargar video en 720p\n3- Descargar video en 1080p30 (Esta tarda bastante)\n0- Salir\n>> "))
    while opc != "0": 
        if opc == "1" or opc == "2" or opc == "3":  
            if opc == "1":
                os.system("cls")
                opc2 = str(input("1- Un solo video\n2- Una playlist\n0- Atrás\n>> "))
                while opc2 != "0":
                    if opc2 == "1" or opc2 == "2":
                        if opc2 == "1":
                            try:
                                os.system("cls")
                                audio()
                            except:
                                os.system("cls")
                                print("Error. Posibilidades:\n\n-El link no es de youtube\n-El link es privado\n-Estas queriendo descargar un archivo que ya existe")
                                os.system("pause")
                        elif opc2 == "2":
                            try:
                                os.system("cls")
                                PLaudio()
                            except:
                                os.system("cls")
                                print("Error. Posibilidades:\n\n-El link no es de youtube\n-El link es privado\n-Estas queriendo descargar un archivo que ya existe")
                                os.system("pause")   
                    else:
                        os.system("cls")
                        opc2 = str(input("INGRESÁ UN ELEMENTO VÁLIDO\n1- Un solo video\n2- Una playlist\n0- Atrás\n>> "))
                os.system("cls")
                opcion()      
            
            
            elif opc == "2":
                try:
                    os.system("cls")
                    sieteveinte()
                except:
                    os.system("cls")
                    print("Error. Posibilidades:\n\n-El link no es de youtube\n-El link es privado\n-Estas queriendo descargar un archivo que ya existe")
                    os.system("pause")       
            
            elif opc == "3":
                try:
                    os.system("cls")
                    milochenta()
                except:
                    os.system("cls")
                    print("Error. Posibilidades:\n\n-El link no es de youtube\n-El link es privado\n-Estas queriendo descargar un archivo que ya existe")
                    os.system("pause")   

        else:
            os.system("cls")
            opc = str(input("INGRESÁ UN ELEMENTO VÁLIDO\n1- Descargar audio\n2- Descargar video en 720p\n3- Descargar video en 1080p30 (Esta tarda bastante)\n0- Salir\n>> "))
    if opc =="0":
        quit()



#inicio del programa
opcion()