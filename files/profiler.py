import cProfile

def profileit(func):
    """
    Decorator (function wrapper) that profiles a single function

    @profileit()
    def func1(...)
            # do something
        pass
    """
    def wrapper(*args, **kwargs):
        func_name = func.__name__ + ".pfl"
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        prof.dump_stats(func_name)
        return retval

    return wrapper

# Example
@profileit
def foo():
    a = 0
    for b in range(1, 100000):
        a += b

foo()

# Analysis
#python -m pstats foo.pfl
#Welcome to the profile statistics browser.
#foo.pfl% help
#foo.pfl% sort time
#foo.pfl% stats 10
#Fri Mar 14 10:26:03 2014    foo.pfl
#
#         7 function calls in 0.008 seconds
#
#   Ordered by: internal time
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.007    0.007    0.007    0.007 {method 'enable' of '_lsprof.Profiler' objects}
#        1    0.002    0.002    0.008    0.008 profile.py:1(<module>)
#        1    0.000    0.000    0.000    0.000 C:\Python27\lib\cProfile.py:5(<module>)
#        1    0.000    0.000    0.007    0.007 profile.py:12(wrapper)
#        1    0.000    0.000    0.007    0.007 C:\Python27\lib\cProfile.py:146(runcall)
#        1    0.000    0.000    0.000    0.000 C:\Python27\lib\cProfile.py:66(Profile)
#        1    0.000    0.000    0.000    0.000 profile.py:3(profileit)



