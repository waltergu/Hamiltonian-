'''
QuantumNumber test.
'''

__all__=['test_quantum_number']

from HamiltonianPy.Basics.QuantumNumber import *
from collections import OrderedDict
import time

def test_quantum_number():
    test_quantum_number_element()
    test_quantum_number_collection()

def test_quantum_number_element():
    print 'test_quantum_number_element'
    a=QuantumNumber([('NE',2,'U1'),('Sz',-2,'U1')])
    b=QuantumNumber([('NE',1,'U1'),('Sz',-1,'U1')])
    print 'a: %s'%(a,)
    print 'b: %s'%(b,)
    print 'a+b: %s'%(a+b,)
    c=QuantumNumber([('SP',1,'Z2')])
    print 'c: %s'%(c,)
    d=a.direct_sum(c)
    print 'd(a.direct_sum(c)): %s'%(d,)
    e=d.replace(NE=11)
    print 'e(d.replace(NE=11)): %s'%(e,)
    print 'd+e: %s'%(d+e,)
    print

def test_quantum_number_collection():
    print 'test_quantum_number_collection'
    a=QuantumNumberCollection([(QuantumNumber([('Sz',1,'U1')]),slice(0,1)),(QuantumNumber([('Sz',0,'U1')]),slice(1,3)),(QuantumNumber([('Sz',-1,'U1')]),slice(3,4))])
    print 'a: %s'%a
    b=QuantumNumberCollection()
    t1=time.time()
    for i in xrange(10):
        b+=a
    print 'b: ',b
    QuantumNumber.set_repr_form(QuantumNumber.repr_forms[2])
    print 'b.map:'
    for key,value in b.map.items():
        print '%s: %s'%(key,value)
    print