# -*- coding: utf-8 -*-

import json
import os.path
import re

originalPathTarget = r'C:\...........\extrator-excel-json\file-en.json'
parsedPathTarget = r'C:\...........\extrator-excel-json\file-en-parsed.json'

if os.path.isfile(originalPathTarget) and os.path.isfile(parsedPathTarget):
    with open(originalPathTarget) as originalFile, open(parsedPathTarget, "w") as parsedFile:
        linesOriginalFile = originalFile.readlines()
        for i in range(0, len(linesOriginalFile)):
            lineOriginalFile = linesOriginalFile[i] 
            if "{" in lineOriginalFile or "}" in lineOriginalFile:
                parsedFile.write(lineOriginalFile)
            else:
                qlist = re.findall('\"(.*?)\"', lineOriginalFile)
                print(qlist)

                if len(qlist) == 0:
                # se for uma linha em branco
                    parsedFile.write(lineOriginalFile)
                else:
                # se for uma linha com conteúdo
                    if (i < len(linesOriginalFile)+1): 
                        if "}" in linesOriginalFile[i+1]: 
                            parsedFile.write("\"" + qlist[0] + "\": \"" + qlist[1] + "\"\n")
                        else:
                            parsedFile.write("\"" + qlist[0] + "\": \"" + qlist[1] + "\",\n")
                