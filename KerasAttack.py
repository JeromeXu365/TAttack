import numpy as np

fname = MODEL_PATH + 'attack_train_data.npz'
with np.load(fname) as f:
        train_x, train_y = [f['arr_%d' % i] for i in range(len(f.files))]
fname = MODEL_PATH + 'attack_test_data.npz'
with np.load(fname) as f:
        test_x, test_y = [f['arr_%d' % i] for i in range(len(f.files))]