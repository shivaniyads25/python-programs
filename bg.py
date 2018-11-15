import matplotlib.pyplot as b
a=[1,2,3,4,5]
c=[150,123,143,128,136]
tick_label=['a','b','c','d','e']
b.bar(a,c,tick_label=tick_label,width=0.5,color=['pink','black'])
b.xlabel('names')
b.ylabel('height in cms')
b.title('bar graph showing height')
b.show()
