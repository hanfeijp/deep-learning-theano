#coding: utf-8
import theano
import theano.tensor as T
import numpy as np

x = T.dscalar('x')

# 微分される数式のシンボルを定義
y = (x - 4) * (x ** 2 + 6)

# yをxに関して微分
gy = T.grad(cost=y, wrt=x)

# 微分係数を求める関数を定義
f = theano.function(inputs=[x], outputs=gy)
print theano.pp(f.maker.fgraph.outputs[0])

# 具体的なxを与えて微分係数を求める
print f(0)
print f(1)
print f(2)