import os

filepaths = ['dataset/Cornell_CS_Movie_Review/Review/tokens/neg','dataset/Cornell_CS_Movie_Review/Review/tokens/pos']

p_n = ['neg_','pos_']

for i in range(2):
    
    filelist = os.listdir(filepaths[i])

    for name in filelist:
        txt_f = os.path.join(filepaths[i], name)
        new_name = p_n[i]+name
        new_name = os.path.join(filepaths[i], new_name)
        os.rename(txt_f, new_name)
        print(os.path.join(filepaths[i], new_name))
