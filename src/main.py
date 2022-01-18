import gzip
import os
import subprocess
import time
import sys


def execute_getMaxFreqs(pathSoundFile):
    '''Usage: GetMaxFreqs[-v(verbose)]
    [-w freqsFile]
    [-ws winSize]
    [-sh shift]
    [-ds downSampling]
    [-nf nFreqs]
    AudioFile'''

    test_name = pathSoundFile.split("/")[-1].split(".")[0]
    subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-w", "Test\\"+test_name+".freqs", pathSoundFile], shell=True, stdout=subprocess.PIPE) #gets freqs for all the test file

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

        subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-w", destiny_file , sample_file], shell=True, stdout=subprocess.PIPE) #erro

def concatenate(list_Samples_Freqs):
    #concatenate files
    path_cf = "Concat_files"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path_cf)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path_cf)

    test_name = test_file.split(".")[0]
    with open("Test/"+test_name+".freqs", "rb") as test_freqs:

        tf = test_freqs.read()

        for i in list_Samples_Freqs:

            with open("Sample_freqs/" + i, "rb") as sample_freqs:

                sf = sample_freqs.read()
                with open("Concat_files/" + test_name+".freqs" + "_"+ i, "wb") as end_file:

                    aux = bytes(tf) + bytes(sf)
                    end_file.write(aux)

def compress(list_Samples_Freqs):

    # compress files
    path_cssf = "Compressed_files"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path_cssf)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path_cssf)

    list_Concat_Files = os.listdir("Concat_files")

    for i in list_Concat_Files:

        with open("Concat_files/" + i, "rb") as file_uncompressed:

            cf = file_uncompressed.read()

        if not os.path.exists('Compressed_concat_files'):
            os.makedirs('Compressed_concat_files')
        fc = gzip.open('Compressed_concat_files/' + i, 'wb')
        fc.write(cf)
        fc.close()

    for i in list_Samples_Freqs:

        with open("Sample_freqs/" + i, "rb") as file_uncompressed:

            cf = file_uncompressed.read()

        fc = gzip.open('Compressed_files/' + i, 'wb')
        fc.write(cf)
        fc.close()

    test_name = test_file.split(".")[0]
    with open("Test/"+test_name+".freqs", "rb") as file_uncompressed:

        cf = file_uncompressed.read()

    fc = gzip.open('Compressed_files/'+test_name+'.freqs', 'wb')
    fc.write(cf)
    fc.close()


def NCD(compr_concat_files):

    ncd_list = []

    for i in compr_concat_files:

        aux = i.split("_")

        first_file = aux[0]
        second_file = aux[1]

        concat_size = os.path.getsize("Compressed_concat_files/" + i)

        first_file_size = os.path.getsize("Compressed_files/" + first_file)
        second_file_size = os.path.getsize("Compressed_files/" + second_file)

        ncd = (concat_size - min(first_file_size, second_file_size)) / max(first_file_size, second_file_size)

        ncd_list.append([ncd, first_file,second_file])

    ncd_list = sorted(ncd_list, key = lambda x: x[0])
    print(str(ncd_list)+"\n")
    return ncd_list[0]

if __name__ == '__main__':
    begin = time.time()
    
    test_path = None #will be passed as arg by terminal

    try:
        test_path = sys.argv[1]

    except Exception as err:
        print("Usage: python3 src/main.py Test/<test file>")
        sys.exit()

    test_file = test_path.split("/")[-1]
    if test_file:
        #execute_getMaxFreqs(test_path)

        list_Samples_Freqs = os.listdir("Sample_freqs")
        concatenate(list_Samples_Freqs)
        compress(list_Samples_Freqs)

        compr_concat_files = os.listdir("Compressed_concat_files")
        if compr_concat_files:
            ncd = NCD(compr_concat_files)

            print(ncd) #i dont understand why the bit size of the files varies

        print("Time: {} sec".format(time.time() - begin))

        # Clean paths
        paths = ["Compressed_concat_files", "Concat_files", "Compressed_files"]
        for p in paths:
            for f in os.listdir(p):
                os.remove(p+"/"+f)