from crypt import crypt
# import torch
from dataset import Password
import argparse
import os
import glob
import time
import torch
from torch.utils.data import DataLoader
import numpy as np
from collections import OrderedDict
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch_size",
                        type=int,
                        default=6)
    
    parser.add_argument("--cuda",
                        default=True)  
    parser.add_argument('--device_ids', type=str, default='3')
    parser.add_argument('--num_thread', type=int, default=1)
    # parser.add_argument('--flownet_pth', type=str, help='path of flownets model')

    return parser.parse_args()
config = parse_args()

def get_real():
	_file = open( "./password.txt", "rb")
	train_data = _file.readlines()
	_file.close()
	real = []

	for line in train_data:
		num = []
		line = line[:-1]
		fake_password = crypt(line, '00')[2:]
		for ch in fake_password:
			num.append(ord(ch)) 
		real.append(num)
	real = np.asarray(real).astype(int)
	real = torch.Tensor(real)
	real = real.unsqueeze(0)
	real = real.repeat(config.batch_size, 1,1)

	return real

def test():
	file = open("./gt.txt",'w') 
	os.environ["CUDA_VISIBLE_DEVICES"] = config.device_ids
	real_password = get_real().cuda()
	dataset =  Password()
	data_loader = DataLoader(dataset,
	                                  batch_size=config.batch_size,
	                                  num_workers= config.num_thread,
	                                  shuffle=False, drop_last=True)
	
	for step, (gt, fake_password) in enumerate(data_loader):
		if config.cuda:
			fake_password = fake_password.cuda()
		print (gt)
		fake_password = fake_password.unsqueeze(1)
		fake_password = fake_password.repeat(1,6,1)
		diff = fake_password - real_password
		diff = torch.sum(diff, dim= 2)
		inds = (diff == 0).nonzero()[1]
		return gt[inds]


test()
