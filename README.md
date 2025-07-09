# 🏏 IPL Insights Dashboard: 2008–2025

## 📌 Project Overview  
This dashboard offers a comprehensive analysis of **Indian Premier League (IPL)** cricket data from its inception in **2008** to the **2025 season**. Designed for cricket enthusiasts, analysts, and stakeholders, the dashboard reveals key performance metrics, historical trends, and team-wise comparisons using a rich dataset and intuitive visual design.

---



## ✨ Key Features  

An interactive and dynamic Tableau dashboard with deep statistical analysis:

### 🔹 Universal Global Filters
- **Season Filter:** Top-right dropdown for filtering one or multiple IPL seasons (e.g., "2008", "2012", "2023–2025").
- This global filter updates all relevant visualizations simultaneously.

### 🔹 Key Performance Indicators (KPIs)
- **At-a-glance metrics**:  
  - Total Matches  
  - Total Runs  
  - Total Wickets  
  - Average Runs  
  - Average Wickets  
  - Extras (Wides, Legbyes, No Balls)

### 🔹 Team Performance Analysis
- **Team Total Runs**: Horizontal bar chart with scroll support, showing offensive power per team.
- **Team Run Distribution**: Histogram revealing how runs are spread across matches.

### 🔹 Match Outcome Analysis
- **Toss Decision (Pie Chart)**: Percentage split of "Bat" vs "Field" decisions.
- **Superover Winners by Toss**: Table displaying Superover outcomes based on toss choices.

### 🔹 Season Match Count
- Bar chart of match frequency per season, highlighting league growth or contraction.

### 🔹 Interactive Action Filters
- Clicking on elements (e.g., a team) filters the entire dashboard for focused analysis—a common practice in Tableau.

---

## 🛠 Technologies Used

- **Tableau Desktop** – Core visualization and dashboard creation.
- **Microsoft Excel** *(if applicable)* – Initial data cleanup and reshaping.
- **Python(Pandas)** *(data cleaning via `data.py`)* – Advanced preprocessing and transformation.

---



### 📦 Data Extraction & Cleaning

- To access the cleaned dataset used in this project:
  - First, **extract** the file `Csv_File.gz` from the repository.
  - Run the preprocessing script `data.py` to generate the final cleaned CSV used for Tableau visualization.

### 🧹 Cleaning Steps in `data.py`:
- Removed duplicate rows
- Trimmed whitespace from all string-based columns
- Converted appropriate columns (like team names, match types) to categorical data types
- Handled missing values with appropriate strategies (e.g., fill, drop, or imputation)
- Standardized inconsistent formats (e.g., team names, dates, outcomes)
- Generated calculated fields required for KPIs and Tableau interactivity

---






## 🔗 How to View the Dashboard

There are two primary ways to explore this IPL Insights Dashboard:

1.  **View on Tableau Public (Recommended for Interactivity):**
    Experience the full interactive functionality of the dashboard directly in your web browser. This includes using the **universal global filters** and **action filters** to explore the data in detail.
    * [**View Live Dashboard**](https://public.tableau.com/views/IPLKeyStats2008-2025/IPL2025Dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

2.  **Open the Tableau Packaged Workbook (.twbx):**
    If you have Tableau Desktop or Tableau Reader installed, you can download the `.twbx` file to open and explore the workbook locally. This allows for full access to the underlying sheets, calculations, and data structure.
    * [**Download Workbook (.twbx)**](IPL_Insights_2008_2025.twbx) 
    * *(Make sure the filename `IPL_Insights_2008_2025.twbx` matches the actual name of your .twbx file in your Gitlab repo.)*
    * **Steps to Open:**
        1.  Extract the `Csv_File.gz` file from this repository.
        2.  Open Tableau Desktop or Tableau Reader.
        3.  Go to `File > Open` and select the downloaded `IPL Key Stats 2008-2025.twbx` file.
---

## 📈 Key Insights

- 🏆 **Consistent High Performers:** Teams like *[e.g., Chennai Super Kings]* show high cumulative runs and win rates.
- 🎯 **Toss Strategy Impact:** Toss decisions reveal strong preferences; fielding often dominates in key matches.
- 📊 **Scoring Trends:** High frequency of 150+ run matches; scoring patterns vary sharply across teams and years.
- 📅 **Seasonal Dynamics:** Notable spike in match volume post-2020; recent years show more competitive balance.

---

## 🔮 Future Improvements

- 🔄 Real-time match data integration  
- 📋 Player-level analytics (strike rate, economy, impact index)  
- 🌦 Weather vs performance correlation  
- 🤖 Predictive modeling for match outcomes  

---

## 👤 Author & Credits

**Author:** *Annaz Mus Sakib*  


**Data Credits:**  
📊 📂Dataset from [Kaggle IPL Dataset (2008–2025)](https://www.kaggle.com/datasets/chaitu20/ipl-dataset2008-2025/data)