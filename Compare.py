import numpy as np
from scipy.io.wavfile import read
from Algorithm.LBG import EUDistance
from Method.mel_coefficients import mfcc
from Method.LPC import lpc
from train import training1
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def LVH():
    messagebox.showinfo("","Compare successfully")
    nSpeaker = 8
    nfiltbank = 12
    orderLPC = 15
    (codebooks_mfcc, codebooks_lpc) = training1(nfiltbank, orderLPC)
    directory = os.getcwd() + '/Test'
    fname = str()
    nCorrect_MFCC = 0
    nCorrect_LPC = 0

    def minDistance(features, codebooks):
        speaker = 0
        distmin = np.inf
        for k in range(np.shape(codebooks)[0]):
            D = EUDistance(features, codebooks[k,:,:])
            dist = np.sum(np.min(D, axis = 1))/(np.shape(D)[0]) 
            if dist < distmin:
                distmin = dist
                speaker = k
        return speaker


    # Create a Tkinter window
    win = tk.Tk()
    win.title("Speaker Recognition")
    win.geometry("650x600+650+100")
    # Create a text box to display the results
    result_textbox = tk.Text(win, height=1000, width=500)
    result_textbox.pack()

    for i in range(nSpeaker):
        fname = '/s' + str(i+1) + '.wav'
        result_textbox.insert(tk.END, 'Now speaker ' + str(i+1) + ' features are being tested\n')
        (fs,s) = read(directory + fname)
        mel_coefs = mfcc(s,fs,nfiltbank)
        lpc_coefs = lpc(s, fs, orderLPC)
        sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
        sp_lpc = minDistance(lpc_coefs, codebooks_lpc)
        
        result_textbox.insert(tk.END, 'Speaker ' + str(i+1) + ' in Test matches with speaker ' + str(sp_mfcc+1) + ' in Train for training with MFCC\n')
        result_textbox.insert(tk.END, 'Speaker ' + str(i+1) + ' in Test matches with speaker ' + str(sp_lpc+1) + ' in Train for training with LPC\n\n')
    
        if i == sp_mfcc:
            nCorrect_MFCC += 1
        if i == sp_lpc:
            nCorrect_LPC += 1

    percentageCorrect_MFCC = (nCorrect_MFCC/nSpeaker)*100
    # result_textbox.insert(tk.END, 'Accuracy of result for training with MFCC is ' + str(percentageCorrect_MFCC) + '%\n')
    percentageCorrect_LPC = (nCorrect_LPC/nSpeaker)*100
    # result_textbox.insert(tk.END, 'Accuracy of result for training with LPC is ' + str(percentageCorrect_LPC) + '%\n')

    result_textbox.insert(tk.END, 'Accuracy of result for training:' +'\n')
    result_textbox.insert(tk.END, f"| {'MFCC': <5} | {'LPC': <5} |" +'\n')
    result_textbox.insert(tk.END, "-"*17 +'\n')
    result_textbox.insert(tk.END,  "| " + str(percentageCorrect_MFCC) +"% | " +str(percentageCorrect_LPC)+ "% |")
    

    # Start the Tkinter event loop
    win.mainloop()
LVH()


