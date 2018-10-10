class Password(data.Dataset):
    def __init__(self,
                 dataset_dir,
                 output_shape=[128, 128],
                 train='train'):
        self.train = train
        self.root ='/mnt/disk1/dat/lchen63/vgg_face_dataset/'
        _file = open(os.path.join(dataset_dir, "test.pkl"), "rb")
        self.train_data = pickle.load(_file)
        _file.close()
       
    def __getitem__(self, index):
        # In training phase, it return real_image, wrong_image, text
                # try:
        print ('------')
        image_path =  self.train_data[index][0]
        label = self.train_data[index][1]
        # print ('------')

        im = cv2.imread(image_path)
        if im is None:
            raise IOError
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        im = cv2.resize(im, self.output_shape)
        im = self.transform(im)
        # print ('------')


        return im, label

           

    def __len__(self):
        return len(self.train_data)
       