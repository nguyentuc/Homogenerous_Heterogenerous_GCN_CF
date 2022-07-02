## Homogenerous_Heterogenerous_GCN_CF
This is the source of the implement of GCN Collaborative Filtering GCNs with homogenerous and heterogenerous graph structure.

## Introduction
In recent years, Graph Convolutional Networks (GCNs) have demonstrated their superiority in Collaborative  Filtering, where the data are often extremely sparse.
GCNs is able to exploit graph data as input to learn good embeddings of users and items, where a graph often contains semantic signals between items and/or users.
In this paper, we show that the embeddings achieve by GCNs are not enough to make accurate predictions on user-item pairs.
We design four GCN-based models to investigate the benefit of taking nonlinear operations for prediction. 
We evaluate these models with the different types of loss functions (cross-entropy and ranking loss). 
The role of negative sampling in cross-entropy (CE) loss function is also discussed.
We design extensive experiments to show the role of the different components and why GCN-based can better deal with the challenge of sparsity.
We also discuss how to manage large graphs to efficiently train GCN-based models, which could be useful for practical applications. 

## The libaries are requries
```
python3
tensorflow 1.15
pandas
numpy
progressbar
```
## Dataset
We also provide the scripts for pre-processing the datasets. For the raw and preprocessed data, please reach me via: nguyentuc1003@gmail.com. 


