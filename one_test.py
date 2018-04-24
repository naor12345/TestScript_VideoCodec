#linux, python3
#one executable codec, for multi-sequence and multi-QP
import os
import sys
import threading
import time
import xlwt
import xlrd
import time
from xlutils.copy import copy
import subprocess
import queue

def get_process_count(imagename):
    p = os.popen('ps -A | grep TAppEncoder') #runable file must be "TAppEncoder*"
    num = p.read().count('TAppEncoder')      #runable file must be "TAppEncoder*"
    return num

def check_exsit(process_name, queue):
    if get_process_count(process_name) == 0:
        queue.put(0)
    else:
        queue.put(1) 

def run(QP, gc, cmd, exename):
    print (subprocess.Popen(cmd, shell=True))
    q = queue.Queue()
    # wait for process done
    while True:
        t = threading.Timer(300, check_exsit, [exename, q])
        #              each 300 seconds, check if is done
        t.start()
        t.join() 
        t.cancel()
        time.sleep(1)
        aa = q.get()
        if aa == 0:
            break

if __name__ == "__main__":
    path_base = os.getcwd()             #get current path
    runn_path = path_base + "/runable/" #executable file path
    apli_name = "TAppEncoderStatic"     #change exe name
    os.system("killall "+ apli_name)    #kill process if exist
    apli = runn_path + apli_name 
    targetFolder = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time())) + "_" + apli_name
    test_path = path_base + "/Result/" + targetFolder
    os.makedirs(test_path, 0o777, True)
    enc_file = path_base + "/cfg/encoder_randomaccess_main.cfg"
    cfg_path = path_base + "/per-sequence/"
    seq_path = "/media/naor12345/0C5812595812423E/Seq_class/"    
    rec_path = path_base + "/Result/" + targetFolder + "/rec/" 
    log_path = path_base + "/Result/" + targetFolder + "/log/" 
    os.makedirs(rec_path, 0o777, True)  #path to rec yuv(no use)
    os.makedirs(log_path, 0o777, True)  #path to log file(result)
    cmd_path = path_base + "/cmdtxt/atxt.txt" #change command txt
    QP_point = [22,27,32,37]            #change qp here
    cmdtxt = open(cmd_path, 'r')    
    seq = cmdtxt.readlines()
    
    #main loop: for each sequence, for each QP
    for line in seq:
        yclass = line.split()[0]
        yuv_name = line.split()[1].split('.')[0]
        cfg_base = line.split()[1].split('_')[0]
        yuv_file = seq_path + yclass + '/' + line.split()[1]
        rec_file = rec_path + yuv_name       
        bin_file = rec_path + yuv_name
        cfg_file = cfg_path + cfg_base + '.cfg'
        log_file = log_path + yclass + "_" + yuv_name
        #init(yuv_name, QP_point, exl_file)

        for i in range(len(QP_point)):
            cmd = apli + ' -c ' + enc_file + ' -c ' + cfg_file + ' ' \
                + '--InputFile=' + yuv_file + ' ' \
                + '--BitstreamFile=' + bin_file + '.bin ' \
                + '--ReconFile=' + rec_file + '.yuv ' \
                + '--QP='+str(QP_point[i]) + ' ' \
                + '> ' + log_file + '_' + str(QP_point[i]) + '.log' 
            print (yuv_name)            
            run(QP_point[i], 'c', cmd, apli_name)
