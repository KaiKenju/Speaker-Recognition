from train import training
import os
from tkinter import messagebox
def fig():
    messagebox.showinfo("","Figure adready")
    nSpeaker = 8
    nfiltbank = 12
    orderLPC = 15
    (codebooks_mfcc, codebooks_lpc) = training(nfiltbank, orderLPC)
    directory = os.getcwd() + '/test'
    fname = str()
    nCorrect_MFCC = 0
    nCorrect_LPC = 0