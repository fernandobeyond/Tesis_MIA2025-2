# SISTEMA DE DETECCIÓN DE ATAQUES DDOS BASADO EN DEEP LEARNING EN ENTORNOS DE RED

Este repositorio contiene el código y los recursos para el preprocesamiento de datos del proyecto de tesis enfocado en la detección de ataques de denegación de servicio distribuido (DDoS) utilizando técnicas de Deep Learning.

## Autores / Equipo

* **Autor(es):** `[Nombre del Autor 1]`, `[Nombre del Autor 2]`
* **Correo / GitHub:** `[correo@dominio.com / usuario-github]`

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

