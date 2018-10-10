from crypt import crypt
import multiprocessing

def get_real():
	_file = open( "./password17_cipher.txt", "rb")
	train_data = _file.readlines()
	_file.close()
	real = []
	for line in train_data:
		num = []
		usrname, psd  = line.split()
		psd = psd[2:]
		num.append(psd)
		num.append(usrname)
		real.append(num)
	return real
def get_fake():
	ggg = open( "./ggg.txt", "w")
	_file = open( "./crackstation.txt", "rb")
	line = _file.readline()
	count = 0
	real =get_real()
	result = []
	while line:
		print (count)
		try:
			line = line[:-1]
			fake_password = crypt(line, '00')[2:]
			for gg in real:
				psd = gg[0]
				usrname = gg[1]
				if fake_password == psd:
					ggg.write(line + ',' + psd + ',' + usrname + '\n')
					result.append(line + ',' + psd + ',' + usrname)
					
			count += 1
			line = _file.readline()
		except:
			line = _file.readline()
			continue
	print (result)
get_fake()	
# def multi_pool(index):
# 	real =get_real()
# 	fake = get_fake(index)
# 	num_thread = 4
# 	for i in range(num_thread):
# 	    process = multiprocessing.Process(
# 	        target=find_same, args=(real[i], fake,))
# 	    process.start()


# def find_same(reals, fake):
# 	psd = reals.keys()[0]
	
# 	for index, key in enumerate(fake) :
# 		if key == psd:
# 			print ('==============')
# 			print (fake[key], key)


# for i in range(1300):
# 	multi_pool(i)
