from __future__ import annotations

import math


BOTH = 0
POLAR = 1
RECT = 2

class ComplexNumber:
    def __init__(self, mode, *params):
        self.mode = mode
        if mode == BOTH:
            self.r, self.theta, self.real, self.imag = params
            if self.r < 0:
                self.r = -self.r
                self.theta += 1
            self.theta = self.theta%1
        elif mode == POLAR:
            self.r, self.theta = params
            if self.r < 0:
                self.r = -self.r
                self.theta += 1
            self.theta = self.theta%1
        else:
            self.real, self.imag = params
            
    def __eq__(self, other) -> bool:
        if self.mode == BOTH or self.mode == POLAR:
            if self.r == other.r and self.theta == other.theta:
                return True
        if self.mode == BOTH or self.mode == RECT:
            if self.real == other.real and self.imag == other.imag:
                return True
        return False

    def __add__(self, other: ComplexNumber | int | float) -> ComplexNumber:
        if self.mode == POLAR:
            self.to_rect()
        if isinstance(other, ComplexNumber):
            if other.mode == POLAR:
                other.to_rect()
            real_new = self.real+other.real
            imag_new = self.imag+other.imag
        elif isinstance(other, int | float):
            real_new = self.real+other
            imag_new = self.imag
        else:
            raise NotImplementedError(f"ComplexNumber addition has not been implemented with {type(other)}")
        return ComplexNumber(RECT, real_new, imag_new)

    def __radd__(self, other: ComplexNumber | int | float) -> ComplexNumber:
        return self+other

    def __sub__(self, other: ComplexNumber | int | float) -> ComplexNumber:
        if self.mode == POLAR:
            self.to_rect()
        if isinstance(other, ComplexNumber):
            if other.mode == POLAR:
                other.to_rect()
            real_new = self.real-other.real
            imag_new = self.imag-other.imag
        elif isinstance(other, int | float):
            real_new = self.real-other
            imag_new = self.imag
        else:
            raise NotImplementedError(f"ComplexNumber subtraction has not been implemented with {type(other)}")
        return ComplexNumber(RECT, real_new, imag_new)

    def __rsub__(self, other: ComplexNumber | int | float) -> ComplexNumber:
        return -(self-other)

    def __mul__(self, other: ComplexNumber | int | float) -> ComplexNumber:
        if isinstance(other, ComplexNumber):
            if self.mode == RECT:
                self.to_polar()
            if other.mode == RECT:
                other.to_polar()
            r_new = self.r*other.r
            theta_new = self.theta+other.theta
            return ComplexNumber(POLAR, r_new, theta_new)
        elif isinstance(other, int | float):
            if self.mode == BOTH:
                r_new = self.r*other
                theta_new = self.theta
                real_new = self.real*other
                imag_new = self.imag*other
                return ComplexNumber(BOTH, r_new, theta_new, real_new, imag_new)
            elif self.mode == POLAR:
                r_new = self.r*other
                theta_new = self.theta
                return ComplexNumber(POLAR, r_new, theta_new)
            elif self.mode == RECT:
                real_new = self.real*other
                imag_new = self.imag*other
                return ComplexNumber(RECT, real_new, imag_new)
        else:
            raise NotImplementedError(f"ComplexNumber multiplication has not been implemented with {type(other)}")

    def __rmul__(self, other: ComplexNumber | int | float) -> ComplexNumber:
        return self*other

    def __truediv__(self, other: ComplexNumber | int | float) -> ComplexNumber:
        if isinstance(other, ComplexNumber):
            if self.mode == RECT:
                self.to_polar()
            if other.mode == RECT:
                other.to_polar()
            r_new = self.r/other.r
            theta_new = self.theta-other.theta
            return ComplexNumber(POLAR, r_new, theta_new)
        elif isinstance(other, int | float):
            if self.mode == BOTH:
                r_new = self.r/other
                theta_new = self.theta
                real_new = self.real/other
                imag_new = self.imag/other
                return ComplexNumber(BOTH, r_new, theta_new, real_new, imag_new)
            elif self.mode == POLAR:
                r_new = self.r/other
                theta_new = self.theta
                return ComplexNumber(POLAR, r_new, theta_new)
            elif self.mode == RECT:
                real_new = self.real/other
                imag_new = self.imag/other
                return ComplexNumber(RECT, real_new, imag_new)
        else:
            raise NotImplementedError(f"ComplexNumber division has not been implemented with {type(other)}")

    def __rtruediv__(self, other: ComplexNumber | int | float) -> ComplexNumber:
        if isinstance(other, ComplexNumber):
            if self.mode == RECT:
                self.to_polar()
            if other.mode == RECT:
                other.to_polar()
            r_new = other.r/self.r
            theta_new = other.theta-self.theta
            return ComplexNumber(POLAR, r_new, theta_new)
        elif isinstance(other, int | float):
            if self.mode == BOTH:
                r_new = other/self.r
                theta_new = -self.theta
                real_new = other/self.real
                imag_new = other/self.imag
                return ComplexNumber(BOTH, r_new, theta_new, real_new, imag_new)
            elif self.mode == POLAR:
                r_new = other/self.r
                theta_new = -self.theta
                return ComplexNumber(POLAR, r_new, theta_new)
            elif self.mode == RECT:
                real_new = other/self.real
                imag_new = other/self.imag
                return ComplexNumber(RECT, real_new, imag_new)
        else:
            raise NotImplementedError(f"ComplexNumber division has not been implemented with {type(other)}")
        
    def __neg__(self) -> ComplexNumber:
        if self.mode == BOTH:
            return ComplexNumber(BOTH, self.r, self.theta+1, -self.real, -self.imag)
        elif self.mode == POLAR:
            return ComplexNumber(POLAR, self.r, self.theta+1)
        elif self.mode == RECT:
            return ComplexNumber(RECT, -self.real, -self.imag)

    def __pos__(self) -> ComplexNumber:
        if self.mode == BOTH:
            return ComplexNumber(BOTH, self.r, self.theta, self.real, self.imag)
        elif self.mode == POLAR:
            return ComplexNumber(POLAR, self.r, self.theta)
        elif self.mode == RECT:
            return ComplexNumber(RECT, self.real, self.imag)

    def __abs__(self) -> float:
        if self.mode == BOTH or self.mode == POLAR:
            return self.r
        elif self.mode == RECT:
            return math.sqrt(self.real**2 + self.imag**2)

    def __str__(self):
        if self.mode == BOTH or self.mode == RECT:
            return f"{self.real}+j{self.imag}"
        elif self.mode == POLAR:
            return f"{self.r}*exp(i*tau*{self.theta})"
        else:
            return super().__repr__()

    def __repr__(self):
        if self.mode == BOTH or self.mode == RECT:
            return f"{self.real}+j{self.imag}"
        elif self.mode == POLAR:
            return f"{self.r}*exp(i*tau*{self.theta})"
        else:
            return super().__repr__()

    def to_rect(self) -> ComplexNumber:
        self.real = self.r*math.cos(math.tau*self.theta)
        self.imag = self.r*math.sin(math.tau*self.theta)
        self.mode = BOTH
        return self

    def to_polar(self) -> ComplexNumber:
        self.r = math.sqrt(self.real**2 + self.imag**2)
        self.theta = (math.atan2(self.imag, self.real)/math.tau)%1
        self.mode = BOTH
        return self

    def as_rect(self) -> ComplexNumber:
        if self.mode == POLAR:
            new_real = self.r*math.cos(math.tau*self.theta)
            new_imag = self.r*math.sin(math.tau*self.theta)
            return ComplexNumber(BOTH, self.r, self.theta, new_real, new_imag)
        return self

    def as_polar(self) -> ComplexNumber:
        if self.mode == RECT:
            new_r = math.sqrt(self.real**2 + self.imag**2)
            new_theta = math.atan2(self.imag, self.real)/math.tau
            return ComplexNumber(BOTH, new_r, new_theta, self.real, self.imag)
        return self