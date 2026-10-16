# ==========================================================
# SIMULADOR DE ITERACIÓN DCU - CICLO PHVA
# Asignatura: Interacción Humano-Computador (UNEMI)
# ==========================================================

def simulador_dcu():
    print("==========================================================")
    print("      INICIANDO PROCESO DE DISEÑO CENTRADO EN EL USUARIO   ")
    print("                  (CICLO DE MEJORA PHVA)                  ")
    print("==========================================================")
    
    satisfactorio = False
    iteracion = 1

    while not satisfactorio:
        print(f"\n--- [ITERACIÓN {iteracion}] ---")
        
        # 1. PLANEAR (P)
        print("[P - PLANEAR]: Investigando contexto de uso (CECU) y especificando requisitos de usuario (ERU)...")
        
        # 2. HACER (H)
        print("[H - HACER]: Produciendo soluciones de diseño (PSD) y elaborando prototipos de interacción...")
        
        # 3. VERIFICAR (V)
        evaluacion = input("[V - VERIFICAR]: ¿Satisface el sistema los requerimientos del usuario? (s/n): ")
        
        # 4. ACTUAR (A)
        if evaluacion.lower().strip() == 's':
            print("\n[A - ACTUAR]: ¡Evaluación Exitosa! El diseño satisface las especificaciones de usabilidad.")
            print(">>> Producto aprobado. Procediendo al desarrollo final. <<<")
            satisfactorio = True
        elif evaluacion.lower().strip() == 'n':
            print("\n[A - ACTUAR]: Criterios de usabilidad no alcanzados.")
            print(">>> Reingresando al ciclo iterativo para redefinir requerimientos y rediseñar...")
            iteracion += 1
        else:
            print("[!] Respuesta no válida. Por favor, ingresa 's' para SÍ o 'n' para NO.")

if __name__ == "__main__":
    simulador_dcu()