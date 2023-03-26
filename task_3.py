file_list = ['file_1.txt', file_2.txt','file_3.txt' ]
new_file_list = ['n_file_1.txt', 'n_file_2.txt','n_file_3.txt' ]
new_data_from_files = []
step = 0
while step < len(file_list):

     with open(file_list[step],encoding='UTF-8') as f:
          data = f.readlines()
          file_str = len(data)
     with open(file_list[step],encoding='UTF-8') as f:
          data_text = f.read()

     with open(new_file_list[step], 'w') as f:
         f.write(f'{file_list[step]}\n')
         f.write(f'{file_str}\n')
         f.write(f'{data_text}\n')
     step +=1
for some_file in new_file_list:
     with open(some_file) as f:
         new_data = f.read()
         new_data_from_files.append(new_data)
new_data_from_files.sort(key=len)

with open('finish_file.txt', 'a') as f:
    for some_pat in new_data_from_files:
          f.write(f'{some_pat}')
