# fraud-detection-in-financial-transactions

 ## Project Overview
 
 The company "FinTech Innovations" is facing a growing challenge of fraudulent transactions that impact customer trust and result in financial losses. To address this issue, a fraud detection system based on the analysis of transactional data, customer data, and external data is being considered. The goal is to detect suspicious activities in real-time and minimize false alerts.

## Table of Contents
1. [API Development](#api-development)
2. [Data Collection and Integration](#data-collection-and-integration)
3. [Data Storage and Management with Hive](#data-storage-and-management-with-hive)
4. [Rule-Based Fraud Detection System](#rule-based-fraud-detection-system)
5. [Deployment](#deployment)

## API Development
### Transaction Data API
- Endpoint: `/api/transactions`
- Provides access to transaction data, including transaction ID, date and time, amount, currency, merchant details, customer ID, and transaction type.

### Customer Data API
- Endpoint: `/api/customers`
- Provides access to customer data, including customer ID, account history, demographic information, and behavioral patterns.

### External Data API
- Endpoint: `/api/externalData`
- Retrieves external data, such as blacklist information, credit scores, and fraud reports.

## Data Collection and Integration
- Utilize the developed APIs to collect transaction, customer, and external data.
    
   before doing any changes on data lets test the connection with hive :

   starting by : `pip install pyhive`

    in case of getting the error of thrift you need to : `pip install thrift`

   ![Alt text](image.png)

- Ensure collected data is clean, relevant, and in a format suitable for analysis.

## Data Storage and Management with Hive
- Design and implement Hive tables to store transaction, customer, and external data.
- Apply partitioning or bucketing strategies for efficient data management.

## Rule-Based Fraud Detection System
- Use HiveQL to write queries that flag transactions based on identified fraud indicators.
- Examples of rules include detecting unusually high transaction amounts, a high frequency of transactions in a short period, transactions from unusual locations, and transactions with customers on a blacklist.

## Deployment
- Set up an Airflow DAG (Directed Acyclic Graph) to orchestrate the data collection, processing, and alerting process.
- Integrate CI/CD with GitHub Actions for automatic and secure script and DAG updates.

## Getting Started
1. Clone the repository: `git clone https://github.com/yourusername/fraud-detection.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure API endpoints and other settings in the configuration file: `config.yaml`
4. Run the data collection and processing scripts: `python collect_and_process.py`
5. Monitor alerts and results through the Airflow UI: `http://airflow-server:8080`

## Contributing
We welcome contributions! If you find any issues or have suggestions, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
