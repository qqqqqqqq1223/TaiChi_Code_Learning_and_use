## 代码学习
## taichi是一个编程语言，有自己的编译器
## 用户可以将Taichi看作一个Python库
## 大规模矩阵计算，数值模拟
import taichi as ti
import time
ti.init(arch=ti.gpu)

f = ti.field(dtype=ti.f32,shape=())

# Taichi能够编译的 Taichi scope
@ti.kernel
def hello_taichi():
    time_start = time.time()
    f[None] = 0.0
    print('Hello Taichi')
    time_end = time.time()
    print('Running time:{} seconds'.format(time_start - time_end))

# Python编译
def hello_pyrhon():
    time_start = time.time()
    print('Hello Python')
    time_end = time.time()
    print('Running time:{} seconds'.format(time_start - time_end))
hello_taichi()
hello_pyrhon()
