# Snowflake Data Engineering Pipeline with PySpark, Airflow, dbt, and Streamlit

<p align="center">
  <img src="https://img.shields.io/badge/PySpark-3.0+-blue.svg">
  <img src="https://img.shields.io/badge/Snowflake-White-blue.svg">
  <img src="https://img.shields.io/badge/Airflow-2.0+-green.svg">
  <img src="https://img.shields.io/badge/dbt-1.0+-orange.svg">
  <img src="https://img.shields.io/badge/Streamlit-1.0+-red.svg">
</p>

## Project Overview

This project is a **modern data engineering pipeline** that integrates **PySpark**, **Snowflake**, **Airflow**, **dbt**, and **Streamlit** to manage the end-to-end process of data extraction, transformation, loading (ETL), and visualization.

The pipeline extracts large datasets from Snowflake, processes them using PySpark, applies transformation and analytics using dbt, and visualizes the results with Streamlit. Airflow orchestrates the entire workflow to ensure seamless automation and scheduling.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Pipeline Workflow](#pipeline-workflow)
- [Usage](#usage)
- [Streamlit Visualization](#streamlit-visualization)

## Features

- **PySpark-based ETL**: Efficiently handle large datasets for transformation and processing.
- **Snowflake as the Data Warehouse**: Centralized storage of raw and processed data.
- **Airflow Orchestration**: Automates and schedules ETL tasks.
- **dbt for Data Transformation**: Simplifies analytics and transformation of data in Snowflake.
- **Streamlit for Visualization**: Interactive and real-time dashboards for exploring insights.
- **Scalable and Modular**: Easily extendable to accommodate additional data sources, transformations, and visualizations.

## Architecture

```mermaid
graph TD;
    A[Snowflake Warehouse] -->|Data Extraction| B[PySpark ETL];
    B -->|Transformations| C[Snowflake Analytics DB];
    C -->|dbt Models| D[dbt Transformation];
    D --> E[REPORT_SCHEMA in Snowflake];
    E --> F[Streamlit Dashboard];
    F --> G[End User Visualization];
    A --> H[Airflow Orchestration];
```

## Tech Stack

- **PySpark**: For large-scale data extraction and transformation, leveraging distributed computing to process millions of records efficiently.
- **Snowflake**: As the central data warehouse for storing raw, transformed, and analytics data.
- **Airflow**: To orchestrate and automate the entire ETL workflow, ensuring tasks are scheduled and dependencies are handled seamlessly.
- **dbt (Data Build Tool)**: To manage SQL-based data transformations and create analytics models in a modular way using version-controlled code.
- **Streamlit**: For interactive web-based visualization, allowing users to explore and analyze the data in real time through a simple and intuitive interface.


## Pipeline Workflow

The pipeline consists of several key components that work together to facilitate efficient data processing. 

1. **Data Extraction**: PySpark extracts data from multiple source tables in Snowflake. 
2. **Data Transformation**: The extracted data undergoes transformations using modular PySpark scripts, ensuring the data is clean and structured for analysis.
3. **Loading into Snowflake**: Transformed data is loaded back into Snowflake for storage and further processing.
4. **Analytics with dbt**: dbt models are used to create analytics tables and enable seamless querying of the transformed data.
5. **Orchestration**: Apache Airflow manages and schedules the entire workflow, ensuring that each step is executed in the correct sequence and monitoring for any failures.
6. **Visualization**: Finally, Streamlit provides an interactive dashboard for visualizing the data, allowing users to gain insights and make data-driven decisions.


## Usage

To interact with the ETL pipeline and visualization components of this project, use the following commands:


1. **Clone the repository**:
   ```bash
   git clone https://github.com/shahidmalik4/pyspark-snowflake-dbt-pipeline.git
   cd project_directory
   ```

2. **Set Up the Environment**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Airflow Services**:
   ```bash
   airflow scheduler &
   airflow webserver -p 8080
   ```

4. **Run dbt Transformations**:
   ```bash
   dbt run
   ```

5. **Start the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

## Streamlit Visualization

The project includes a Streamlit application for interactive data visualization. To access the visualization dashboard, follow these steps:

1. **Launch the Streamlit App**: Navigate to the project directory and start the Streamlit server.
   ```bash
   streamlit run app.py
   ```


