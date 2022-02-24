# Complex Math

Complex math library that supports basic arithmetic and a few other operations.

Numbers are are stored in polar or rectangular form (or both) and are lazily updated when needed. For example, a number will be stored in polar form after a multiplication by another complex number and then will stay in polar form until its next addition, at which point its real and imaginary components will finally be updated. The mode attribute keeps track of whether the number is in polar or rectangular mode (or both, after an update). 

Each number object contains ((self.r, self.theta), (self.real, self.imag)). (Though due to lazy updating, both pairs will not always be up-to-date at the same time.)

Theta, the polar argument, is scaled by a factor of 1/tau and then only the fractional part is taken (so `0 <= theta < 1`; this will hopefully be of use in case of future conversion to fixed point).

Thus, `z = real+j*imag = r*exp(j*tau*theta)`.

---

Inspired by https://math.stackexchange.com/questions/4172817/complex-floating-point-types

Adapted from tests by Tim Peters on python-ideas mailing list https://mail.python.org/archives/list/python-ideas@python.org/message/3IY3NTJRAMSQZYTCVQABTYPM2TGS3UVN/
