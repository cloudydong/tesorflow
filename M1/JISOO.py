import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

x = np.arange(1, 100)
y = x
z = x*x
arr = [y, z, y, z, z, z, y, z]


def create_pages(row, col):
    with PdfPages('multi_page_pdf.pdf') as pdf:
        idx = 0
        for cnt in range(len(arr) // (row*col)):
            fig, ax = plt.subplots(nrows=row, ncols=col)
            for i, axi in enumerate(ax.flat):
                axi.set_title(idx)
                axi.plot(x, arr[idx])
                idx += 1
                print(idx)
            pdf.savefig()
        plt.close()


create_pages(2, 2)
