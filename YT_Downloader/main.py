#!/usr/bin/env python3
import os

import PySimpleGUI as sg
import shutil
from pytube import YouTube

def download_file(link, path, format):
    try:
        if format == "mp3":
            yt = YouTube(link)
            video = yt.streams.filter(only_audio=True).first()
            downloaded_file = video.download(path)
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, new_file)
            sg.popup_ok("File downloaded!", title="Success")
        if format == "mp4":
            # Download Video
            mp4_video = YouTube(link).streams.filter().get_highest_resolution().download()
            # move file to selected directory
            shutil.move(mp4_video, path)
            sg.popup_ok("File downloaded!", title="Success")
    except:
        sg.popup_error("Something went wrong!\n(Maybe the file already downloaded or I have no permission to write here)", title="Error")

def percent(tem, total):
    perc = (float(tem) / float(total)) * float(100)
    return perc

def progress_function(stream, chunk, file_handle, bytes_remaining):

    size = stream.filesize
    p = 0
    while p <= 100:
        progress = p
        str(p) + '%'
        p = percent(bytes_remaining, size)
        window["-DOWNLOAD_PROGRESS_PERC-"].update(p)

layout = [
    [sg.Text("Enter YouTube url: "), sg.Input("", key="-URL-")],

    [sg.Radio("MP3", "TYPE", default=True, key="-TYPE-", ), sg.Radio("MP4", "TYPE", default=False, key="-TYPE-")],

    [sg.Text('Output Directory: '), sg.Input("Select output folder", do_not_clear=True, key='-OUT_DIR-', readonly=True), sg.FolderBrowse(target='-OUT_DIR-', key='_browse_out_dir_')],
    [sg.Button("Download")]
]

window = sg.Window("YouTube Downloader", layout, element_justification='c').Finalize()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Download':

        if values["-URL-"].strip() == "":
            sg.popup_error("You did not enter a URL!")

        if values["-OUT_DIR-"].strip() == "Select output folder":
            sg.popup_error("You did not select the output folder!")

        if values["-TYPE-"] == True:
            filetype = "mp3";
        else:
            filetype = "mp4";

        if values["-URL-"].strip() != "" and values["-OUT_DIR-"].strip() != "Select output folder":
            download_file(values["-URL-"].strip(), values["-OUT_DIR-"].strip(), filetype)