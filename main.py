# -*- coding: utf-8 -*-

import json
import os.path
import re

originalPathTarget = r'.\file-en.json'
parsedPathTarget = r'.\file-en-parsed.json'

if os.path.isfile(originalPathTarget) and os.path.isfile(parsedPathTarget):
    with open(originalPathTarget) as originalFile, open(parsedPathTarget, "w") as parsedFile:
        linesOriginalFile = originalFile.readlines()
        for i in range(0, len(linesOriginalFile)):
            lineOriginalFile = linesOriginalFile[i] 
            if "{" in lineOriginalFile or "}" in lineOriginalFile:
                parsedFile.write(lineOriginalFile.replace("    ", ""))
            else:
                qlist = re.findall('\"(.*?)\"', lineOriginalFile)
                #print(qlist)

                if len(qlist) == 0:
                # se for uma linha em branco
                    parsedFile.write(lineOriginalFile)
                else:
                # se for uma linha com conteúdo
                    if (i < len(linesOriginalFile)+1):  

                        # print original line
                        print(lineOriginalFile)
                        
                        # remove json indentation
                        newValue = lineOriginalFile.replace("    ", "")

                        # remove break line
                        newValue = newValue.replace("\n", "")
                        
                        # generate the query string
                        stringToReplace = "\"" + qlist[0] + "\": \"" + qlist[1] + "\""
                        
                        # removes the query string from the original string
                        newValue = newValue.replace(stringToReplace, "")
                        
                        if(len(newValue) > 0):
                            if(newValue[0] == ","):
                                newValue = newValue.replace(",", "", 1)
                        
                        # removes tabulation
                        newValue = newValue.replace("\t", "")

                        # print the final result
                        print(newValue)


                        if "}" in linesOriginalFile[i+1]: 
                        # if it is the final of a block, there is no need of "," in the end
                            parsedFile.write("\"" + qlist[0] + "\": \"" + newValue + "\"\n")
                        else:
                        # if it isn't the final of a block, there is need of "," in the end
                            parsedFile.write("\"" + qlist[0] + "\": \"" + newValue + "\",\n")
       