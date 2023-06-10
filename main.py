from __future__ import division
from scipy.io.wavfile import read
from Method.mel_coefficients import mfcc
from Method.LPC import lpc
from train import training
import os
from test import minDistance


nSpeaker = 8
nfiltbank = 12
orderLPC = 15
(codebooks_mfcc, codebooks_lpc) = training(nfiltbank, orderLPC)
directory = os.getcwd() + '/Test'
fname = str()
nCorrect_MFCC = 0
nCorrect_LPC = 0

#Show that the speaker who is match in Test folder and Train folder (LPC or MFCC)
for i in range(nSpeaker):
    fname = '/s' + str(i+1) + '.wav'
    print('Now speaker ', str(i+1), 'features are being tested')
    (fs,s) = read(directory + fname)
    mel_coefs = mfcc(s,fs,nfiltbank)
    lpc_coefs = lpc(s, fs, orderLPC)
    sp_mfcc = minDistance(mel_coefs, codebooks_mfcc)
    sp_lpc = minDistance(lpc_coefs, codebooks_lpc)
    
    print('Speaker ', (i+1), ' in Test matches with speaker ', (sp_mfcc+1), ' in Train for training with MFCC')
    print('Speaker ', (i+1), ' in Test matches with speaker ', (sp_lpc+1), ' in Train for training with LPC')
   
    if i == sp_mfcc:
        nCorrect_MFCC += 1
    if i == sp_lpc:
        nCorrect_LPC += 1


percentageCorrect_MFCC = (nCorrect_MFCC/nSpeaker)*100
print('Accuracy of result for training with MFCC is ', percentageCorrect_MFCC, '%')
percentageCorrect_LPC = (nCorrect_LPC/nSpeaker)*100
print('Accuracy of result for training with LPC is ', percentageCorrect_LPC, '%')


    
