#!/usr/bin/env python

## -*-Pyth-*-
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "implicitSourceTerm.py"
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
 # protection and is in the public domain.  FiPy is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
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

from fipy.terms.sourceTerm import SourceTerm
from fipy.tools import numerix

class ImplicitSourceTerm(SourceTerm):
    r"""

    The `ImplicitSourceTerm` represents

    .. math::

       \int_V \phi S \,dV \simeq \phi_P S_P V_P 
       
    where :math:`S` is the `coeff` value.       
    """

    def _getWeight(self, var, transientGeomCoeff=None, diffusionGeomCoeff=None):
        """
        Test for a bug due to the sign operator not being updating
        correctly.

            >>> from fipy import *
            >>> m = Grid1D(nx=1)
            >>> v = CellVariable(mesh=m, value=1.)
            >>> eq = TransientTerm() == ImplicitSourceTerm(v)
            >>> eq.solve(v)
            >>> print v
            [ 2.]
            >>> v.setValue(-1.)
            >>> eq.solve(v)
            >>> print v
            [-0.5]
            
        """
        if transientGeomCoeff is not None:
            if numerix.all(transientGeomCoeff >= 0):
                diagonalSign = 1
            elif numerix.all(transientGeomCoeff <= 0):
                diagonalSign = -1
            else:
                raise Exception, "Transient coefficient has both positive and negative values"
        elif diffusionGeomCoeff is not None:
            if numerix.all(diffusionGeomCoeff[0] <= 0):
                diagonalSign = 1
            elif numerix.all(diffusionGeomCoeff >= 0):
                diagonalSign = -1
            else:
                raise Exception, "Diffusion coefficient has both positive and negative values"
        else:
            diagonalSign = 1

        coeff = self._getGeomCoeff(var)
        combinedSign = diagonalSign * numerix.sign(coeff)

        return {'diagonal' : (combinedSign >= 0),
                'old value' : numerix.zeros(var.mesh.numberOfCells, 'd'),
                'b vector' :  -var * (combinedSign < 0),
                'new value' : numerix.zeros(var.mesh.numberOfCells, 'd')}
    
def _test(): 
    import doctest
    return doctest.testmod()
    
if __name__ == "__main__": 
    _test() 
