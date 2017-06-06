import re
import glob
import numpy as np

def main():
    dataset = []
    for f in glob.glob('heightweight/*.jpg'):
        m = re.match('heightweight\/(\d+)-(\d+)_.*', f)
        if m:
            h = int(m.group(1))
            height = float(int(h / 100) * 12 + (h % 100)) * 2.54
            weight = float(m.group(2))
            dataset.append((f, height, weight))

    total_sz = len(dataset)
    val_sz = int(total_sz * 0.15)
    test_sz = val_sz
    train_sz = total_sz - val_sz - test_sz

    ndata = np.array(dataset)
    np.random.shuffle(ndata)

    train = ndata[:train_sz]
    val = ndata[train_sz:train_sz+val_sz]
    test = ndata[train_sz+val_sz:]

    print "train, val, test size: ", len(train), len(val), len(test)

    print test[:,1]
    
main()
