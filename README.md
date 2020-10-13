# K-Means算法的Python实现

如果觉得对您有帮助的话，劳烦给个Star

在K-Means.py中定义了一个KMeans类，只需要两行代码即可实现K-Means中心聚类算法

```python
km = KMeans(dataset_tmp, 3)  # 聚成三个簇
km.fit()
```

该类具体方法如下：

## \_\_init\_\_(self, dataset, cluster_num=2)

该类的初始化方法，参数如下：

dataset: list  数据集，列表嵌套列表的形式。例如[[1,2,3,...], [4,5,6,...],...]

cluster_num: int  要划分的簇的个数。Default: 2

return: None

Demo: 若要对dataset_tmp进行聚类，首先实例化KMeans类

附部分dataset_tmp截图



{% qnimg K-Means算法及Python实现_dataset_demo.png alt:dataset_demo %}

```python
km = KMeans(dataset_tmp, 3)
```

## fit(self)

进行聚类

return: None

``` python
km.fit()
```

## _distance(p1, p2)

p1点和p2点的欧氏距离

@staticmethod

p1: list  形如[x,y]

return: None

## \_center(_list):

计算坐标组中的中心点

@staticmethod

_list: list 形如dataset，列表嵌套列表的形式。例如[[1,2,3,...], [4,5,6,...],...]

return: list 中心点坐标[x,y,z,...]