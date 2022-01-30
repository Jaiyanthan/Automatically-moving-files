import os
import shutil

#directory which has the files 
directory = r"C:\Users\Admin\Downloads"

#directory to where we are moving files
image_directory = r"C:\Users\Admin\Downloads\images"
video_directory = r"C:\Users\Admin\Downloads\videos"
pdf_directory = r"C:\Users\Admin\Downloads\pdf"
docx_directory = r"C:\Users\Admin\Downloads\docx"
books_directory = r"C:\Users\Admin\Downloads\books"
program_directory = r"C:\Users\Admin\Downloads\programs"
zip_directory = r"C:\Users\Admin\Downloads\zip"
others_directory = r"C:\Users\Admin\Downloads\other files"
music_directory = r"C:\Users\Admin\Downloads\music"

#for loop
for filename in os.listdir(directory):
    if filename.endswith('.pdf') or filename.endswith('.PDF'):
        os.rename(directory+'/'+filename, pdf_directory+'/'+filename)
    elif filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.PNG') or filename.endswith('JPEG') or filename.endswith(".SVG") or filename.endswith('.svg'):
        os.rename(directory+'/'+filename, image_directory+'/'+filename)
    elif filename.endswith('.mp4') or filename.endswith('.mkv') or filename.endswith('.MP4'):
        os.rename(directory+'/'+filename, video_directory+'/'+filename)
    elif filename.endswith('.doc') or filename.endswith('docx'):
        os.rename(directory+'/'+filename, docx_directory+'/'+filename)
    elif filename.endswith('.epub') or filename.endswith('.mobi'):
        os.rename(directory+'/'+filename, books_directory+'/'+filename)
    elif filename.endswith('.py') or filename.endswith('.js') or filename.endswith('.jsx'):
        os.rename(directory+'/'+filename, program_directory+'/'+filename)
    elif filename.endswith('.zip') or filename.endswith('.rar') or filename.endswith('.gr'):
        os.rename(directory+'/'+filename, zip_directory+'/'+filename)
    elif filename.endswith('.mp3') or filename.endswith('.wav'):
        os.rename(directory+'/'+filename, music_directory+'/'+filename)      
    else:
        print("Other file format:" + filename)
        os.rename(directory+'/'+filename, others_directory+'/'+filename)
