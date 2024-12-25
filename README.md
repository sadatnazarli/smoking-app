# SmokeX Calculator

A modern, responsive web application that calculates the financial and health impact of smoking. SmokeX estimates monthly costs, life expectancy reduction, and provides investment comparisons to demonstrate potential savings. The application supports multiple languages including English, Turkish, and Azerbaijani.

## Features

### Financial Analysis
- Calculate monthly and yearly smoking expenses based on daily consumption
- Support for multiple currencies (USD, TL, and AZN)
- Project potential savings through investment alternatives

### Health Impact Assessment
- Estimate monthly life expectancy reduction in days
- Predict approximate death age based on average life expectancy
- Visualize long-term health impacts

### User Experience
- Interactive line charts showing costs and investment projections
- Fully responsive design optimized for all devices
- Modern black and red theme for enhanced visibility
- Complete localization in English, Turkish, and Azerbaijani
- Comprehensive FAQ section with interactive accordion design

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Setup

1. Clone the repository
```bash
git clone https://github.com/sadatnazarli/smoking-app.git
cd smoking-app
```

2. Create and activate virtual environment
```bash
# Unix/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Launch application
```bash
flask run
```

Access the application at `http://127.0.0.1:5000`

## Calculation Methodology

### Life Expectancy Impact

Each cigarette reduces life expectancy by approximately 11 minutes according to scientific estimates. For a standard pack of 20 cigarettes:

```python
minutes_per_pack = 20 cigarettes × 11 minutes = 220 minutes
monthly_life_lost = (packs_per_day × 30 × 220) / (24 × 60) # Converted to days
```

### Financial Calculations

Monthly and annual cost projections:
```python
monthly_cost = packs_per_day × 30 × cost_per_pack
yearly_cost = monthly_cost × 12
```

### Investment Projection

The compound interest formula used for investment calculations:
```python
future_value = monthly_contribution × ((1 + r)^n - 1) / r
# where:
# r = monthly interest rate (annual_rate ÷ 12)
# n = number of months
```

## Project Structure

```
smoking-app/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── img/
│   │   ├── marlbro.jpg
│   │   └── mb-new.png
│   └── js/
├── templates/
│   ├── faq.html
│   ├── index.html
│   ├── login.html
│   └── projection.html
├── app.py
├── README.md
└── requirements.txt
```

## Technology Stack

### Backend
- Flask (Python web framework)
- Flask-Babel (Internationalization)
- SQLAlchemy (ORM)

### Frontend
- HTML5 & CSS3
- Bootstrap 5
- Chart.js
- JavaScript

## Localization

Currently supported languages:
- English (default)
- Turkish
- Azerbaijani

Language preferences can be modified through the UI's language selector.

## License

Released under the MIT License. See [LICENSE](LICENSE) for details.

## Author

Created by Sadat Nazarli
- GitHub: [@sadatnazarli](https://github.com/sadatnazarli)

---

**Note:** For bug reports, feature requests, or contributions, please open an issue or submit a pull request on GitHub.