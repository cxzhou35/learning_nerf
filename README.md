# Learning NeRF

This repository is initially created by [Haotong Lin](https://haotongl.github.io/).

## Data preparation

Download NeRF synthetic dataset and add a link to the data directory. After preparation, you should have the following directory structure:

```
data/nerf_synthetic
|-- chair
|   |-- test
|   |-- train
|   |-- val
|-- drums
|   |-- test
......
```

## 复现NeRF

### 配置文件

已经在configs/nerf/ 创建好了一个配置文件，nerf.yaml。其中包含了复现NeRF必要的参数。
可以根据自己的喜好调整对应的参数的名称和风格。

### 创建dataset： lib.datasets.nerf.synthetic.py

核心函数包括：init, getitem, len.

init函数负责从磁盘中load指定格式的文件，计算并存储为特定形式。

getitem函数负责在运行时提供给网络一次训练需要的输入，以及groundtruth的输出。
例如对NeRF，分别是1024条rays以及1024个RGB值。

len函数是训练或者测试的数量。getitem函数获得的index值通常是[0, len-1]。

#### debug

```
python run.py --type dataset --cfg_file configs/img_fit/lego_view0.yaml
```

### 创建network

核心函数包括：init, forward.

init函数负责定义网络所必需的模块，forward函数负责接收dataset的输出，利用定义好的模块，计算输出。例如，对于NeRF来说，我们需要在init中定义两个mlp以及encoding方式，在forward函数中，使用rays完成计算。

#### debug

```
python run.py --type network --cfg_file configs/img_fit/lego_view0.yaml
```

### loss模块和evaluator模块

这两个模块较为简单，不作仔细描述。

debug方式分别为：

```
python train_net.py --cfg_file configs/img_fit/lego_view0.yaml
```

```
python run.py --type evaluate --cfg_file configs/img_fit/lego_view0.yaml
```

## 问题记录

复现过程中出现的一些问题记录在这里: [Issues](https://github.com/cxzhou35/learning_nerf/blob/master/Issues.md)
