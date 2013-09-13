# Import the numpy package
import numpy

def copyW(q,w,js,iq,qrows):

    #  Copy the eigenvectors corresponding to the largest roots into the
    #  remaining empty rows and columns js of q 

    # Author: Gary Anderson
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
    
    
    if iq < qrows:
        lastrows = range(iq,qrows+1)
        wrows = range(0,len(lastrows))
        q[lastrows-1,js-1] = w[:,wrows-1].T

    return q
