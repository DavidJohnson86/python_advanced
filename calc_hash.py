from os import walk, access, R_OK
from os.path import join, getsize
from hashlib import sha1
from perf_demo import measure

BUFF_SIZE=65536
def create_filelist(src_dir):
    retval=[]
    for dir_name, dirs, files in walk(src_dir):
        for file_name in (join(dir_name, fn) for fn in files):
            if 10_000_000<getsize(file_name) and access(file_name, R_OK):
                retval.append(file_name)
    return retval

def calc_hash(filename):
    hashfunc=sha1()
    try:
        with open(filename, 'rb') as f:
            while True:
                data=f.read(BUFF_SIZE)
                if len(data) == 0:
                    break
                hashfunc.update(data)
    except PermissionError as e:
        print(e)
        return filename, "ACCESSDENIED"
    return filename, hashfunc.hexdigest()

@measure
def seq_calc_hash(file_list):
    for file_name in file_list:
        res=calc_hash(file_name)

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
@measure
def thread_calc_hash(file_list):
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_list=[]
        for file_name in file_list:
            future_list.append(executor.submit(calc_hash, file_name))
        results = []
        for future in as_completed(future_list):
            results.append(future.result())
    return results

@measure
def process_calc_hash(file_list):
    with ProcessPoolExecutor(max_workers=2) as executor:
        future_list=[]
        for file_name in file_list:
            future_list.append(executor.submit(calc_hash, file_name))
        results = []
        for future in as_completed(future_list):
            results.append(future.result())
    return results
if __name__ == "__main__":
    filenames=create_filelist(r"C:\windows\System32")
    seq_calc_hash(filenames)
    thread_calc_hash(filenames)

