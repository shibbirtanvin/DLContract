import csv
import os
import resource
import sys
import subprocess
import time


BASE_RAW_DATA_PATH='Benchmark'
BUGGY_MODEL=True    #True: cifar10
MAX_RUN=-1

dataset=input('Enter dataset name: ')
dataset=dataset.upper()

dataset_path=os.path.join(BASE_RAW_DATA_PATH,dataset)

if BUGGY_MODEL:
    file_path = os.path.join(dataset_path, "cifar10")
else:
    file_path = os.path.join(dataset_path, "fashion_mnist")


iteration=0
count =1
for dI in os.listdir(file_path):
    config_path=os.path.join(file_path, dI)
    if os.path.isdir(config_path):

        if MAX_RUN!=-1 and iteration>=MAX_RUN:
            break
        iteration+=1
        #print(config_path)

        training_config_path=''
        model_path=''

        count = 0
        #model_path_list = []
        for fI in os.listdir(file_path):
            #file_path_model = os.path.join(file_path, fI)
            # file_path=os.path.join(post_path)
            print(file_path)

            if os.path.isdir(file_path) == True:
                if 'correct.py' in fI:
                    #model_path_list.append(file_path_model)
                    model_path = os.path.join(file_path, fI)
                # if file_path.endswith('h5'):
                #     model_path=file_path
            #count = count + 1
        # for i in model_path_list:
        #     if (model_path_list.__len__() > 1):
        #         model_path_extract = [x for x in model_path_list if x.endswith('main.py')]
        #         try:
        #             model_path = model_path_extract[-1]
        #         except IndexError:
        #             pass
        #     # print(training_config_path, model_path)
        #     else:
        #         model_path = model_path_list[-1]
            print(model_path)

            #print(model_path)
            if model_path and count<5:
                with open('CorrectCifar10UMLAUT.csv', 'a') as p:
                    theWriter = csv.writer(p)
                    #theWriter.writerow(['Contract Violation'])
                    theWriter.writerow([str(count)]+[model_path])
                    #theWriter.writerow("\n")
                start = time.time()
                try:
                    p = subprocess.run("python " + model_path, stderr=sys.stderr,
                                       stdout=sys.stdout, shell=True)
                    count = count +1
                finally:
                    end = time.time()
                    time_elapsed = end - start
                    #print(end - start)
                    memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
                    with open('CorrectCifar10UMLAUT.csv', 'a') as p:
                        theWriter = csv.writer(p)
                        theWriter.writerow([" "]+[" "]+["Time"]+[str(time_elapsed)]+["Memory"]+[str(memMb)])
            #p.wait()
        #start clock
        # for x in range(0, 1):
        #     print(str(x+1) + "th time Running")
        #     p = subprocess.run("python reproduce.py -mp "+model_path+" -cp "+training_config_path, stderr=sys.stderr, stdout=sys.stdout, shell=True)
        #p.wait()
        #end clock
