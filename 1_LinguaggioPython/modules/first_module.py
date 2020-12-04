from time import time

def tabulazione(f):
    def stampa(a, b, step = 0.1):
        assert a <= b
        print("x\tf(x)")
        x = a
        while x <= b + step / 2:
            y = f(x)
            print(f"{x:.2f}\t{y:.2f}")
            x += step
    return stampa

def time_it(function):
    def timed(*args, **kwargs):
        start = time() * 1000
        result = function(*args, **kwargs)
        end = time() * 1000
        print(f"Elapsed time: {end - start:.3f} ms")
        return result
    return timed