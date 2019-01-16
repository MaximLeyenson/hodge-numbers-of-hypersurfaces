# Hodge numbers of hypersurfaces and complete intersections

This Python program computes the Hodge numbers of a hypersurface in a projective space.

   requires the 'SymPy' module

 It can easily be modified to work with complete intersections.

 Usage:
 
  $ python -i a.py

   HS(n,d)

   where 
      n is the dimension of V, and 
      d is the degree.

   Example:

   n = 2, d = 4 (K3 surface)
   
   >> HS(2,4)

   1    0    1
   0    20   0
   1    0    1  


   n = 3, d = 5 (3-dimensional Calabi-Yao)

    ⎡1   0    0   1⎤
    ⎢              ⎥
    ⎢0  101   1   0⎥
    ⎢              ⎥
    ⎢0   1   101  0⎥
    ⎢              ⎥
    ⎣1   0    0   1⎦



 References:

     * Deligne in SGA 7, part 2
       Exposé XI. 
       Cohomologie des intersections complètes
       very well written
       works in any characteristics

     * Hirzebruch's book
       "Topological methods in algebraic geometry"
       Schwarzenberger's appendix

     * https://math.stackexchange.com/questions/606592/hodge-diamond-of-complete-intersections


 For the odd dimension of a variety it looks like

 |  *     1
 |    * 1
 |    1 *
 |  1     *
   ---------

 and for the even dimension of the variety it looks like


 |  *      1
 |    *  1
 |     * 
 |    1  *
 |  1      *
   ---------
          
