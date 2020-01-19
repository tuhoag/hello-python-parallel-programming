import time
from joblib import Parallel, delayed
from tqdm import tqdm

def f1(x, y):
    # print('Running f(x={}, y={})'.format(x, y))
    time.sleep(1)
    return x + y

def main():
    x_list = list(range(10))
    y_list = list(range(10,20))

    print('start parallel')
    parallel_results = Parallel(n_jobs=2)(delayed(f1)(x=x, y=y) for x, y in tqdm(iterable=zip(x_list, y_list), total=len(x_list)))
    print('parallel results: {}'.format(parallel_results))

if __name__ == "__main__":
    main()