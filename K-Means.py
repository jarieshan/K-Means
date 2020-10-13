import numpy as np
import sys
import matplotlib.pyplot as plt


class KMeans(object):
    """向量化计算"""

    def __init__(self, dataset, cluster_num=2):
        """
        :param dataset: is list likes [[],[]]
        """
        self.dataset = dataset
        # 簇中心数量
        self.cluster_num = cluster_num
        # 选取数据集前N个点为簇中心
        self.center_points = dataset[0:cluster_num]
        self.result = {}

    def fit(self):
        """:return {簇序号:[[点1],[点2]]...}"""
        while True:
            # 空字典
            for i in range(self.cluster_num):
                self.result[i] = []
            # 划分
            for data in self.dataset:
                index = 0
                min_distance = sys.maxsize
                for i in range(self.cluster_num):
                    """分别对每个点计算其到N个簇中心的距离"""
                    _distance = self._distance(data, self.center_points[i])
                    if _distance < min_distance:
                        index = i
                        min_distance = _distance
                self.result[index].append(data)
            # 求中心点
            new_center = []
            for i in range(self.cluster_num):
                if len(self.result[i]) is 0:
                    new_center.append(self.center_points[i])
                else:
                    new_center.append(self._center(self.result[i]))
            if new_center == self.center_points:
                return
            else:
                self.center_points = new_center

    @staticmethod
    def _distance(p1, p2):
        """欧氏距离"""
        _sum = 0
        for i in range(len(p1)):
            _sum += pow(p1[i] - p2[i], 2)
        return pow(_sum, 0.5)

    @staticmethod
    def _center(_list):
        return np.array(_list).mean(axis=0).tolist()


if __name__ == '__main__':

    with open("./xclara.csv", encoding='utf-8-sig') as f:
        dataset_unprocess = f.readlines()
    dataset_unprocess.pop(0)
    dataset_tmp = []
    for tmp in dataset_unprocess:
        d = []
        for i in tmp.strip().split(","):
            d.append(float(i))
        dataset_tmp.append(d)
    km = KMeans(dataset_tmp, 3)
    km.fit()
    print(km.result)

    # 绘制各个簇
    color = ['#0dceda', '#1fab89', '#8971d0']
    for k, v in km.result.items():
        x_list = []
        y_list = []
        for x, y in v:
            x_list.append(x)
            y_list.append(y)
        plt.plot(x_list, y_list, '.b', color=color[k])

    # 绘制簇中心点
    x_list = []
    y_list = []
    for x, y in km.center_points:
        x_list.append(x)
        y_list.append(y)
    plt.plot(x_list, y_list, '+', color='black')
    plt.show()
