ORI_TRAIN = "../train_test_inputs/eigen_train_files_with_gt_ori.txt"

TRAIN = "../train_test_inputs/eigen_train_files_with_gt.txt"

N = 2

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
                f.write(line.replace(".png", ".jpg", 1) + "\n")
                i += 1

def main():
    train_lines = readFile(ORI_TRAIN)
    writeFile(TRAIN, train_lines)

if __name__=='__main__':
    main()