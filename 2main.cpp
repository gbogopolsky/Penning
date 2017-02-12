#include<iostream>
#include<stdlib.h>
#include<math.h>
#include<fstream>
#include<sstream>
#include"rk4.hpp"
using namespace std;

double e = 1.602e-19, m = 9.109e-31, wz = 2*M_PI*60.e6, b0 = 1.;
double wc = 2*M_PI*51.e9; //fréquence cyclotron légèrement modifiée par le champs électrique

double K = wz*wz/2, M = wc;


void systeme(double* q, double t, double* qp, int n) {
  qp[0] = q[3];
  qp[1] = q[4];
  qp[2] = q[5];
  qp[3] = K * q[0] - M * q[4];
  qp[4] = K * q[1] + M * q[3];
  qp[5] = - 2 * K * q[2];
}

int main() {
  int i, n = 3, Nt = 200000; //n = dim = 3
  double t = 0, tfin = 1.e-9, dt = (tfin - t) / (Nt - 1);
  double* q  = (double*)malloc(2 * n * sizeof(double)); //coordonnées et vitesses canoniques
  fstream fich("2penning.res", ios::out);

  //Conditions initiales
  q[0] = 1e-4; q[1] = 1e-4; q[2] = 1e-4; //position initiale
  q[3] = 2e4; q[4] = 2e4; q[5] = 2e4; //vitesse initiale

  //Résolution
  for (i = 0; i < Nt; i++) {
    fich << t << " " << q[0] << " " << q[1] << " " << q[2] << endl;
    rk4(systeme, q, t, dt, 2*n);
    t += dt;
  }
  fich.close();

  free(q);
  return 0;
}
