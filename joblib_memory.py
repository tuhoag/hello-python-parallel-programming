from joblib import Memory

cache_dir = 'cache'
memory = Memory(cache_dir, verbose=0)

@memory.cache
def f(x):
    print('Running f({})'.format(x))
    return x

def main():
    f(1)
    f(1)
    f(2)
    


if __name__ == "__main__":
    main()