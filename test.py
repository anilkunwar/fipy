#!/usr/bin/env python

## 
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "test.py"
 #                                    created: 11/26/03 {3:23:47 PM}
 #                                last update: 4/2/04 {4:02:18 PM} { 2:26:30 PM}
 #  Author: Jonathan Guyer
 #  E-mail: guyer@nist.gov
 #  Author: Daniel Wheeler
 #  E-mail: daniel.wheeler@nist.gov
 #    mail: NIST
 #     www: http://ctcms.nist.gov
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  PFM is an experimental
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
 #  Description: 
 # 
 #  History
 # 
 #  modified   by  rev reason
 #  ---------- --- --- -----------
 #  2003-11-10 JEG 1.0 original
 # ###################################################################
 ##

"""Run all the test cases
"""

import unittest

import examples.test
import fipy.test
##import fipy.meshes.pyMesh.test
##import fipy.meshes.numMesh.test
##import fipy.tools.test
import fipy.tests.testProgram
##import fipy.variables.test

def suite():
    theSuite = unittest.TestSuite()
    theSuite.addTest(examples.test.suite())
    theSuite.addTest(fipy.test.suite())
##    theSuite.addTest(fipy.tools.test.suite())
##    theSuite.addTest(fipy.meshes.numMesh.test.suite())
##    theSuite.addTest(fipy.meshes.pyMesh.test.suite())
##    theSuite.addTest(fipy.variables.test.suite())
    return theSuite

if __name__ == '__main__':
    fipy.tests.testProgram.main(defaultTest='suite')
