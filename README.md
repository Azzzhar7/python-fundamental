# Python Fundamentals - Summer Short Course

## Development Environment Setup (Windows | Linux | Google Colab)

### Pre-requisites
- Basic understanding of programming logic  
- Python 3.9+ installed on system  
- Familiarity with command line usage (basic level)  

### Setup Instructions
- Install Python 3.9+  
- Recommended tools:  
  - Anaconda (comes with Jupyter Notebook & libraries pre-installed), or  
  - Manual installation: `pip install numpy pandas matplotlib`  
- Use Jupyter Notebook, VS Code, or PyCharm to run your code.  
- For cloud-based execution, upload the notebook to Google Colab.  

---

## Short Course Outline (Weekly Distribution)

### Week 1
- Hello World program  
- Variables demonstration  
- Data types usage  
- Operators examples  
- Control flow (if/else)  
- Iterations (loops)  
- Input and Output handling  

### Week 2
- Lists operations  
- Dictionaries usage  
- Functions implementation  
- Exception handling  
- Scope management  
- Mini Project: Contact Book  
- Mini Project: Student Grades System  

### Week 3
- Reading and writing text files  
- Working with CSV files  
- Using built-in modules  
- Creating custom modules  
- Basic Command Line Interface (CLI)  
- Mini Project: To-do List  
- Mini Project: Expense Tracker  

---

## Technical Guide on Comprehensive Task

### Scenario Background
The agricultural research team is collecting crop yield data from small farms to understand productivity trends and prepare for future AI-based automation. The tasks in this course gradually build from basic Python logic to applied data analysis and visualization.  

---

### Task 1: Fundamentals of Python (Logic & Data Representation)

**Details Implemented:**  
- Script displays “Welcome to Crop Yield Analyzer”.  
- Variables store farmer’s name, farm size (in acres), and main crop.  
- Demonstration of integers, floats, strings, and booleans.  
- If-else check for farm size classification (Large or Small).  
- Loops generate a sample list of crops: [“Wheat”, “Rice”, “Corn”].  

**Topics Covered:** Data types, variables, conditionals, loops.  

---

### Task 2: Static Data Processing (Pre-Generated Dataset)
**Details Implemented:**  
- Dataset stored as a list of dictionaries or tuples.  
- Code prints farmers growing Wheat.  
- Total yield calculated across all farmers.  
- Farmer with maximum yield identified.  

**Topics Covered:** Lists, dictionaries, loops, basic aggregation.  

**Sample Dataset Structure:**  
```python
data = [
    {"Farmer": "Farmer 1", "Crop": "Wheat", "Acres": 5, "Yield": 12, "Region": "North"},
    {"Farmer": "Farmer 2", "Crop": "Rice",  "Acres": 8, "Yield": 18, "Region": "South"},
    {"Farmer": "Farmer 3", "Crop": "Corn",  "Acres": 4, "Yield": 9,  "Region": "East"},
    {"Farmer": "Farmer 4", "Crop": "Wheat", "Acres": 6, "Yield": 14, "Region": "West"},
]
```

### Task 3: Data Analysis (Beginner Level)

**Details Implemented:** 
- Functions calculate average yield per crop type.
- Functions count farmers per region.
- Exception handling ensures missing data does not break execution.

Topics Covered: Functions, error handling, reusable code.

### Task 4: Statistical Analysis

**Details Implemented:**
- Mean, Median, and Mode of crop yields calculated.
- Standard deviation computed for variability.
- Correlation measured between acres and yield.

Sample Output Example:
Mean Yield = 13.25 tons
Median Yield = 13 tons
Standard Deviation = 3.5
Correlation (Acres, Yield) = 0.89

Topics Covered: Basic statistics using Python (statistics module, NumPy optional).

### Task 5: Data Visualization (Graphs & Tables)

**Details Implemented:**  
- Bar chart for average yield per crop.
- Pie chart for percentage of farmers by region.
- Scatter plot for acres vs yield.
- Tabular representation of results using Pandas DataFrame.

Topics Covered: Beginner data visualization, tables, result presentation.

# Extension (Optional Advanced Mini-Project)

**Details Implemented:**  
- Simple prediction of expected yield using:
  Predicted Yield = Acres × Average Yield per Acre (based on dataset)
- Results displayed for each farmer.

## How to Use
- Copy this course task guide into a new file named:  
  `python_fundamentals_AI_agriculture.ipynb`
- Upload to Google Colab or Jupyter Notebook.
- Execute step by step using (Shift+Enter).

## **Contact**
- *Email: [muhammadazhar@uaar.edu.pk](mailto:muhammadazhar@uaar.edu.pk)*
- *Linkedin: [https://www.linkedin.com/in/azzzhar7/](https://www.linkedin.com/in/azzzhar7/)*