import gzip
import os
import subprocess


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

        newi = i.split('.')
        newi = newi[0]

        destiny_file = "Sample_freqs\\" + newi + ".freqs"

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

    fc = gzip.open('Compressed_files\\test.freqs', 'wb')
    fc.write(cf)
    fc.close()


def NCD():

    compr_concat_files = os.listdir("Compressed_concat_files")

    ncd_list = []

    for i in compr_concat_files:

        aux = i.split("_")

        first_file = aux[0]
        second_file = aux[1]

        concat_size = os.path.getsize("Compressed_concat_files\\" + i)

        first_file_size = os.path.getsize("Compressed_files\\" + first_file)
        second_file_size = os.path.getsize("Compressed_files\\" + second_file)

        ncd = (concat_size - min(first_file_size, second_file_size)) / max(first_file_size, second_file_size)

        ncd_list.append([ncd, first_file,second_file])

    ncd_list = sorted(ncd_list, key = lambda x: x[0])

    return ncd_list[0]

if __name__ == '__main__':

    file_name = "test.wav" #will be passed as arg by terminal

    path = "Test\\" + file_name

    execute_getMaxFreqs(path)

    ncd = NCD()

    print(ncd) #i dont understand why the bit size of the files varies




