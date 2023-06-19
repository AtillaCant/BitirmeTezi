import numpy as np
def samplesize(ci, d, p):

    if ci == 0.95:
        ratio, prop = 1.96/d, p*(1-p)
        ssize = ratio*ratio*prop
    elif ci == 0.96:
        ratio, prop = 2.05/d, p*(1-p)
        ssize = np.power(ratio, 2)*prop
    elif ci == 0.98:
        ratio, prop = 2.33/d, p*(1-p)
        ssize = np.power(ratio, 2)*prop

    return int(np.ceil(ssize))


def main():
    ci, d, p = 0.95, 0.05, 0.5
    sample_size = samplesize(ci, d, p)
    print('n: %d' % (sample_size))
if __name__ == "__main__":
   main()


