# Smart Complaint Categorizer

## Overview

Smart Complaint Categorizer is a Python-based terminal application that automatically categorizes customer complaints based on their content. It assigns a complaint category, determines its priority level, recommends the responsible department, and stores the complaint history for future analysis.

The application demonstrates how rule-based text processing can automate customer support workflows before integrating advanced AI or NLP models.

---

## Features

- Complaint Categorization
- Priority Detection
- Department Assignment
- Complaint History
- Statistics Dashboard
- JSON Data Storage
- History Management
- Rule-Based Classification
- Object-Oriented Design

---

## Project Structure

complaint-categorizer/

├── complaint_categorizer.py

├── complaint_studio.py

├── README.md

└── .gitignore

---

## Requirements

- Python 3.x

No external libraries are required.

---

## Run

```bash
python complaint_studio.py
```

---

## Menu

1. Analyze Complaint

2. View Complaint History

3. View Statistics

4. Delete History

5. Exit

---

## Complaint Categories

- Billing
- Technical
- Delivery
- Account
- General

---

## Priority Levels

- Critical
- High
- Medium
- Low

---

## Example

### Complaint

I paid twice for my order but my refund has not been processed.

### Output

Category : Billing

Priority : Medium

Department : Finance Team

---

### Complaint

Application crashes while logging into my account.

### Output

Category : Technical

Priority : High

Department : Technical Support

---

## Generated File

complaint_history.json

Stores all complaint records automatically.

---

## Applications

- Customer Support
- Help Desk Systems
- CRM Platforms
- E-commerce Support
- Telecom Complaint Management
- Banking Customer Service
- IT Support Centers

---

## Future Improvements

- AI-based Complaint Classification
- Sentiment Analysis
- Complaint Similarity Detection
- Automatic Ticket Generation
- Email Integration
- Dashboard with Charts
- Complaint Trend Analysis
- Multi-language Complaint Support
- PDF Report Export
- REST API Integration

---

## License

MIT License