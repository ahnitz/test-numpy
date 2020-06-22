import numpy
import sys

val = [(0, 0., 0, -31.666483, 200, 0., 0.,  1.      ,  -2.8499086-4.852268j  ,  613090),
 (1, 0., 0, 260.91525 ,  42, 0., 0.,  1.      ,  11.672331 -0.39883116j,  787315),
 (1, 0., 0,  52.15155 ,  42, 0., 0.,  1.      ,  -3.9071944-3.9876528j ,  806641),
 (1, 0., 0,  52.430195,  42, 0., 0.,  1.      ,   3.5721765-4.4356694j , 1363540),
 (2, 0., 0, 304.43646 ,  58, 0., 0.,  1.      ,  -0.9019805+6.379318j  ,  787323),
 (3, 0., 0, 299.42108 ,  52, 0., 0.,  1.      ,   6.365695 +3.1266918j ,  787332),
 (4, 0., 0,  39.4836  ,  28, 0., 0.,  9.182192, -16.804018 +9.028097j  ,  787304),
 (4, 0., 0,  76.83787 ,  28, 0., 0.,  1.      ,   3.2854116-5.3171387j , 1321869),
 (5, 0., 0, 143.26366 ,  24, 0., 0., 10.996129,  14.33073  +1.0027167j ,  787299)]
 
 
dtype = [('template_id', '<i8'), ('bank_chisq', '<f4'), ('bank_chisq_dof', '<i8'), ('chisq', '<f4'), ('chisq_dof', '<i8'), ('cont_chisq', '<f4'), ('psd_var_val', '<f4'), ('sg_chisq', '<f4'), ('snr', '<c8'), ('time_index', '<i8')]

vec = numpy.array(val, dtype=dtype)


a = vec['snr']
g = abs(a)

b = vec['snr'].copy()
h = abs(b)

print ((h-g).sum(), a, b, g, h)

if (h-g).sum() != 0:
    sys.exit(1)
