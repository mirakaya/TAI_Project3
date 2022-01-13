import os
import subprocess

#subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-nf", "getMaxFreqs\\src\\test.wav"])
import wave


def execute_getMaxFreqs(pathSoundFile):
    '''Usage: GetMaxFreqs[-v(verbose)]
    [-w freqsFile]
    [-ws winSize]
    [-sh shift]
    [-ds downSampling]
    [-nf nFreqs]
    AudioFile'''



    subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-w", "Test\\test.freqs", pathSoundFile]) #gets freqs for all the test file

    path = "Sample_freqs"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print("The new directory is created!")

    list_Samples = os.listdir("Samples")


    for i in list_Samples: #gets freqs for all the sample files

        #print(i)

        newi = i.split('.')
        newi = newi[0]
        #str(newi)

        destiny_file = "Sample_freqs\\" + newi + ".freqs"

        #print(destiny_file)
        sample_file = "Samples\\" + i

        subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-w", destiny_file , sample_file]) #erro

    #concatenate files

    #subprocess.Popen(r"sox.exe")

    #compress files

    with open(pathSoundFile, "rb") as test_freqs:

        test_freqs.read()

        











    #subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-v", pathSoundFile])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    file_name = "test.wav" #will be passed as arg by terminal

    path = "Test\\" + file_name

    execute_getMaxFreqs(path)

    #copy /b sample01.wav + sample02.wav a.wav



