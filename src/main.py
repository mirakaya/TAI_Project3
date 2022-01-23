import bz2
import gzip
import lzma
import os
import shutil
import subprocess
import time
import sys
import zipfile


def execute_getMaxFreqs(pathSoundFile):
    '''Usage: GetMaxFreqs[-v(verbose)]
    [-w freqsFile]
    [-ws winSize]
    [-sh shift]
    [-ds downSampling]
    [-nf nFreqs]
    AudioFile'''

    test_name = pathSoundFile.split("/")[-1].split(".")[0]
    subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-w", "Test\\test.freqs",
                      pathSoundFile])  # gets freqs for all the test file

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

        subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-w", destiny_file,
                          sample_file])  # gets freqs for all the test file
        #subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-w", destiny_file , sample_file], shell=True, stdout=subprocess.PIPE) #erro

def concatenate(list_Samples_Freqs):#concatenates files

    path_cf = "Concat_files"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path_cf)
    # Create a new directory if it does not exist
    if not isExist:
        os.makedirs(path_cf)

    '''paths = ["Concat_files"]
    for p in paths:
        for f in os.listdir(p):
            os.remove(p+"/"+f)'''

    test_name = test_file.split(".")[0]
    with open("Test/"+test_name+".freqs", "rb") as test_freqs:
        tf = test_freqs.read()

        for i in list_Samples_Freqs:

            with open("Sample_freqs/" + i, "rb") as sample_freqs:
                sf = sample_freqs.read()

                with open("Concat_files/" + test_name+".freqs" + "_"+ i, "wb") as end_file:

                    aux = bytes(tf) + bytes(sf)
                    end_file.write(aux)

def compress_gzip():
    # compress files
    path_cssf = "Compressed_files"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path_cssf)

    # Create a new directory if it does not exist
    if not isExist:
        os.makedirs(path_cssf)

    for i in os.listdir("Compressed_concat_files"):
        os.remove("Compressed_concat_files/" + i)

    for i in os.listdir("Compressed_files"):
        os.remove("Compressed_files/" + i)

    list_Concat_Files = os.listdir("Concat_files")

    if not os.path.exists('Compressed_concat_files'):
        os.makedirs('Compressed_concat_files')

    for i in list_Concat_Files:
        with open("Concat_files/" + i, mode="rb") as fin, gzip.open('Compressed_concat_files/' + i, "wb") as fout:
            fout.write(fin.read())

    for i in list_Samples_Freqs:
        with open("Sample_freqs/" + i, mode="rb") as fin, gzip.open('Compressed_files/' + i, "wb") as fout:
            fout.write(fin.read())

    test_name = test_file.split(".")[0]
    with open("Test/" + test_name + ".freqs", mode="rb") as fin, gzip.open('Compressed_files/' + test_name + '.freqs',
                                                                          "wb") as fout:
        fout.write(fin.read())




def compress_bz2():

    # compress files
    path_cssf = "Compressed_files"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path_cssf)

    # Create a new directory if it does not exist
    if not isExist:
        os.makedirs(path_cssf)

    for i in os.listdir("Compressed_concat_files"):
        os.remove("Compressed_concat_files/" + i)

    for i in os.listdir("Compressed_files"):
        os.remove("Compressed_files/" + i)


    list_Concat_Files = os.listdir("Concat_files")

    if not os.path.exists('Compressed_concat_files'):
        os.makedirs('Compressed_concat_files')

    for i in list_Concat_Files:

        with open("Concat_files/" + i, mode="rb") as fin, bz2.open('Compressed_concat_files/' + i, "wb") as fout:
            fout.write(fin.read())



    for i in list_Samples_Freqs:

        with open("Sample_freqs/" + i, mode="rb") as fin, bz2.open('Compressed_files/' + i, "wb") as fout:
            fout.write(fin.read())


    test_name = test_file.split(".")[0]
    with open("Test/"+test_name+".freqs", mode="rb") as fin, bz2.open('Compressed_files/'+test_name+'.freqs', "wb") as fout:
        fout.write(fin.read())


def compress_zip():
    # compress files
    path_cssf = "Compressed_files"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path_cssf)

    # Create a new directory if it does not exist
    if not isExist:
        os.makedirs(path_cssf)

    for i in os.listdir("Compressed_concat_files"):
        os.remove("Compressed_concat_files/" + i)

    for i in os.listdir("Compressed_files"):
        os.remove("Compressed_files/" + i)

    list_Concat_Files = os.listdir("Concat_files")

    if not os.path.exists('Compressed_concat_files'):
        os.makedirs('Compressed_concat_files')

    for i in list_Concat_Files:
        with open("Concat_files/" + i, mode="rb") as fin, zipfile.open('Compressed_concat_files/' + i, "wb") as fout:
            fout.write(fin.read())

    for i in list_Samples_Freqs:
        with open("Sample_freqs/" + i, mode="rb") as fin, zipfile.open('Compressed_files/' + i, "wb") as fout:
            fout.write(fin.read())

    test_name = test_file.split(".")[0]
    with open("Test/" + test_name + ".freqs", mode="rb") as fin, zipfile.open('Compressed_files/' + test_name + '.freqs',
                                                                           "wb") as fout:
        fout.write(fin.read())

def compress_LZMA():
    # compress files
    path_cssf = "Compressed_files"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path_cssf)

    # Create a new directory if it does not exist
    if not isExist:
        os.makedirs(path_cssf)

    for i in os.listdir("Compressed_concat_files"):
        os.remove("Compressed_concat_files/" + i)

    for i in os.listdir("Compressed_files"):
        os.remove("Compressed_files/" + i)

    list_Concat_Files = os.listdir("Concat_files")

    if not os.path.exists('Compressed_concat_files'):
        os.makedirs('Compressed_concat_files')

    for i in list_Concat_Files:
        with open("Concat_files/" + i, mode="rb") as fin, lzma.open('Compressed_concat_files/' + i, "wb") as fout:
            fout.write(fin.read())

    for i in list_Samples_Freqs:
        with open("Sample_freqs/" + i, mode="rb") as fin, lzma.open('Compressed_files/' + i, "wb") as fout:
            fout.write(fin.read())

    test_name = test_file.split(".")[0]
    with open("Test/" + test_name + ".freqs", mode="rb") as fin, lzma.open('Compressed_files/' + test_name + '.freqs',
                                                                          "wb") as fout:
        fout.write(fin.read())








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

        shutil.rmtree("Sample_freqs")

        execute_getMaxFreqs(test_path)

        time.sleep(0.5)

        list_Samples = os.listdir("Samples")
        list_Samples_Freqs = os.listdir("Sample_freqs")

        concatenate(list_Samples_Freqs)

        #working
        compress_gzip()
        #compress_bz2()
        #compress_LZMA()


        #not working
        #compress_zip()



        compr_concat_files = os.listdir("Compressed_concat_files")
        if compr_concat_files:
            ncd = NCD(compr_concat_files)
            print(ncd)

        print("Time: {} sec".format(time.time() - begin))

        # Clean paths
        paths = ["Compressed_concat_files", "Concat_files", "Compressed_files"]
        '''for p in paths:
            for f in os.listdir(p):
                os.remove(p+"/"+f)'''