"""Assess a betting strategy.

Copyright 2018, Georgia Institute of Technology (Georgia Tech)
Atlanta, Georgia 30332
All Rights Reserved

Template code for CS 4646/7646

Georgia Tech asserts copyright ownership of this template and all derivative
works, including solutions to the projects assigned in this course. Students
and other users of this template code are advised not to share it with others
or to make it available on publicly viewable websites including repositories
such as github and gitlab.  This copyright statement should not be removed
or edited.

We do grant permission to share solutions privately with non-students such
as potential employers. However, sharing with other current or future
students of CS 7646 is prohibited and subject to being investigated as a
GT honor code violation.

-----do not edit anything above this line---

Student Name: Michael Groff (replace with your name)
GT User ID: mgroff3 (replace with your User ID)
GT ID: 902772277 (replace with your GT ID)
"""

import numpy as np
import matplotlib.pyplot as plt

def author():
    return 'mgroff3' # replace tb34 with your Georgia Tech username.

def gtid():
	return 902772277 # replace with your GT ID number

def get_spin_result(win_prob):
	result = False
	if np.random.random() <= win_prob:
		result = True
	return result

def spin_thousands(win_prob):
    w = np.zeros(1000)
    t = 0
    b = 1
    for x in np.nditer(w, op_flags = ['readwrite']):
        if t == 80:
            x[...] = t
            continue
        if get_spin_result(win_prob):
            t = t + b
            b = 1
        else:
            t = t-b
            b = b*2
        x[...] = t
    return w

def spin_256(win_prob):
    w = np.zeros(1000)
    t = 0
    b = 1
    h = False
    for x in np.nditer(w, op_flags = ['readwrite']):
        if t == 80:
            x[...] = t
            continue
        if t == -256:
            x[...] = t
            continue
        if get_spin_result(win_prob):
            t = t + b
            if h:
                b = c-b
                h = False
            else:
                b=1
        else:
            t = t-b
            b = b*2
        x[...] = t
        if t-b < -256:
            c = b
            b = t+256
            h = True
    return w

def test_code():
    win_prob = 18.0/38
    np.random.seed(gtid())

    winnings = np.append(0,spin_thousands(win_prob))
    for i in range(0,9):
        winnings = np.vstack((winnings,  np.append(0,spin_thousands(win_prob))))
    r = np.arange(0,1001,1)
    plt.figure(1)
    plt.ylim(-256,100)
    plt.xlim(0,300)
    plt.xlabel("Successive Bets")
    plt.ylabel("Total Winings")
    for i in range(0,10):
        plt.plot(r, winnings[i,:])
    plt.savefig('f1.png', bbox_inches='tight')

    winnings = np.append(0,spin_thousands(win_prob))
    for i in range(0,999):
        winnings = np.vstack((winnings,  np.append(0,spin_thousands(win_prob))))

    mdata = np.zeros((7,1001))
    mdata[0,:] = np.mean(winnings, axis = 0)
    mdata[1,:] = np.median(winnings, axis = 0)
    mdata[2,:] = np.std(winnings, axis = 0)
    mdata[3,:] = np.add(mdata[0,:],mdata[2,:])
    mdata[4,:] = np.subtract(mdata[0,:],mdata[2,:])
    mdata[5,:] = np.add(mdata[1,:],mdata[2,:])
    mdata[6,:] = np.subtract(mdata[1,:],mdata[2,:])

    plt.figure(2)
    plt.ylim(-256,100)
    plt.xlim(0,300)
    plt.xlabel("Successive Bets")
    plt.ylabel("Total Winings")
    plt.plot(r, mdata[0,:])
    plt.plot(r, mdata[3,:])
    plt.plot(r, mdata[4,:])
    plt.savefig('f2.png', bbox_inches='tight')
    plt.figure(3)
    plt.ylim(-256,100)
    plt.xlim(0,300)
    plt.xlabel("Successive Bets")
    plt.ylabel("Total Winings")
    plt.plot(r, mdata[1,:])
    plt.plot(r, mdata[5,:])
    plt.plot(r, mdata[6,:])
    plt.savefig('f3.png', bbox_inches='tight')

    winnings = np.append(0,spin_256(win_prob))
    for i in range(0,999):
        winnings = np.vstack((winnings,  np.append(0,spin_256(win_prob))))

    mdata = np.zeros((7,1001))
    mdata[0,:] = np.mean(winnings, axis = 0)
    mdata[1,:] = np.median(winnings, axis = 0)
    mdata[2,:] = np.std(winnings, axis = 0)
    mdata[3,:] = np.add(mdata[0,:],mdata[2,:])
    mdata[4,:] = np.subtract(mdata[0,:],mdata[2,:])
    mdata[5,:] = np.add(mdata[1,:],mdata[2,:])
    mdata[6,:] = np.subtract(mdata[1,:],mdata[2,:])

    plt.figure(4)
    plt.ylim(-256,100)
    plt.xlim(0,300)
    plt.xlabel("Successive Bets")
    plt.ylabel("Total Winings")
    plt.plot(r, mdata[0,:])
    plt.plot(r, mdata[3,:])
    plt.plot(r, mdata[4,:])
    plt.savefig('f4.png', bbox_inches='tight')
    plt.figure(5)
    plt.ylim(-256,100)
    plt.xlim(0,300)
    plt.xlabel("Successive Bets")
    plt.ylabel("Total Winings")
    plt.plot(r, mdata[1,:])
    plt.plot(r, mdata[5,:])
    plt.plot(r, mdata[6,:])
    plt.savefig('f5.png', bbox_inches='tight')

if __name__ == "__main__":
    test_code()
