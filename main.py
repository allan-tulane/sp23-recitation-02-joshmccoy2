"""
CMPS 2200  Recitation 2
"""

import tabulate
import time

def simple_work_calc(n, a, b):
  if n == 1:
    return 1
  elif n ==0:
    return 0
  else:
    return a*simple_work_calc(n/b, a, b)+ n
pass

def test_simple_work():
	assert work_calc(10, 2, 2) == 36
	assert work_calc(20, 3, 2) == 230
	assert work_calc(30, 4, 2) == 650
  #assert work_calc(30, 4, 2) == 
  #assert work_calc(30, 4, 2) == 
  #assert work_calc(30, 4, 2) == 
# Dealing with indentation error
def work_calc(n, a, b, f):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  else: return a*work_calc(n//b, a, b, f)+ f(n)
pass

def span_calc(n, a, b, f):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  else: return work_calc(n//b, a, b, f) + f(n)
pass

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
 # assert work_calc(40, 2, 3, lambda 
 # assert work_calc(50, 3, 4, lambda 
 # assert work_calc(40, 2, 3, lambda 
  # still having indentation error like last lab


def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	result = []
	for n in sizes:
		result.append((n, work_fn1(n), work_fn2(n)))
	return result
	
def print_results(results):
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work(sizes =[10,20,50,100,1000,5000, 10000]):
  result = []
  work_fn1 = lambda n: work_calc(n, 4, 2, lambda n: n)
  work_fn2 = lambda n: work_calc(n, 4, 2, lambda n:n*n)
  res = compare_work(work_fn1, work_fn2)
  print_results(res)

def compare_span(span_fn1, span_fn2, sizes=[10,20,50,100,1000,5000,10000]):
  result = []
  for n in sizes:
    result.append((n, work_fn1(n), work_fn2(n)))
  return result
  

def test_compare_span():
  result = []
  span_fn1 = lambda n: span_calc(n, 4, 2, lambda n: n)
  span_fn2 = lambda n: span_calc(n, 4, 2, lambda n: n*n)
  res = compare_work(span_fn1, span_fn2)
  print_results(res)