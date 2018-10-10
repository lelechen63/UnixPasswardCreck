from crypt import crypt
import multiprocessing

def get_real():
	_file = open( "./password17_cipher.txt", "rb")
	train_data = _file.readlines()
	_file.close()
	real = []
	for line in train_data:
		num = {}
		usrname, psd  = line.split()
		psd = psd[2:]
		num[psd] = usrname
		real.append(num)
	return real
def get_fake(index):
	_file = open( "./crackstation.txt", "rb")
	line = _file.readline()
	big_pool = {}
	count = 0
	while line:
		if count < index * 1000000:
			continue
		try:
			line = line[:-1]
			fake_password = crypt(line, '00')[2:]
			big_pool[fake_password] = line
			count += 1
			line = f.readline()
		except:
			line = f.readline()
			continue
		
		if count == 1000000 * (index + 1):
			return big_pool
	return big_pool    

def multi_pool(index):
	real =get_real()
	fake = get_fake(index)
	num_thread = 4
	for i in range(num_thread):
	    process = multiprocessing.Process(
	        target=find_same, args=(real[i], fake,))
	    process.start()


def find_same(reals, fake):
	psd = reals.keys()[0]
	
	for index, key in enumerate(fake) :
		if key == psd:
			print ('==============')
			print (fake[key], key)
for i in range(1300):
	multi_pool(i)

multi_pool()