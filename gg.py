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
def get_fake():
	_file = open( "./crackstation.txt", "rb")
	pool = _file.readlines()
	_file.close()
	big_pool = {}
	for line in pool:
		try:
			line = line[:-1]
			fake_password = crypt(line, '00')[2:]
			big_pool[fake_password] = line
		except:
			continue
	return big_pool    

def multi_pool():
	real =get_real()
	fake = get_fake()
	num_thread = 215
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
multi_pool()