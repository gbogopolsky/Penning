#include<iostream>
#include<stdlib.h>
#include<math.h>
#include<fstream>
#include<sstream>
#include"rk4.hpp"
using namespace std;

double e = 1., m = 1., wz = 1., b0 = 1.;
double wc = 1.5; //fréquence cyclotron légèrement modifiée par le champs électrique

double K = wz*wz/2, M = wc;


void systeme(double* q, double t, double* qp, int n) { //système d'équation de degré 1 à résoudre
  qp[0] = q[3];
  qp[1] = q[4];
  qp[2] = q[5];
  qp[3] = K * q[0] - M * q[4];
  qp[4] = K * q[1] + M * q[3];
  qp[5] = - 2 * K * q[2];
}

int main() {
  int i, n = 3, Nt = 20000; //n = dim = 3
  double t = 0, tfin = 50, dt = (tfin - t) / (Nt - 1);
  double* q  = (double*)malloc(2 * n * sizeof(double)); //coordonnées et vitesses canoniques
  fstream fich("2penning.res", ios::out);

  //Conditions initiales
  q[0] = 0.1; q[1] = 0.1; q[2] = 0.1;  //position initiale
  q[3] = 1.; q[4] = 1.; q[5] = 1.;     //vitesse initiale

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
