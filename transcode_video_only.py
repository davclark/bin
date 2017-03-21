#!/usr/bin/env python3

'''Strip audio track from a file using ffmpeg, converting audio to mp4 using
h.264 coded (creating a copy called orig-silent.mp4). ffmpeg is available in
most command line package managers.'''

from sys import argv
from os import path
# Only introduced in 3.5
from subprocess import run

try:
    vidnames = argv[1:]
except IndexError:
    print('Strip audio to a silent mp4-transcoded copy: \n',
          '$ transcode_video_only.py <orig.vid> [more.vid]')

conv_str = 'ffmpeg -i {} -an -c:v libx264 -preset slow {}'
for vidname in vidnames:
    newname, _ = path.splitext(vidname)
    newname += '-silent.mp4'

    run(conv_str.format(vidname, newname).split())
