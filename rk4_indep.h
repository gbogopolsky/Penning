void ini_D_1(double *x, int ni,...);
void ini_D_2(double **x, int ni,int nj,...);
void f_D_1(double* mat, int ligne);
void f_D_2(double** mat, int ligne, int ncolonne);

void rk4(void(*systeme)(double*,double,double*,int), double *q,
double t, double dt, int n);
