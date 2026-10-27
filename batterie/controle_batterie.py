import sys
import time
from batterie import DFRobot_INA219

# ---------------------------------
# CONFIGURATION
# ---------------------------------
ina219_reading_mA = 1000
ext_meter_reading_mA = 1000

V_min = 6.0           # Tension minimale batterie 2S Li-ion

# ---------------------------------
# INITIALISATION DU CAPTEUR
# ---------------------------------
ina = DFRobot_INA219.INA219(1, DFRobot_INA219.INA219.INA219_I2C_ADDRESS4)
while not ina.begin():
    print("Échec de l'initialisation INA219, réessai dans 2s...")
    time.sleep(2)
ina.linear_cal(ina219_reading_mA, ext_meter_reading_mA)

# ---------------------------------
# FONCTIONS UTILES
# ---------------------------------
def voltage_to_soc(V):
    """Estime le SoC à partir de la tension pour 2 piles Li-ion 18650 en série"""
    voltage_points = [
        6.0, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8,
        6.9, 7.0, 7.1, 7.2, 7.25, 7.3, 8.4
    ]
    soc_points = [
        0, 7, 14, 21, 28, 35, 42, 49,
        56, 63, 70, 77, 84, 91, 100
    ]

    if V <= voltage_points[0]:
        return 0
    elif V >= voltage_points[-1]:
        return 100

    for i in range(1, len(voltage_points)):
        if V < voltage_points[i]:
            V0, V1 = voltage_points[i-1], voltage_points[i]
            SoC0, SoC1 = soc_points[i-1], soc_points[i]
            return SoC0 + (V - V0) * (SoC1 - SoC0) / (V1 - V0)

# Variables globales pour Coulomb counting
V_initial = ina.get_bus_voltage_V()
SoC = voltage_to_soc(V_initial)

def update_soc():
    """Met à jour le SoC via evaluation par voltage"""
    global SoC
    V = ina.get_bus_voltage_V()
    SoC = voltage_to_soc(V)   
    return round(SoC, 1)

def update_conso():   # renvoie la puissance consommée en mW
    power = ina.get_power_mW() 
    return power
