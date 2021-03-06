import pandas as pd
import numpy as np
import os
from tqdm import *
from multiprocessing import Pool, cpu_count

def my_process1(file_name):
    emb_path = '../../models/vgg_face2/resnet50_scratch_pytorch/embedding/train/%s'%file_name.replace('.png', '.npy')
    emb = np.load(emb_path)
    return emb

def my_process2(file_name):
    emb_path = '../../models/vgg_face2/resnet50_scratch_pytorch/embedding/train/%s'%file_name.replace('.png', '_flip.npy')
    emb = np.load(emb_path)
    return emb

def my_process3(file_name):
    emb_path = '../../models/vgg_face2/resnet50_scratch_pytorch/embedding/test/%s'%file_name.replace('.png', '.npy')
    emb = np.load(emb_path)
    return emb

def my_process4(file_name):
    emb_path = '../../models/vgg_face2/resnet50_scratch_pytorch/embedding/test/%s'%file_name.replace('.png', '_flip.npy')
    emb = np.load(emb_path)
    return emb

if __name__ == '__main__':
    test_df = pd.read_csv('../../datasets/test_refined.csv')
    train_df = pd.read_csv('../../datasets/train_refined.csv')

    p = Pool(8)
    train_data = p.map(func=my_process1, iterable = train_df.image.values.tolist())
    p.close()
    train_data = np.array(train_data)
    print(train_data.shape)
    np.save('train_data.npy', train_data)
    train_data = []

    p = Pool(8)
    train_flip_data = p.map(func=my_process2, iterable = train_df.image.values.tolist())
    p.close()
    train_flip_data = np.array(train_flip_data)
    print(train_flip_data.shape)
    np.save('train_flip_data.npy', train_flip_data)
    train_flip_data = []

    p = Pool(8)
    test_data = p.map(func=my_process3, iterable = test_df.image.values.tolist())
    p.close()
    test_data = np.array(test_data)
    print(test_data.shape)
    np.save('test_data.npy', test_data)
    test_data = []

    p = Pool(8)
    test_flip_data = p.map(func=my_process4, iterable = test_df.image.values.tolist())
    p.close()
    test_flip_data = np.array(test_flip_data)
    print(test_flip_data.shape)
    np.save('test_flip_data.npy', test_flip_data)
    test_flip_data = []