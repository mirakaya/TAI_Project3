import gzip
import io
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

    path_sf = "Sample_freqs"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path_sf)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path_sf)

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

    path_cf = "Concat_files"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path_cf)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path_cf)



    list_Samples_Freqs = os.listdir("Sample_freqs")

    with open("Test\\test.freqs", "rb") as test_freqs:

        tf = test_freqs.read()

        for i in list_Samples_Freqs:

            with open("Sample_freqs\\" + i, "rb") as sample_freqs:

                sf = sample_freqs.read()

                with open("Concat_files\\" + "test.freqs" + "_"+ i, "wb") as end_file:

                    aux = bytes(tf) + bytes(sf)


                    end_file.write(aux)



    # compress files

    path_cssf = "Compressed_files"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path_cssf)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path_cssf)

    list_Concat_Files = os.listdir("Concat_files")

    for i in list_Concat_Files:

        with open("Concat_files\\" + i, "rb") as file_uncompressed:

            cf = file_uncompressed.read()

        fc = gzip.open('Compressed_concat_files\\' + i, 'wb')
        fc.write(cf)
        fc.close()

    for i in list_Samples_Freqs:

        with open("Sample_freqs\\" + i, "rb") as file_uncompressed:

            cf = file_uncompressed.read()

        fc = gzip.open('Compressed_files\\' + i, 'wb')
        fc.write(cf)
        fc.close()

    with open("Test\\test.freqs", "rb") as file_uncompressed:

        cf = file_uncompressed.read()

    fc = gzip.open('Compressed_files\\test_freqs', 'wb')
    fc.write(cf)
    fc.close()


def NCD():

    compr_files = os.listdir("Compressed_concat_files")

    for i in compr_files:

        aux = i.split("_")

        first_file = aux[0]
        second_file = aux[1]

        #look for them in compressed_files and check their size












        











    #subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-v", pathSoundFile])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    file_name = "test.wav" #will be passed as arg by terminal

    path = "Test\\" + file_name

    execute_getMaxFreqs(path)

    NCD()

    #copy /b sample01.wav + sample02.wav a.wav



