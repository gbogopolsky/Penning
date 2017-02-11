#ifndef RK4_HPP
#define RK4_HPP

void rk4(void(*systeme)(double*,double,double*,int), double* q, double t, double dt, int n);

#endif
