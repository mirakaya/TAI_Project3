import argparse
from ast import arg
import os
import sys
import time
from main import Shazam
import matplotlib.pyplot as plt
import numpy as np

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
    return acc

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
    return acc

def bar_plot(results):
    fig = plt.figure()
    x = [com for com,acc in results]
    accs = [acc for com,acc in results]
    plt.bar(x,accs)
    #plt.bar(list_compressors,[38,94,100,98])   #- 3s
    #plt.bar(list_compressors,[100,100,100,100])   #- 6s
    plt.title("Accuracy for diferent compressors - Test length = 1s")
    plt.ylim([0,100])
    plt.legend()
    plt.show()

def bar_plot_2(results):
    # set width of bars
    barWidth = 0.25

    # set heights of bars
    bars1 = [acc[0] for res,acc in results]
    bars2 = [acc[1] for res,acc in results]


    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    # Make the plot
    plt.bar(r1, bars1, color='red', width=barWidth, edgecolor='black', label='Without Noise')
    plt.bar(r2, bars2, color='blue', width=barWidth, edgecolor='black', label='With Noise')

    # Add xticks on the middle of the group bars
    plt.xlabel('group', fontweight='bold')
    x = [res for res,acc in results]
    plt.xticks([r + barWidth for r in range(len(bars1))], x)

    # Create legend & Show graphic
    plt.legend()
    plt.show()


def cleanPaths():
    # Clean paths
    paths = ["Compressed_concat_files", "Concat_files", "Compressed_files"]
    for p in paths:
        for f in os.listdir(p):
            os.remove(p+"/"+f)


if __name__ == '__main__':
    # Command line arguments
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument("-l", "--length", default="10", help="Choose the length(seconds) of test files (1, 3, 6, 10). Default 10.")
    cli_parser.add_argument("-c", "--compressor", default="gzip", help="Choose the compressor method ('gzip' , 'lzma', 'bz2', 'zlib'). Default 'gzip'")
    cli_parser.add_argument("-n", "--noise", default="false", help="Test only files with noise. Default False. Enter True to activate")
    args = cli_parser.parse_args()
    
    test_length = args.length
    test_dir = 'Test_'+test_length+"s"
    compressor = args.compressor
    noise = False
    if args.noise.lower() == "true":
        noise = True
    
    begin = time.time()
    if noise:
        evaluation_with_noise(compressor,test_dir)
    else:
        evaluation_without_noise(compressor,test_dir)
    print("Time: {} sec".format(time.time()-begin))

    begin = time.time()
    # Test compressors accuracy
    """list_compressors = ["lzma","gzip","bz2","zlib"]
    results = []
    for comp in list_compressors:
        acc = evaluation_without_noise(comp,"Test_1s")
        results.append((comp, round(acc,2)))
    
    for comp,acc in results:
        print("Accuracy: {}% | 50 Tests without noise | Type of Compression: {} | Length of the test file 1s".format(acc, comp))
    print("Time: {} min".format((time.time()-begin)/60))
    cleanPaths()
    bar_plot(results)"""

    # Test test length accuracy
    """list_paths = ["Test_1s","Test_3s","Test_6s","Test_10s"]
    results = []
    for path in list_paths:
        acc = evaluation_without_noise("lzma", path)
        acc_noise = evaluation_with_noise("lzma", path)
        results.append((path, [round(acc,2), round(acc_noise,2)]))
    
    for path,acc in results:
        print("Without noise - Accuracy: {}% | 50 Tests | Type of Compression: lzma | Length of the test file {}".format(acc[0], path.split("_")[-1]))
        print("With noise    - Accuracy: {}% | 10 Tests | Type of Compression: lzma | Length of the test file {}".format(acc[1], path.split("_")[-1]))
    print("Time: {} min".format((time.time()-begin)/60))
    cleanPaths()
    bar_plot_2(results)"""    