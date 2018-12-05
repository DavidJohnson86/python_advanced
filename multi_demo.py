from multiprocessing import Process, set_start_method, Queue, Lock
from time import sleep

def slow_function(i, l, q):
    print("Started "+str(i))
    with l:
        sleep(1)
    q.put((i, 41))
    print("Finished")

if __name__ == "__main__":
    #set_start_method("spawn")
    proc_list=[]
    lock=Lock()
    q=Queue()
    for i in range(5):
        p=Process(target=slow_function, args=(i, lock, q))
        p.start()
        proc_list.append(p)
    sleep(0.5)
    print("Main is live")
    system_alive=True
    while system_alive:
        if not any(p.is_alive() for p in proc_list):
            system_alive=False
        while not q.empty():
            print(q.get(False))

    for p in proc_list:
        p.join()
    print("All process finished")