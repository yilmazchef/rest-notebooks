#!/usr/bin/env python


from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, UnknownLength
import os
import sys
import json
import time
import uuid
from folder_manager import notebook_file_paths
from docx_manager import to_docx, add_header, add_footer

if __name__ == "__main__":

    src_path = input(
        "Please paste here the absolute path of the root folder: "
    )

    if src_path == "":
        src = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

    source_file_list = notebook_file_paths(src_path, ".md")

    pBarMax = len(source_file_list)
    widgets = [Percentage(),
               ' ', Bar(),
               ' ', ETA(),
               ' ', AdaptiveETA()]
    pBar = ProgressBar(widgets=widgets, maxval=pBarMax)

    pBar.start()
    pBarCount = 0
    for source_file in source_file_list:

        to_docx(source_file)

        pBarCount += 1
        pBar.update(pBarCount)

    pBar.finish()
