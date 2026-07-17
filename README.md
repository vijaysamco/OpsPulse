# 🌦️ OpsPulse – Weather Data Pipeline

## 📌 Project Overview

OpsPulse is a simple ETL (Extract, Transform, Load) project built using Python. It fetches live weather data from the Open-Meteo public API, stores the raw response in JSON format, transforms the data into a structured CSV file using Pandas, and validates the output with Pytest.

This project demonstrates API integration, data transformation, file handling, and automated testing.

---

## 📂 Project Structure

```
OpsPulse/
│── data/
│   ├── raw_weather.json
│   ├── weather.csv
│
│── src/
│   ├── fetch_weather.py
│   ├── transform.py
│
│── tests/
│   ├── test_transform.py
│
│── requirements.txt
│── README.md
```

---

## 🚀 Features

- Fetches live weather data from a public API.
- Stores raw API response in JSON format.
- Converts JSON data into a CSV file using Pandas.
- Includes automated tests using Pytest.
- Demonstrates a simple ETL pipeline.

---

## 🛠 Technologies Used

- Python 3.x
- Requests
- Pandas
- Pytest

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/OpsPulse.git
cd OpsPulse
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1: Fetch Weather Data

```bash
python src/fetch_weather.py
```

This creates:

```
data/raw_weather.json
```

### Step 2: Transform the Data

```bash
python src/transform.py
```

This creates:

```
data/weather.csv
```

---

## ✅ Running Tests

Run the following command:

```bash
pytest
```

Expected output:

```
============================= test session starts =============================
...
3 passed in 0.05s
```

---

## 📊 Sample Output

| Time | Temperature | Humidity | WindSpeed |
|------|-------------|----------|-----------|
| 2026-07-17T10:00 | 31.2 | 74 | 12.5 |

---

## 📁 Output Files

### Raw Data

```
data/raw_weather.json
```

Contains the complete API response.

### Processed Data

```
data/weather.csv
```

Contains the cleaned weather information in tabular format.

---

## 🧪 Test Cases

The project includes three automated tests:

- Verify required columns exist.
- Ensure temperature values are not null.
- Check humidity values are between 0 and 100.

---

## 🌐 Data Source

Open-Meteo Weather API

https://open-meteo.com/

API Endpoint:

https://api.open-meteo.com/v1/forecast

---

## 📌 Future Improvements

- Support multiple cities.
- Store processed data in SQLite or PostgreSQL.
- Schedule automatic data collection.
- Generate weather trend visualizations.
- Add logging and exception handling.

---

## 👤 Author

Vijay Kumar Subramanian

Mini Project – OpsPulse

Python | Pandas | API Integration | Pytest
