#!/usr/bin/env python
import os
from multiprocessing import Process,JoinableQueue
import ROOT as r
############################################
def opts() :
    from optparse import OptionParser
    parser = OptionParser("usage: %prog [options]")
    parser.add_option("--submit",     dest = "submit",     default = False, action  = "store_true", help = "submit to batch queue")
    parser.add_option("--runlocally", dest = "runlocally", default = None,  metavar = "N",          help = "loop over events using N cores (N>0)")
    parser.add_option("--merge",      dest = "merge",      default = False, action  = "store_true", help = "merge job output")
    options,args = parser.parse_args()
    return options
#####################################
def operateOnListUsingQueue(nCores, workerFunc, inList) :
    q = JoinableQueue()
    listOfProcesses=[]
    for i in range(nCores):
        p = Process(target = workerFunc, args = (q,))
        p.daemon = True
        p.start()
        listOfProcesses.append(p)
    map(q.put,inList)
    q.join()# block until all tasks are done
    #clean up
    for process in listOfProcesses :
        process.terminate()
############################################
def points() :
    return [(100.0, 50.0), (150.0, 50.0), (100.0, 75.0), (150.0, 75.0)]
############################################
def jobCmds() :
    pwd = os.environ["PWD"]
    return ["%s/job.sh %s %g %g"%(pwd, pwd, point[0], point[1]) for point in points()]
############################################    
def submitJobs() :
    for jobCmd in jobCmds() :
        subCmd = "bsub %s"%jobCmd
        print subCmd
        #os.system(subCmd)
############################################    
def runLocally(nWorkers) :
    def worker(q):
        while True:
            item = q.get()
            os.system(item)
            q.task_done()
    operateOnListUsingQueue(nWorkers, worker, jobCmds())
############################################
options = opts()

if options.submit :
    submitJobs()

if options.runlocally :
    runLocally(int(options.runlocally))
    
if options.merge :
    pass
