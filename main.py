import os
import subprocess

#subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-nf", "getMaxFreqs\\src\\test.wav"])



def execute_getMaxFreqs(pathSoundFile):
    '''Usage: GetMaxFreqs[-v(verbose)]
    [-w freqsFile]
    [-ws winSize]
    [-sh shift]
    [-ds downSampling]
    [-nf nFreqs]
    AudioFile'''


    subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-nf", pathSoundFile])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    file_name = "test.wav" #will be passed as arg by terminal

    path = "Test\\" + file_name

    execute_getMaxFreqs(path)


