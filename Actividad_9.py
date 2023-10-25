from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
       
        direcciones_a_grados = {
            "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5,
            "E": 90, "ESE": 112.5, "SE": 135, "SSE": 157.5,
            "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
            "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
        }

        total_temperatura = 0
        total_humedad = 0
        total_presion = 0
        total_velocidad_viento = 0
        direccion_viento_grados = []

        with open(self.nombre_archivo, 'r') as archivo:
            for i in archivo:
                if "Temperatura:" in i:
                    total_temperatura += float(i.split(":")[1])
                elif "Humedad:" in i:
                    total_humedad += float(i.split(":")[1])
                elif "Presión:" in i:
                    total_presion += float(i.split(":")[1])
                elif "Viento:" in i:
                    viento_info = i.split(":")[1].split(",")
                    velocidad_viento = float(viento_info[0])
                    direccion_viento = viento_info[1].strip()
                    total_velocidad_viento += velocidad_viento
                    direccion_viento_grados.append(direcciones_a_grados[direccion_viento])

        promedio_temperatura = total_temperatura / len(direccion_viento_grados)
        promedio_humedad = total_humedad / len(direccion_viento_grados)
        promedio_presion = total_presion / len(direccion_viento_grados)
        promedio_velocidad_viento = total_velocidad_viento / len(direccion_viento_grados)

        
        promedio_direccion_viento_grados = sum(direccion_viento_grados) / len(direccion_viento_grados)
        direccion_viento_predominante = min(direcciones_a_grados, key=lambda x: abs(direcciones_a_grados[x] - promedio_direccion_viento_grados))

        return promedio_temperatura, promedio_humedad, promedio_presion, promedio_velocidad_viento, direccion_viento_predominante

