#!/usr/bin/env python

## -*-Pyth-*-
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "linearCGSSolver.py"
 #
 #  Author: Jonathan Guyer <guyer@nist.gov>
 #  Author: Daniel Wheeler <daniel.wheeler@nist.gov>
 #  Author: James Warren   <jwarren@nist.gov>
 #    mail: NIST
 #     www: http://www.ctcms.nist.gov/fipy/
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  FiPy is an experimental # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  
 # ###################################################################
 ##

__docformat__ = 'restructuredtext'

import sys

from pysparse import itsolvers

from fipy.solvers.pysparse.pysparseSolver import PysparseSolver

class LinearCGSSolver(PysparseSolver):

    """

    The `LinearCGSSolver` solves a linear system of equations using
    the conjugate gradient squared method (CGS), a variant of the
    biconjugate gradient method (BiCG). CGS solves linear systems with
    a general non-symmetric coefficient matrix.

    The `LinearCGSSolver` is a wrapper class for the the PySparse_
    `itsolvers.cgs()` method.

    .. _PySparse: http://pysparse.sourceforge.net

    
    """
    def __init__(self, precon=None, *args, **kwargs):
        """
        :Parameters:
          - `precon`: Preconditioner to use
        """
        import warnings
        warnings.warn("The PySparse CGS solver may return incorrect results for some matrices", UserWarning)
        PysparseSolver.__init__(self, precon=precon, *args, **kwargs)
        self.solveFnc = itsolvers.cgs

