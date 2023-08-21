import csv
import os
import resource
import sys
import subprocess
import time


BASE_RAW_DATA_PATH='raw_data'
BUGGY_MODEL=True  #True: Repaired
MAX_RUN=-1

dataset=input('Enter dataset name: ')
dataset=dataset.upper()

dataset_path=os.path.join(BASE_RAW_DATA_PATH,dataset)

if BUGGY_MODEL:
    dataset_path = os.path.join(dataset_path, 'repaired')
else:
    dataset_path = os.path.join(dataset_path, 'normal')

#print(os.path.basename(os.path.dirname(dataset_path)))
#Directory = os.path.basename

#print(dataset_path)

iteration=0
count =1
for dI in os.listdir(dataset_path):
    config_path=os.path.join(dataset_path, dI)
    if os.path.isdir(config_path):

        if MAX_RUN!=-1 and iteration>=MAX_RUN:
            break
        iteration+=1
        #print(config_path)

        training_config_path=''
        model_path=''

        for fI in os.listdir(config_path):
            file_path=os.path.join(config_path,fI)
            if os.path.isdir(file_path)==False:
                if file_path.endswith('pkl'):
                    training_config_path=file_path
                if file_path.endswith('h5'):
                    model_path=file_path

        print(training_config_path, model_path)

        print(model_path)

        with open('CIFAR10_Count.csv', 'a') as p:
            theWriter = csv.writer(p)
            #theWriter.writerow(['Contract Violation'])
            theWriter.writerow([str(count)]+[model_path])
            #theWriter.writerow("\n")
        start = time.time()
        try:
            p = subprocess.run("python reproduce.py -mp " + model_path + " -cp " + training_config_path, stderr=sys.stderr,
                           stdout=sys.stdout, shell=True)
            count = count +1
        finally:
            end = time.time()
            time_elapsed = end - start
            #print(end - start)
            memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
            with open('CIFAR10_Count.csv', 'a') as p:
                theWriter = csv.writer(p)
                theWriter.writerow([" "]+[" "]+["Time"]+[str(time_elapsed)]+["Memory"]+[str(memMb)])
        #p.wait()
        #start clock
        # for x in range(0, 1):
        #     print(str(x+1) + "th time Running")
        #     p = subprocess.run("python reproduce.py -mp "+model_path+" -cp "+training_config_path, stderr=sys.stderr, stdout=sys.stdout, shell=True)
        #p.wait()
        #end clock
