import csv
import logging
import os
import resource
import sys
import subprocess
import time
import traceback

BASE_RAW_DATA_PATH='Benchmark'
BUGGY_MODEL=True    #To run correct models BUGGY_MODEL=False
MAX_RUN=-1

dataset=input('Enter dataset name: ')
dataset=dataset.upper()

dataset_path=os.path.join(BASE_RAW_DATA_PATH,dataset)
#dataset_path = os.path.join(BASE_RAW_DATA_PATH)

# if BUGGY_MODEL:
#     model_path=os.path.join(dataset_path, 'Buggy')
# else:
#     model_path=os.path.join(dataset_path, 'Correct Code')

print(os.path.basename(os.path.dirname(dataset_path)))
Directory = os.path.dirname(dataset_path)
#print(Directory)
#print(dataset_path)

iteration=0
serial =1
for dI in os.listdir(dataset_path):
    config_path=os.path.join(dataset_path, dI)
    if os.path.isdir(config_path):
        if MAX_RUN!=-1 and iteration>=MAX_RUN:
            break
        iteration+=1
        #print(config_path)
        SOpost = dI
        print(SOpost)
        training_config_path=''
        #post_path= os.path.join(config_path, model_path)
        for dI in os.listdir(config_path):
            print("The dir is: %s" % os.listdir(config_path))
            print(config_path)
            #for f in os.listdir("."):
            # r = dI.replace(" ", "_")
            # if (r != dI):
            #     os.rename(dI, r)
            #os.rename('Buggy', "Buggy")
            #os.rename('Correct Code', "Correct")
        if BUGGY_MODEL:
            file_path = os.path.join(config_path, "Buggy")
        else:
            file_path = os.path.join(config_path, "Correct")

        count = 0
        model_path_list = []
        for fI in os.listdir(file_path):
            file_path_model = os.path.join(file_path, fI)
            #file_path=os.path.join(post_path)
            print(file_path_model)
            if os.path.isdir(file_path_model)==False:
                if file_path_model.endswith('.py'):
                    model_path_list.append(file_path_model)
                # if file_path.endswith('h5'):
                #     model_path=file_path
            count = count+1
        for i in model_path_list:
            if(model_path_list.__len__() >1):
                model_path_extract = [x for x in model_path_list if x.endswith('main.py')]
                model_path = model_path_extract[-1]
        #print(training_config_path, model_path)
            else:
                model_path = model_path_list[-1]
        print(model_path)

        with open('COUNT_SO.csv', 'a') as p:
            theWriter = csv.writer(p)
            #theWriter.writerow(['Contract Violation'])
            theWriter.writerow([str(serial)]+[SOpost]+[model_path])
            #theWriter.writerow("\n")
        #start = time.time()
        e = ''
        try:
            start = time.time()
            p = subprocess.run("python "+ model_path, stderr=sys.stderr,
                           stdout=sys.stdout, shell=True)
            serial = serial +1
        except Exception as error:
            #e = e + error
            #print('An exception occurred: {}'.format(error))
            logging.error(traceback.format_exc())
            e = e + str(logging.error(traceback.format_exc()))
            print(e)
            # Logs the error appropriately.
        finally:
            end = time.time()
            time_elapsed = end - start
            #print(end - start)
            memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
            with open('COUNT_SO.csv', 'a') as p:
                theWriter = csv.writer(p)
                theWriter.writerow([" "]+[e]+["Time"]+[str(time_elapsed)]+["Memory"]+[str(memMb)])
        #p.wait()
        #start clock
        # for x in range(0, 1):
        #     print(str(x+1) + "th time Running")
        #     p = subprocess.run("python reproduce.py -mp "+model_path+" -cp "+training_config_path, stderr=sys.stderr, stdout=sys.stdout, shell=True)
        #p.wait()
        #end clock
