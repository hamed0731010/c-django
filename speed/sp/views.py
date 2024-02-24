from django.shortcuts import render
import  time
import ctypes
import os
# Create your views here.
current_dir= os.path.dirname(os.path.abspath(__file__))
lib_path = os.path.join(current_dir,'hello.so')
sum_calc= ctypes.CDLL(lib_path)
sum_calc.claculate.argtypes=[ctypes.c_int]
sum_calc.claculate.argtypes= [ctypes.c_longlong]

def calc(limit):
    return sum_calc.claculate(limit)
def speed(request):
    total=0
    limit= 100000000
    start= time.time()
    # for i in range(limit):
    #     total += i
    total=calc(limit)
    end =time.time()    
    return render(request,'sp/test.html',context={'total':total,'diff':end-start})        