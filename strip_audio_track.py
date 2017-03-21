#!/usr/bin/env python3

'''Strip audio track from a file using ffmpeg (creating a copy called
orig-silent.<orig>). ffmpeg is available in most command line package
managers.'''

from sys import argv
from os import path
# Only introduced in 3.5
from subprocess import run

try:
    vidnames = argv[1:]
except IndexError:
    print('Strip audio to a silent copy: \n',
          '$ strip_audio_track.py <orig.mp4> [more.mp4]')

strip_str = 'ffmpeg -i {} -an -c:v copy {}'
for vidname in vidnames:
    newname, ext = path.splitext(vidname)
    newname += '-silent' + ext

    run(strip_str.format(vidname, newname).split())
