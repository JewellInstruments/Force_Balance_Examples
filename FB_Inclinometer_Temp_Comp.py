import math


def output_temp_compensated(
    V: float,
    T: float,
    SFTS: float,
    K_0: float,
    K_1: float,
    ZTS: float,
    T_0: float,
    phi: float,
) -> float:
    """compute the angle from a given voltage and temperature for an inclinometer.

    Args:
        V (float): voltage output from the inclinometer
        T (float): current temperature of the inclinometer
        SFTS (float): scale factor temperature sensitivity (1/C)
        K_0 (float): zero tilt (V)
        K_1 (float): scale factor (V/g)
        ZTS (float): zero tilt temperature sensitivity (V/C)
        T_0 (float): room temperature measurement from the ATP report.
        phi (float): Output axis misalignment (degrees)

    Returns:
        float: output angle in degrees.
    """

    a = V - (K_0 + (T - T_0) * ZTS)
    b = K_1 * ((T - T_0) * SFTS + 1)

    return math.degrees(math.asin(a / b)) - phi


def main():
    V = 2.0214  # Volts -> measured
    T = 34.5  # C -> measured

    SFTS_hot = 0.000007  # 1/C -> From ATP report
    SFTS_cold = -0.000095  # 1/C -> From ATP report
    K_0 = -0.0189  # V -> From ATP report
    K_1 = 95.5734  # V/g -> From ATP report
    ZTS_hot = 0.000905  # V/C -> From ATP report
    ZTS_cold = -0.000285  # V/C -> From ATP report
    T_0 = 21.2  # C -> From ATP report
    Moa = 0.009  # deg -> From ATP report

    if T > T_0:
        SFTS = SFTS_hot
        ZTS = ZTS_hot
    else:
        SFTS = SFTS_cold
        ZTS = ZTS_cold

    angle = output_temp_compensated(V, T, SFTS, K_0, K_1, ZTS, T_0, Moa)
    print(f"Angle (deg): {angle: 0.5f}")
    return


if __name__ == "__main__":
    main()
