import argparse
import os
import sys
import time
from xmlrpc.client import SYSTEM_ERROR, boolean
from main import Shazam

def evaluation_with_noise(comp_type,test_dir):
    test_files = [f for f in  os.listdir(test_dir) if ('.freq' not in f and 'unknown' not in f and 'noise' in f)]
    positive_results_num = 0

    for test in test_files:
        print("Test {} ...".format(test))
        sha = Shazam(test, comp_type, test_dir)
        res = sha.run()
        res = res[0][2].split(".")[0]
        print("Result: {}".format(res))
        if res in test:
            positive_results_num+=1            
        
        print()
    
    acc = positive_results_num / len(test_files) * 100
    print("Accuracy: {}% | {} Tests with noise | Type of Compression: {} | Length of the test file {}".format(acc, len(test_files), comp_type, test_dir.split("_")[-1]))

def evaluation_without_noise(comp_type,test_dir):
    test_files = [f for f in  os.listdir(test_dir) if ('.freq' not in f and 'unknown' not in f and 'noise' not in f)]
    positive_results_num = 0

    for test in test_files:
        print("Test {} ...".format(test))
        sha = Shazam(test, comp_type, test_dir)
        res = sha.run()
        res = res[0][2].split(".")[0]
        print("Result: {}".format(res))
        if res in test:
            positive_results_num+=1            
        
        print()
    
    acc = positive_results_num / len(test_files) * 100
    print("Accuracy: {}% | {} Tests without noise | Type of Compression: {} | Length of the test file {}".format(acc, len(test_files), comp_type, test_dir.split("_")[-1]))



def cleanPaths():
    # Clean paths
    paths = ["Compressed_concat_files", "Concat_files", "Compressed_files"]
    for p in paths:
        for f in os.listdir(p):
            os.remove(p+"/"+f)


if __name__ == '__main__':
    # Command line arguments
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument("-l", "--length", default="10", help="Choose the length(seconds) of test files (3, 6, 10). Default 10.")
    cli_parser.add_argument("-c", "--compressor", default="gzip", help="Choose the compressor method ('gzip' , 'lzma', 'bz2', 'zlib'). Default 'gzip'")
    cli_parser.add_argument("-n", "--noise", type=boolean, default=False, help="Test only files with noise. Default False. Enter True to activate")
    args = cli_parser.parse_args()
    
    test_length = args.length
    test_dir = 'Test_'+test_length+"s"
    compressor = args.compressor
    noise = args.noise
    
    begin = time.time()
    if noise:
        evaluation_with_noise(compressor,test_dir)
    else:
        evaluation_without_noise(compressor,test_dir)
    print("Time: {} sec".format(time.time()-begin))
    cleanPaths()