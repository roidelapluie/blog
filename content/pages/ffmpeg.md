Title: ffmpeg tips and tricks

Getting info of a video

    :::text
    ffprobe video.avi

Audio: from 5.1 to stereo

    :::text
    ffmpeg -i video.avi -ac 2 out.avi

Video: xvid

    :::text
    ffmpeg -i video.avi -c:v libxvid output.avi

Quality

    :::text
    ffmpeg -i video.avi -q:vscale 7 -q:ascale 7 output.avi
