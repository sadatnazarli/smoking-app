Absolutely, here's the full markdown for the SmokeX Calculator README file:

```markdown
# SmokeX Calculator

SmokeX is a modern, responsive web application that calculates the **financial** and **health impact** of smoking. The application estimates monthly costs, life expectancy reduction, and provides a comparison of how much you could save if you invested the money instead of smoking. The app supports **multiple languages**: English, Turkish, and Azerbaijani.

---

##  Features

**Smoking Cost Calculator**

* Calculates monthly and yearly smoking expenses based on daily consumption and pack cost.
* Supports multiple currencies: USD, TL, and AZN.

**Life Expectancy Reduction**

* Estimates the monthly life lost in days due to smoking.
* Predicts the approximate death age based on an average life expectancy of 75 years.

**Investment Projection**

* Displays potential savings if the money spent on smoking were invested with a compound annual return.

**Chart Visualization**

* Interactive line charts to display smoking costs and potential investment growth over time.

**Multi-Language Support**

* Fully localized interface with translations in English, Turkish, and Azerbaijani.

**FAQ Page**

* Detailed explanations of how calculations are performed.
* Interactive accordion design for easy navigation.

**Responsive Design**

* Fully responsive UI optimized for mobile, tablet, and desktop devices.
* Black and red theme for a sleek and modern look.

---

##  How to Run Locally

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/smokex-calculator.git](https://github.com/your-username/smokex-calculator.git)
cd smokex-calculator
```

### 2. Set Up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
flask run
```

The app will be available at http://127.0.0.1:5000.

---

##  How Calculations Work

**1. Monthly Life Lost**

Each cigarette reduces life expectancy by approximately 11 minutes (scientific estimate). A pack of 20 cigarettes reduces life expectancy by ~220 minutes.

**Formula:**

```sql
Monthly Life Lost = Packs per Day × 30 × 220 minutes
Converted to days: Minutes / (24 × 60)
```

**2. Cost**

**Monthly Cost:**

```sql
Monthly Cost = Packs per Day × 30 × Cost per Pack
```

**Yearly Cost:**

```java
Yearly Cost = Monthly Cost × 12
```

**3. Investment Projection**

A simple compound interest formula is used for investment projection:

```css
Future Value = Monthly Contribution × [(1 + r)^n - 1] / r
```

Where:

* r = Monthly interest rate (annual rate ÷ 12)
* n = Number of months

---

##  Multi-Language Support

The application supports the following languages:

* English (default)
* Turkish
* Azerbaijani

You can switch the language using the dropdown menu in the header.

---

##  Project Structure

```csharp
smokex-calculator/
│
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles
│   ├── img/
│   │   └── mb-new.png    # SmokeX logo
│   └── js/
│       └── script.js     # Optional JS for interactivity
├── templates/
│   ├── index.html        # Main calculator page
│   ├── faq.html          # FAQ page
│   └── base.html         # Reusable layout template
└── README.md             # Project documentation
```

---

##  Technologies Used

* Backend: Flask (Python)
* Frontend: HTML5, CSS3 (Bootstrap 5), JavaScript (Chart.js)
* Localization: Flask-Babel for multi-language support

---

##  License

This project is licensed under the MIT License.

---

## ‍ Author

GitHub: sadatnazarli

---

