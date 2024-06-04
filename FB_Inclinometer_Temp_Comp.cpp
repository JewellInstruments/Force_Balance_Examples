#include<math.h>
#include<cstdio>

double output_temp_compensated(
    double V, double T, double SFTS, double K_0, double K_1, double ZTS, double T_0, double phi){
    double a, b; 
    a = V - (K_0 + (T - T_0) * ZTS);
    b = K_1 * ((T - T_0) * SFTS + 1);

    return 180./M_PI*asin(a / b) - phi;
}
    


int main(){
    double V = 2.0214;  // Volts -> measured
    double T = 34.5;  // C -> measured

    double SFTS_hot = 0.000007;  // 1/C -> From ATP report
    double SFTS_cold = -0.000095;  // 1/C -> From ATP report
    double K_0 = -0.0189;  // V -> From ATP report
    double K_1 = 95.5734;  // V/g -> From ATP report
    double ZTS_hot = 0.000905;  // V/C -> From ATP report
    double ZTS_cold = -0.000285;  // V/C -> From ATP report
    double T_0 = 21.2;  // C -> From ATP report
    double Moa = 0.009;  // deg -> From ATP report

    double SFTS, ZTS, angle;

    if (T > T_0){
        SFTS = SFTS_hot;
        ZTS = ZTS_hot;
    }
    else{
        SFTS = SFTS_cold;
        ZTS = ZTS_cold;
    }
    angle = output_temp_compensated(V, T, SFTS, K_0, K_1, ZTS, T_0, Moa);
    printf("Angle (deg): %f", angle);
    // print(f"Angle (deg): {angle: 0.5f}")
    return 0;
}