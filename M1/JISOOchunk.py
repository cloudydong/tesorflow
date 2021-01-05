import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

x = np.arange(1, 100)
y = x
z = x*x
arr = [y, z, y, z, z, z, z, z]


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def create_pdf(row, col):
    with PdfPages('multi_page_chunk.pdf') as pdf:
        for i, f in enumerate(chunks(arr, (row*col))):
            fig, ax = plt.subplots(nrows=row, ncols=col)
            for j, axi in enumerate(ax.flat):
                axi.set_title(i*(row*col)+j)
                axi.plot(x, f[j])
            pdf.savefig()
            plt.close()


create_pdf(2, 2)
