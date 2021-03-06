ORI_TRAIN = "mono/datasets/splits/eigen_full/train_files_ori.txt"
ORI_VAL = "mono/datasets/splits/eigen_full/val_files_ori.txt"
TRAIN = "mono/datasets/splits/eigen_full/train_files.txt"
VAL = "mono/datasets/splits/eigen_full/val_files.txt"
N = 1500

def readFile(path):
    with open(path) as f:
        lines = f.read().splitlines()
    return lines
def writeFile(path, lines):
    i = 0
    with open(path, 'w') as f:
        for line in lines:
            if i > N:
                break
            if "2011_09_26" in line:
                f.write(line + "\n")
                i += 1

def main():
    train_lines = readFile(ORI_TRAIN)
    writeFile(TRAIN, train_lines)
    val_lines = readFile(ORI_VAL)
    writeFile(VAL, val_lines)
if __name__=='__main__':
    main()