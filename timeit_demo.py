import timeit

if __name__ == "__main__":
    m=timeit.repeat("r = sum_mul(a, b)",
                    "import random;"+
                    "from perf_demo import generate_data, sum_mul;"
                    +"a = generate_data();b = generate_data()",
                    number=10, repeat=1)
    print(m)

