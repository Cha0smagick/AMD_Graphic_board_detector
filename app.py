import wmi

def obtener_info_gpu():
    # Conectar al WMI
    c = wmi.WMI()

    # Obtener información de la GPU
    gpus = c.Win32_VideoController()

    if not gpus:
        print("No se encontraron tarjetas gráficas en el sistema.")
        return

    for gpu in gpus:
        print(f"Nombre: {gpu.Name}")
        print(f"Descripción: {gpu.Description}")
        print(f"Procesador Gráfico: {gpu.VideoProcessor}")
        print(f"RAM Adapter: {gpu.AdapterRAM} bytes")
        print(f"Driver Version: {gpu.DriverVersion}")
        print(f"Resolución Horizontal: {gpu.CurrentHorizontalResolution}")
        print(f"Resolución Vertical: {gpu.CurrentVerticalResolution}")
        print("-" * 40)

if __name__ == "__main__":
    obtener_info_gpu()
