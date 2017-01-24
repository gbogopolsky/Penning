#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<stdarg.h>
#include<cmath>
#include<complex>
#include<vector>
#include<string>
#include<iostream>
#include<fstream>
#include<iomanip>
#include<sstream>
using namespace std;

void ini_D_1(double *x, int ni,...) {
  int i;
  va_list ap;
  va_start(ap,ni);
  for (i = 0; i < ni; i++) x[i]=va_arg(ap,double);
  va_end(ap);
}

void ini_D_2(double **x, int ni, int nj,...) {
  int i, j;
  va_list ap;
  va_start(ap, nj);
  for (i = 0; i < ni; i++) for (j = 0; j < nj; j++) x[i][j] = va_arg(ap,double);
  va_end(ap);
}

void f_D_1(
		     double *mat,      //  Pointeur sur le vecteur
		     int ligne         //  Nombre d'elements
		     ){
  free(mat);
  return;
}

void f_D_2(
		       double **mat,      //  Pointeur sur la matrice
		       int ligne,         //  Nombre de lignes
		       int ncolonne       //  Nombre de colonnes
		       ){
  int i;
  for(i=0;i<ligne;i++)
    free(mat[i]);
  free(mat);
  return;
}

void rk4(void(*systeme)(double*,double,double*,int), double *q,
double t,double dt, int n) {
  int i, k, p, PM = 4;
  static const double c2 = 1./2, c3 = 1./3, c6 = 1./6;

  //Allocations et initialisations

  double** a = (double**)malloc(PM * sizeof(double*));
  for (i = 0; i < PM; i++)
    a[i] = (double*)malloc(PM * sizeof(double));
  ini_D_2(a,PM,PM,c2,0.,0.,0.,0.,c2,0.,0.,0.,0.,1.,0.,c6,c3,c3,c6);

  double* b = (double*)malloc(PM * sizeof(double));
  ini_D_1(b,PM,0.,c2,c2,1.);

  double** y = (double**)malloc((PM+1) * sizeof(double*));
  for (i = 0; i < PM+1; i++)
    y[i] = (double*)malloc(n * sizeof(double));

  double** z = (double**)malloc(PM * sizeof(double*));
  for (i = 0; i < PM; i++)
    z[i] = (double*)malloc(n * sizeof(double));

  //Calcul

  for (i = 0; i < n; i++) y[0][i] = q[i];
  for (p = 1; p <= PM; p++) {
    systeme(y[p-1], t + b[p-1] * dt, z[p-1], n);
    for (i = 0; i < n; i++) y[p][i] = q[i];
    for (k = 0; k < p; k++) {
      for (i = 0; i < n; i++) y[p][i] = y[p][i] + dt * a[p-1][k] * z[k][i];
    }
  }
  for (i = 0; i < n; i++) q[i] = y[PM][i];

  //Désallocations
  f_D_2(a,PM,PM); f_D_1(b,PM); f_D_2(y,PM+1,n); f_D_2(z,PM,n);
}
