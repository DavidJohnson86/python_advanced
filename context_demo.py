import sys

class IOCounter:
    def write_and_count(self, data):
        self.counter += len(data)
        self.real_write(data)

    def __enter__(self):
        self.real_write=sys.stdout.write
        sys.stdout.write=self.write_and_count
        self.counter=0
        return self

    def __exit__(self, exec_type, exec_val, exec_tb):
        sys.stdout.write=self.real_write
        print("{} written".format(self.counter))

with IOCounter() as out:
    print("Hello World!")
    print(out.counter)
