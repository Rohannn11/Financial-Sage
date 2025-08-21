# FinancialSage

**An intelligent pipeline for financial document classification, storage, semantic search, and predictive analytics, designed to handle structured, unstructured, and handwritten records with minimal human intervention.**

---

## Introduction
FinancialSage is a modular and automated system for processing financial documents of various formats, including invoices, receipts, contracts, statements, and handwritten notes.  
It integrates machine learning (ML), natural language processing (NLP), optical character recognition (OCR), natural language inference (NLI), and predictive analytics to improve efficiency, enhance accuracy, and provide actionable insights for finance teams, auditors, and analysts.

---

## Core Features
- Automated document classification using SVM with TF-IDF vectorization.  
- OCR support for scanned and handwritten documents via Google Cloud Vision API.  
- Natural Language Inference (NLI) with Gemini API to identify content relationships and contradictions.  
- Dynamic routing and storage:  
  - **MySQL** for structured financial data.  
  - **MongoDB** for unstructured/semi-structured data with embeddings.  
- Semantic search using FAISS and sentence-transformer embeddings.  
- Predictive analytics for financial forecasting and anomaly detection.  
- Real-time logging, monitoring, and performance tracking via a Streamlit dashboard.  
- Web interface with drag-and-drop uploads, semantic search, and visualization of trends.  

---

## System Workflow
- **File Ingestion** – Supports uploads of PDFs, CSVs, Excel, JSON, and handwritten documents.  
- **Metadata Extraction** – Extracts file attributes and determines document type.  
- **OCR Processing** – Extracts text from handwritten and scanned files.  
- **Classification** – SVM model categorizes documents into financial types.  
- **NLI Analysis** – Evaluates semantic relationships between documents.  
- **Routing Logic** – Structured data stored in MySQL, unstructured data routed to MongoDB.  
- **Semantic Search** – Embeddings generated with sentence-transformers and indexed with FAISS.  
- **Predictive Analytics** – Time-series and regression models applied to structured data.  
- **Monitoring** – Streamlit dashboard for performance metrics and forecasting results.  

---

## Key Results
- Streamlined financial document processing with reduced manual effort.  
- Accurate classification across diverse file types, including handwritten notes.  
- Semantic search capabilities for rapid retrieval and contextual understanding.  
- Predictive forecasting of financial metrics (e.g., revenue, expenditure trends).  
- Enhanced auditability with real-time logging and monitoring.  

---

## Repository Structure
- **Notebooks and Pipeline**  
  - End-to-end automation of ingestion, classification, OCR, storage, and analytics.  
- **Database Operations**  
  - MySQL for structured financial data with stored procedures for cleaning and validation.  
  - MongoDB for unstructured/semi-structured data with embeddings and vector indexing.  
- **Web Application**  
  - Backend: Flask/FastAPI APIs for pipeline integration.  
  - Frontend: React + Tailwind CSS for upload, search, and visualization.  
- **Monitoring Dashboard**  
  - Built with Streamlit for logging, performance metrics, and predictive trends.  

---

## Tech Stack
- **Programming Language:** Python 3.11  
- **Machine Learning & NLP:** scikit-learn, sentence-transformers, NLTK, spaCy  
- **OCR & NLI APIs:** Google Cloud Vision API, Gemini API  
- **Databases:** MySQL 8.0, MongoDB 5.0  
- **Indexing & Search:** FAISS for vector similarity search  
- **Data Processing:** pandas, numpy, pdfplumber, PyMuPDF  
- **Visualization & Monitoring:** matplotlib, seaborn, Streamlit  
- **Web Application:** Flask/FastAPI (backend), React + Tailwind CSS (frontend)  

---

## Future Enhancements
- Expand support for additional financial document categories.  
- Improve OCR accuracy with domain-specific handwriting datasets.  
- Extend predictive analytics to include advanced deep learning models.  
- Deploy scalable API services for enterprise-level adoption.  

---

## License
MIT License – free to use, modify, and distribute with attribution.

---

## Repository Description
**FinancialSage** – End-to-end system for financial document automation. Supports classification, OCR, NLI, semantic search, and predictive analytics, with dynamic routing to MySQL and MongoDB for structured and unstructured data management.
