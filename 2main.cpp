#include<iostream>
#include<stdlib.h>
#include<math.h>
#include<fstream>
#include<sstream>
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

void rk4(void(*systeme)(double*,double,double*,int), double* q, double t, double dt, int n) {
  static int first_ite = 0;  // first_ite initialisée à 0 uniquement lors de la 1ere exécution
                          // first_ite conserve sa valeur entre 2 appels de la fonction
  static double** p = (double**)malloc(5 * sizeof(double*)); // p initialisé idem static variable

  int i, j;
  double coeff;
  // seulement exécuté à la 1ere itération de rk4()
  if (first_ite == 0) {
  first_ite = 1;
  for (i = 0; i < 5; i++) {
      p[i] = (double*)malloc(n * sizeof(double)); // initialisation uniquement au premier appel
    }
  }

  // 4 vecteurs p[i] à calculer et p[0] = intermédiaire de calcul
  systeme(q, t, p[1], n);                      // p[1] = F(q,t)
  for (i = 2; i < 5; i++) {
      if (i != 4) coeff = 1./2;
      else coeff = 1.;
      for (j = 0; j < n; j++)
          p[0][j] = q[j] + coeff * dt * p[i-1][j];

      systeme(p[0], t + coeff * dt, p[i], n); /* p[2]  = F(q + dt/2 * p[1], t + dt/2)
                                                 p[3]  = F(q + dt/2 * p[2], t + dt/2)
                                                 p[4]  = F(q + dt * p[3], t + dt) */
  }

  for (i = 0; i < n; i++) {
      q[i] = q[i] + dt * (p[1][i] + 2 * p[2][i] + 2 * p[3][i] + p[4][i]) / 6.;
          // q(t+dt) = q(t) + dt/6.*(p[0]+2*p[1]+2*p[2]+p[3])
  }
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
