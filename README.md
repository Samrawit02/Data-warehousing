# Data-warehousing

A data pipeline for Extracting, Loading and Transforming traffic data
<p align="center">
  <h3 align="center">Data Engineering TrafficDrone Data</h3>

  <p align="center">
    A ELT pipeline using mysql, dbt, Apache Airflow, and Redash.
    <br />  
   
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project



A  ELT pipeline with MySql for data storage, Airflow for automation and orchestration, DBT for data transformation, and a Redash dashboard connected to the data warehouse.

### Built With

Tech Stack used in this project

-   [MySQL](https://dev.mysql.com/doc/)
-   [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/)
-   [dbt](https://docs.getdbt.com/)
-   [Redash](https://redash.io/help/)


### Prerequisites

Make sure you have docker installed on local machine.

-   Docker
-   Docker Compose

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/Samrawit02/Data-warehousing.git
    ```

2. Run
    ```sh
     docker-compose up
    ```
3. Open Airflow web browser
    ```JS
    Navigate to `http://localhost:8081/` on the browser


<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

-   [10 Academy](https://www.10academy.org/)
