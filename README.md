# SISTEMA DE DETECCIÓN DE ATAQUES DDOS BASADO EN DEEP LEARNING EN ENTORNOS DE RED

Este repositorio contiene el código y los recursos para el preprocesamiento de datos del proyecto de tesis enfocado en la detección de ataques de denegación de servicio distribuido (DDoS) utilizando técnicas de Deep Learning.

## Autores / Equipo

* **Autor(es):** `FLORES QUILICHE, Fernando`, `RODRIGUEZ MALMA, Josef Renato`
* **Correo:** `fernando.flores.q@uni.pe - josef.rodriguez.m@uni.pe`

## Dataset

El conjunto de datos utilizado para este proyecto contiene un registro de flujos de red, con características extraídas para diferenciar entre tráfico benigno y diversos tipos de ataques DDoS.

* **Fuente:** El dataset original, `dataset_ddos.csv`, se encuentra alojado en una ruta privada de Google Drive. Se recomienda al autor añadir el enlace a la fuente pública si está disponible (ej. Canadian Institute for Cybersecurity - CIC-DDoS2019).
* **Descripción:**
    * El dataset original consta de **2,670,479 registros** y **20 variables**.
    * Las variables principales incluyen características de flujo de red como `Flow Duration`, `Total Fwd Packets`, `Fwd Packet Length Max`, `Flow Bytes/s`, y la etiqueta de clasificación `Attack_Label`.
    * La variable objetivo `Attack_Label` fue transformada a una clasificación binaria (0 para `BENIGN` y 1 para `ATTACK`).
* **Versión utilizada:**
    * **Fecha:** `[Indicar la fecha de descarga o versión del dataset]`
    * **Hash:** `[Indicar el hash SHA256 del archivo para garantizar la reproducibilidad]`

## Requisitos

Para ejecutar el notebook de preprocesamiento, es necesario contar con las siguientes librerías de Python. Puede instalarlas utilizando `pip`:

```bash
pip install -r requirements.txt
```
El contenido del archivo requirements.txt es el siguiente:
```bash
pandas
numpy
matplotlib
seaborn
scikit-learn
imblearn
```

## Estructura del Repositorio
El proyecto se organiza de la siguiente manera para mantener la claridad y facilitar la reproducibilidad:

```bash
├── data/
│   ├── raw/
│   │   └── dataset_ddos.csv        # Dataset original sin procesar
│   └── processed/
│       └── ddos_balanceado.csv     # Dataset balanceado y listo para el modelo
│
├── notebooks/
│   └── 01_EDA_y_Preprocesamiento.ipynb  # Notebook con el análisis y balanceo
│
├── src/
│   └── ...                         # Scripts de Python para funciones auxiliares (si aplica)
│
├── README.md                       # Este archivo
└── requirements.txt                # Dependencias del proyecto
```

## Cómo correr el pipeline
El notebook DDos_attack.ipynb realiza el primer paso fundamental del proyecto. Para reproducir el experimento de preprocesamiento, siga estos pasos:

1. Clonar el repositorio:

```bash
git clone [URL-del-repositorio]
cd [nombre-del-repositorio]
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```
3. Ubicar el dataset: Coloque el archivo dataset_ddos.csv en la carpeta data/raw/.

4. Ejecutar el notebook: Abra y ejecute todas las celdas del notebook notebooks/01_EDA_y_Preprocesamiento.ipynb en un entorno como Jupyter Lab o Google Colab.

## Resultados Esperados
Al ejecutar completamente el notebook de preprocesamiento, el pipeline generará el siguiente resultado:
- Un archivo llamado ddos_balanceado.csv en la carpeta data/processed/.
- Este archivo contendrá un subconjunto de los datos originales, con las clases benigna y ataque perfectamente balanceadas (50%-50%) mediante la técnica de submuestreo (Undersampling). El dataset resultante tiene 1,116,322 registros.