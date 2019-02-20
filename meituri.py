def start():
	id=1000
	number=100
	
	while id<20000:
		id=id+1
		album=str(id)
		out = []
		
		# if len(sys.argv) == 3:
		# 	album = int(sys.argv[1])
		# 	number = int(sys.argv[2])
		# 	out = []
		# else:
		# 	print(strings('err_args'))
		# 	return
		
		path = f'albums/hywly-{album}/'
		try:
			if not os.path.exists(path):
				os.makedirs(path)
		except NotADirectoryError as e:
			print(f'NotADirectoryError: {e}')
			return
		except OSError as e:
			print(f'OSError: {e}')
			return

		for x in range(1, number+1):
			out.append(URL.format(album, x))
		
		download_images(out, path)
	
def get_opener():
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]
	urllib.request.install_opener(opener)

def download_images(links, path):
	total_time = 0
	get_opener()
	for link in links:
		name = link.split('/')[-1]
		print(strings('down') % link)
		try:

			start = time.time()
			urllib.request.urlretrieve(link, path + name)
			end = time.time()
			passed = end - start
			total_time += passed
			print(strings('comp') % passed)

		except:
			continue

	print(strings('all_comp') % (len(links), total_time))
		


		

if __name__ == '__main__':
	start()
