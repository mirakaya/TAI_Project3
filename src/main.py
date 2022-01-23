import bz2
import gzip
import lzma
import os
import shutil
import subprocess
import time
import sys
import zipfile

class Shazam:
    def __init__(self, test_file, compress_type):
        self.test_file = test_file
        self.compress_type = compress_type

    def run(self):
        self.execute_getMaxFreqs()

        list_Samples_Freqs = os.listdir("Sample_freqs")
        self.concatenate(list_Samples_Freqs)
        self.compress(list_Samples_Freqs, self.compress_type)
        
        ncd = []
        compr_concat_files = os.listdir("Compressed_concat_files")
        if compr_concat_files:
            ncd = self.NCD(compr_concat_files)

        return ncd

    def execute_getMaxFreqs(self):
        '''Usage: GetMaxFreqs[-v(verbose)]
        [-w freqsFile]
        [-ws winSize]
        [-sh shift]
        [-ds downSampling]
        [-nf nFreqs]
        AudioFile'''

        test_path = "Test\\"+self.test_file
        test_name = self.test_file.split(".")[0]
        """subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-w", "Test\\test.freqs",     
                        test_path])  # gets freqs for all the test file"""
        subprocess.Popen([r"getMaxFreqs/bin/GetMaxFreqs.exe", "-w", "Test\\"+test_name+".freqs",
                        test_path], stdout=subprocess.PIPE)  # gets freqs for all the test file

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

            """subprocess.Popen([r"getMaxFreqs\bin\GetMaxFreqs.exe ", "-w", destiny_file,
                            sample_file])  # gets freqs for all the test file"""
            subprocess.Popen([r"getMaxFreqs/bin/GetMaxFreqs.exe", "-w", destiny_file,
                            sample_file], stdout=subprocess.PIPE)  # gets freqs for all the test file

        time.sleep(0.7)

    def concatenate(self, list_Samples_Freqs):#concatenates files

        path_cf = "Concat_files"

        # Check whether the specified path exists or not
        isExist = os.path.exists(path_cf)
        # Create a new directory if it does not exist
        if not isExist:
            os.makedirs(path_cf)

        self.cleanPath("Concat_files")

        test_name = self.test_file.split(".")[0]
        with open("Test/"+test_name+".freqs", "rb") as test_freqs:
            tf = test_freqs.read()

            for i in list_Samples_Freqs:

                with open("Sample_freqs/" + i, "rb") as sample_freqs:
                    sf = sample_freqs.read()

                    with open("Concat_files/" + test_name+".freqs" + "_"+ i, "wb") as end_file:

                        aux = bytes(tf) + bytes(sf)
                        end_file.write(aux)


    def compress(self, list_Samples_Freqs, _type):
        # compress files
        path_cssf = "Compressed_files"

        # Check whether the specified path exists or not
        isExist = os.path.exists(path_cssf)

        # Create a new directory if it does not exist
        if not isExist:
            os.makedirs(path_cssf)

        self.cleanPath("Compressed_concat_files")
        self.cleanPath("Compressed_files")

        list_Concat_Files = os.listdir("Concat_files")

        if not os.path.exists('Compressed_concat_files'):
            os.makedirs('Compressed_concat_files')
        
        if _type == 'gzip':
            self.compress_gzip(list_Samples_Freqs, list_Concat_Files)
        elif _type == 'lzma':
            self.compress_lzma(list_Samples_Freqs, list_Concat_Files)
        elif _type == 'bz2':
            self.compress_bz2(list_Samples_Freqs, list_Concat_Files)
        elif _type == 'zip':
            self.compress_zip(list_Samples_Freqs, list_Concat_Files)


    def compress_gzip(self, list_Samples_Freqs, list_Concat_Files):
        for i in list_Concat_Files:
            with open("Concat_files/" + i, mode="rb") as fin, gzip.open('Compressed_concat_files/' + i, "wb") as fout:
                fout.write(fin.read())

        for i in list_Samples_Freqs:
            with open("Sample_freqs/" + i, mode="rb") as fin, gzip.open('Compressed_files/' + i, "wb") as fout:
                fout.write(fin.read())

        test_name = self.test_file.split(".")[0]
        with open("Test/" + test_name + ".freqs", mode="rb") as fin, gzip.open('Compressed_files/' + test_name + '.freqs',
                                                                            "wb") as fout:
            fout.write(fin.read())


    def compress_bz2(self, list_Samples_Freqs, list_Concat_Files):
        for i in list_Concat_Files:
            with open("Concat_files/" + i, mode="rb") as fin, bz2.open('Compressed_concat_files/' + i, "wb") as fout:
                fout.write(fin.read())

        for i in list_Samples_Freqs:
            with open("Sample_freqs/" + i, mode="rb") as fin, bz2.open('Compressed_files/' + i, "wb") as fout:
                fout.write(fin.read())

        test_name = self.test_file.split(".")[0]
        with open("Test/"+test_name+".freqs", mode="rb") as fin, bz2.open('Compressed_files/'+test_name+'.freqs', "wb") as fout:
            fout.write(fin.read())


    def compress_zip(self, list_Samples_Freqs, list_Concat_Files):
        for i in list_Concat_Files:
            with open("Concat_files/" + i, mode="rb") as fin, zipfile.open('Compressed_concat_files/' + i, "wb") as fout:
                fout.write(fin.read())

        for i in list_Samples_Freqs:
            with open("Sample_freqs/" + i, mode="rb") as fin, zipfile.open('Compressed_files/' + i, "wb") as fout:
                fout.write(fin.read())

        test_name = self.test_file.split(".")[0]
        with open("Test/" + test_name + ".freqs", mode="rb") as fin, zipfile.open('Compressed_files/' + test_name + '.freqs',
                                                                            "wb") as fout:
            fout.write(fin.read())


    def compress_lzma(self, list_Samples_Freqs, list_Concat_Files):
        for i in list_Concat_Files:
            with open("Concat_files/" + i, mode="rb") as fin, lzma.open('Compressed_concat_files/' + i, "wb") as fout:
                fout.write(fin.read())

        for i in list_Samples_Freqs:
            with open("Sample_freqs/" + i, mode="rb") as fin, lzma.open('Compressed_files/' + i, "wb") as fout:
                fout.write(fin.read())

        test_name = self.test_file.split(".")[0]
        with open("Test/" + test_name + ".freqs", mode="rb") as fin, lzma.open('Compressed_files/' + test_name + '.freqs',
                                                                            "wb") as fout:
            fout.write(fin.read())


    def cleanPath(self, path):
        # Clean paths
        for f in os.listdir(path):
            os.remove(path+"/"+f)


    def NCD(self, compr_concat_files):

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
        """for i, el in enumerate(ncd_list[:5]):
            print("\n{} : {} - {}\n".format(i+1, el[2], el[0]))"""
        return ncd_list[0]


if __name__ == '__main__':
    test_path = None #will be passed as arg by terminal

    try:
        test_path = sys.argv[1]

    except Exception as err:
        print("Usage: python3 src/main.py Test/<test file>")
        sys.exit()

    begin = time.time()
    test_file = test_path.split("/")[-1]
    if test_file:
        sha = Shazam(test_file, "lzma")
        res = sha.run()

        print("Result: {}".format(res))
        print("Time: {} sec".format(time.time() - begin))

        # Clean paths
        paths = ["Compressed_concat_files", "Concat_files", "Compressed_files"]
        for p in paths:
            sha.cleanPath(p)