#!/usr/bin/python
# -*- coding: utf-8 -*-

#  using Unicode to reference Deligne's paper, etc

""" by Maxim Leyenson, <leyenson at gmail com>
   under the GNU license

   requires the 'SymPy' module

 --------

 This program computes the Hodge numbers of a hypersurface
 in a projective space.

 It can easily be modified to work with complete intersections.

 Usage:
 
  $ python3 -i a.py3.py

    >> HS(n,d)

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
          

"""


from sympy import Symbol


# formal power series, and polynomials

from sympy import series
from sympy import Poly # convert smth into a polynomial

# matrices
from sympy import eye # unit matrix

# pretty printing 
from sympy import pprint 


x=Symbol('x')
y=Symbol('y')
z=Symbol('z')


# for the hypersurface of degree d

# starting with a plane curve

r = 1       # codimension in the projective space


# = plane quartic =

# n = 1       # dimension of a variety
# d = 4       # plane quartic


# = cubic surface in P^3 =

# n = 2       # dimension of a variety
# d = 3       # cubic surface 

# = quartic surface in P^3 (K3) =

n = 2       # dimension of a variety
d = 4       # cubic surface 

# = quintic threefold in P^4 =

# n = 3       # dimension of a variety
# d = 5       # quintic threefold


# -----------------------------------
# for the hypersurface of degree d

def HS(n,d): # return Hodge numbers of a hypersurface 
   """return Hodge numbers of a hypersurface
      n is the dimension of V 
      d is the degree """
   print("dimension of V: ", n)
   print("degree of V: ", d)

   result = []

   RHS1 = 1 / ( (1-z) * (1 + y*z) )
   num = (1 + z * y)**d - (1 - z)**d

   den = (1 + z * y)**d + y * (1 - z)**d      

   RHS = RHS1 * num / den

   print("RHS =", RHS)

   # example: d = 4 => I get

   # (-(-z + 1)**4 + (y*z + 1)**4)/((-z + 1)*(y*z + 1)*(y*(-z + 1)**4 + (y*z + 1)**4)))

   # I am interested in the term at z^{n+r}

   z_series = RHS.series(z,0,n + r + 1)

   # it has O(z^{n+r+1})

   z_series = z_series.removeO()

   z_coeff = z_series.coeff(z**(n + r))

   # print "z_coeff = ", z_coeff

   # and thus we computed chi_y

   chi_y = z_coeff 

   # this is a coefficient at z^{n+r};
   # it is a function in y
   # example: for a plane quartic, it is 2*y**2/(y + 1) - 2/(y + 1)

   print("chi_y = ", chi_y)

   print("simplifying it; it should be a polynomial in y of degree n =", n)

   chi_y_simplified =  chi_y.simplify()

   # print "chi_y_simplified = ", chi_y_simplified 
   # print "of type", type(chi_y_simplified)

   # still need to convert it into a polynomial, formally
   chi_y_simplified = Poly( chi_y_simplified , y )

   # i NEED to specify 'y'; otherwise it crashed if chi_y = 0 
   # (which is the case of the elliptic curve)

   print(" ")
   # print "chi_y_simplified = ", chi_y_simplified 
   # print "of type", type(chi_y_simplified)

   print("taking all the coefficients of chi_y; they are chi^p genera (in the opposite order)..")

   coeffs_of_chi_y_simplified = chi_y_simplified.all_coeffs()

   # print  coeffs_of_chi_y_simplified 

   # all_coeffs() sorts by the top coefficient to the free term; so
   # i should reverse them

   #    [5, 0, 2, 0, 1]

   #    x^4    x^2   1

   chi_p_genera = list(reversed(coeffs_of_chi_y_simplified))

   # print "chi_p_genera = ", chi_p_genera

   # some top coeffs could be zero. fixing this.


   if len( chi_p_genera ) != n + 1:                
         print('----------------------------')
         print('length of answer should be equal to the width (Hodge square) = n + 1')
         print("SOmetimes this array is too short, ")
         print("if top coeffs of chi_y are zero")
         print("extending  it by zeroes..")
         missing_length = ( n + 1 ) - len( chi_p_genera )
         chi_p_genera = chi_p_genera + [0] * missing_length 
         # print "now chi_p_genera = ", chi_p_genera
         print('----------------------------')


   chi = chi_p_genera    # now calling it chi; it's a list [chi^0,...,chi^n]
   print("chi^p genera; i = 0,...n : ")
   print(chi)

   w = n + 1  # width of the Hodge square

   # it looks like

   #  *     1
   #    * 1
   #    1 *
   #  1     *

   # in the even w case (odd dimension of the variety)


   # and as

   # *      1
   #   *  1
   #    * 
   #   1  *
   # 1      *
          
   # in the odd w case (even dimension of the variety)

   # -----------------
   # introducing numbers for the 2nd diagonal, p + q = n
   # this diagonal has (n + 1) entries

   a = [0] * w
   # initialized the diagonal

   # initializing the Hodge square
   HS = eye(w)

   if w % 2 == 0:
       print("Hodge square is of even size")
       for p in range (0,n + 1):   # 0 - n; total w = n + 1
           a[p] = 1 - (-1)**p * chi[p]   # non-principal diagonal of the HS
           HS[p, n-p ] = a[p]
           HS[p, p ] = 1
   else:
       print("Hodge square is of odd size")
       for p in range (0,n + 1):   # 0 - n; total w = n + 1
           a[p] = (-1)**p * chi[p] - 1  # non-principal diagonal of the HS
           HS[p, n-p ] = a[p]
           HS[p, p ] = 1
       # now, this is true for all the elements besides the matrix
       # center!!
       # n is even
       p = n//2   # median!
                  # Remark: in Python 3, n/2 is float, even if n is an even integer
       a[p] = (-1)**p * chi[p] 
       HS[p, p] =  a[p]


   print("Non-principal diagonal of the Hodge square: ")
   print(a)

   # Now, when a matrix is printed, SymPy prints it top-to-bottom, so I
   # need to flip it
   HS_flipped = eye(w)
   for p in range (0,n + 1):   # 0 - n; total w = n + 1
      for q in range (0,n + 1):   # 0 - n; total w = n + 1
          HS_flipped[p,q] = HS[p, n-q ]
   

   print("Hodge square HS: ")
   pprint(HS_flipped)   # pretty printing

   # print " quitting the function"
   print("------------------------------------------")

# ---- end of the hs() ----------

# ----- calling the main function -----

# hs(n,d)

# hs(1,4)




