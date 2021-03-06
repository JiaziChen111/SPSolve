# import numpy and scipy packages
from numpy import *
from scipy import *
from scipy.sparse import *
from numpy.linalg import *

def reducedForm(q,qrows,qcols,bcols,neq,condn):
    
    # Compute reduced-form coefficient matrix, b.
    
    # Original author: Gary Anderson
    # Original file downloaded from:
    # http://www.federalreserve.gov/Pubs/oss/oss4/code.html
    # Adapted for Dynare by Dynare Team.
    
    # This code is in the public domain and may be used freely.
    # However the authors would appreciate acknowledgement of the source by
    # citation of any of the following papers:

    # Anderson, G. and Moore, G.
    # "A Linear Algebraic Procedure for Solving Linear Perfect Foresight
    # Models."
    # Economics Letters, 17, 1985.
    
    # Anderson, G.
    # "Solving Linear Rational Expectations Models: A Horse Race"
    # Computational Economics, 2008, vol. 31, issue 2, pages 95-113
    
    # Anderson, G.
    # "A Reliable and Computationally Efficient Algorithm for Imposing the
    # Saddle Point Property in Dynamic Models"
    # Journal of Economic Dynamics and Control, 2010, vol. 34, issue 3,
    # pages 472-489
    
    qs = csr_matrix(q)
    left = range(0,qcols-qrows)
    right = range(qcols-qrows,qcols)
    nonsing = 1/cond(csr_matrix(qs[:,right]).todense()) > condn
    if nonsing:
        qs[:,left] = -qs[:,right].I * qs[:,left]
        b = qs[0:neq,0:bcols]
        b = csr_matrix(b).todense()
    else:  
        # rescale by dividing row by maximal qr element
        # inverse condition number small, rescaling
        themax = abs(qs[:,right]).max(axis=1)
        oneoverVector = list()
        for i in range(0,len(themax)):
            temp = 1 / themax[i]
            oneoverVector.append(temp)
        oneover = diag(oneoverVector)
        productMatrixRight = oneover * qs[:,right]
        nonsing = 1/cond(csr_matrix(productMatrixRight).todense()) > condn
        if nonsing:
            productMatrixLeft = oneover * qs[:,left]
            qs[:,left] = -productMatrixRight.I * productMatrixLeft
            b = qs[0:neq,0:bcols]
            b = csr_matrix(b).todense()

    return nonsing, b
