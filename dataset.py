import torch.utils.data as data
from crypt import crypt
import numpy as np
import torch
class Password(data.Dataset):
    def __init__(self):

        self._file = open( "./pool.txt", "rb")
        self.train_data = self._file.readlines()
        self._file.close()
       
    def __getitem__(self, index):
        line = self.train_data[index][:-1]
        fake_password = crypt(line, '00')[2:]
        num = []
        for ch in fake_password:
            num.append(ord(ch)) 
        num = np.asarray(num).astype(int)
        num = torch.Tensor(num)
        return line, num 
    def __len__(self):
        return len(self.train_data)
       