demonstration the usage of cProfile


import os, cProfile, pstats

def profile(sortby='time', counts=5):
    """Profile sugar"""
    def _profile(function):
        def __profile(*args, **kw):
            profiler = cProfile.Profile()   
            profiler.runcall(function, *args, **kw)
            stats = pstats.Stats(profiler)
            stats.sort_stats(sortby).print_stats(counts)
        return __profile
    return _profile

#test
def test(i, j):
    return i + j

@profile('time', 2)
def test_main(total):
    sum = 0
    for i in range(total):
        for j in range(i):
            sum += test(i, j)
    return sum


if __name__ == '__main__':
    TOTAL = 100
    test_main(TOTAL)
            
##output:        
##         4952 function calls in 0.004 seconds
##
##   Ordered by: internal time
##   List reduced from 3 to 2 due to restriction <2>
##
##   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
##        1    0.003    0.003    0.004    0.004 ~\profile.py:17(test_main)
##     4950    0.001    0.000    0.001    0.000 ~\profile.py:14(test)
