import numpy as np


def proportional_method(I, A):
    '''
    Inputs:
        I = indicator array to be use in the benchmark. 
        Ordered from t0 to tn (high frequncy) ex. quarterly data
        A =  aggregate data represented as every element as mean of a the n subset of I 
        (in the same order) (low frequncy) ex. annual data
        I/A has to be integer i.e the elements in the indicator data must the multiple of A.
    Output
        B = array with high frequency interpolation of the high frequency data in the low frequency
    
    Example:
    Taken from: https://www.imf.org/external/pubs/ft/qna/pdf/2017/chapter6.pdf
    Table: Example 6.2
    
    import numpy as np
    import denton

    I = np.array([99.4,99.6,100.1,100.9,101.7,102.2,102.9,
         103.8,104.9,106.3,107.3,107.8,107.9,
         107.5,107.2,107.5])
    A = np.array([1000, 1040, 1060.8, 1064.9])
    
    #the average of every 4 in the data annual data
    B = denton.proportional_method(I, A)    

    #to replicate the table then divide by 4
    B_imf = denton.proportional_method(I, A)/4

    '''
    len_A, len_I, q = len(A), len(I), int(len(I)/len(A)) 
    I_tilde = np.linalg.pinv(np.diag(I))
    I, A = I[:, np.newaxis], A[:, np.newaxis]

    D = -1 * np.eye(len_I)
    D[-1, -1] = 0
    for i in range(len(D)-1):
        D[i, i+1] = 1

    J = np.zeros((len_A, len_I))
    for j in range(len(J)):
        J[j, j*q:j*q + q] = [1]*q

    M = I_tilde.T @ D.T @ D @ I_tilde
    r1, r2 = np.concatenate((M + M.T, -J.T), axis=1), np.concatenate((J, np.zeros((len_A, len_A))), axis=1)
    Z = np.concatenate((r1, r2), axis=0)
    X_lambda = np.linalg.pinv(Z) @ np.concatenate((np.zeros((len_I ,1)), A), axis=0)
    X = X_lambda[:-len_A]
    rv = X*q
    return rv

