import csv
import os
import resource
import sys
import subprocess
import time
import os, psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss)

BASE_RAW_DATA_PATH='sample_buggy_scripts'
BUGGY_MODEL=True
MAX_RUN=-1

dataset=input('Enter dataset name: ')
dataset=dataset.upper()

dataset_path=os.path.join(BASE_RAW_DATA_PATH,dataset)

if BUGGY_MODEL:
    file_path = os.path.join(dataset_path, "Buggy")
else:
    file_path = os.path.join(dataset_path, "Correct")

#print(os.path.basename(os.path.dirname(dataset_path)))
#Directory = os.path.basename

#print(dataset_path)

iteration=0
# count =1
#for dI in os.listdir(file_path):
 #   config_path=os.path.join(file_path, dI)
#    if os.path.isdir(config_path):

# if MAX_RUN!=-1 and iteration>=MAX_RUN:
#     break
# iteration+=1
#print(config_path)

training_config_path=''
model_path=''

count = 0
#model_path_list = []
for fI in os.listdir(file_path):
    if MAX_RUN!=-1 and iteration>=MAX_RUN:
        break
    iteration+=1
    file_path_model = os.path.join(file_path, fI)
    # file_path=os.path.join(post_path)
    print(file_path_model)
    if os.path.isdir(file_path_model) == False:
        if file_path_model.endswith('main.py'):
            model_path = file_path_model

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

            with open('newMmemoryNeuraLint.csv', 'a') as p:
                theWriter = csv.writer(p)
                #theWriter.writerow(['Contract Violation'])
                theWriter.writerow([str(count)]+[str(fI)])
                #theWriter.writerow("\n")
            start = time.time()
            start_rusage = resource.getrusage(resource.RUSAGE_SELF)
            try:
                p = subprocess.run("python " + model_path, stderr=sys.stderr,
                                   stdout=sys.stdout, shell=True)
                count = count +1
            finally:
                end = time.time()
                end_rusage = resource.getrusage(resource.RUSAGE_SELF)
                time_elapsed = end - start
                #print(end - start)
                memMbR = (end_rusage - start_rusage)
                print(memMbR)
                memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
                with open('newMmemoryNeuraLint.csv', 'a') as p:
                    theWriter = csv.writer(p)
                    theWriter.writerow([" "]+[" "]+["Time"]+[str(time_elapsed)]+["Memory"]+[str(memMb)]+ ["New Memory"] + memMbR)
        #p.wait()
        #start clock
        # for x in range(0, 1):
        #     print(str(x+1) + "th time Running")
        #     p = subprocess.run("python reproduce.py -mp "+model_path+" -cp "+training_config_path, stderr=sys.stderr, stdout=sys.stdout, shell=True)
        #p.wait()
        #end clock
