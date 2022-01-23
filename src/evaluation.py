import os
import time
from main import Shazam

def evaluation(comp_type):
    test_files = [f for f in  os.listdir("Test") if ('.freq' not in f and 'unknown' not in f)]
    positive_results_num = 0

    for test in test_files:
        print("Test {} ...".format(test))
        sha = Shazam(test, comp_type)
        res = sha.run()
        res = res[2].split(".")[0]
        print("Result: {}".format(res))
        if res in test:
            positive_results_num+=1            
        
        print()
    
    acc = positive_results_num / len(test_files) * 100
    print("Accuracy: {}% -- {} Tests -- Type of Compression: {}".format(acc, len(test_files), comp_type))

def cleanPaths():
    # Clean paths
    paths = ["Compressed_concat_files", "Concat_files", "Compressed_files"]
    for p in paths:
        for f in os.listdir(p):
            os.remove(p+"/"+f)


if __name__ == '__main__':
    begin = time.time()
    comp_type = "bz2"
    evaluation(comp_type)
    print("Time: {} sec".format(time.time()-begin))
    cleanPaths()