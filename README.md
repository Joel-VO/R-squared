# Valid Extraction and Retrieval of Data from Information on Court Trials(Project VERDICT)

## Introduction - What's Project VERDICT? 
VERDICT is fully connected court case pipeline for people to access their court cases, to retrieve data, to ask doubts and to ask for guidance using a chatbot feature. The UI is made user-friendly and minimalistic by design to allow easy use of the website and its features.  
Users can prompt court cases based on their respective IPC section and collect the data, or they can filter out the files based on the place where the crime was reported and so on. This dynamic approach is made possible with the use of a vector based Database (FAISS) that allows the retrieval of data based on matches in the text. 
The pipeline also allows the easy insertion of new pdf image data into the database after converting to a vector space.

### Features
- **PDF Processing:**: Convert court case PDFs into images using pymupdf and extract text using OCR.
- **Search & Query:**: Index extracted data for efficient searching and querying using a vector database.
- **Chatbot Interface:**: Interact with the dataset using natural language queries.
- **User Friendly UI**: The UI is simple to understand and the users can easily prompt for the appropriate court cases and can ask queries as needed.
- **Prompt Engineered Response**: The prompt is carefully tuned to provide accurate and comprehensive response.


## Installation
### Running Locally
#### **For Linux/Mac**
```bash
git clone https://github.com/Joel-VO/R-squared.git
```

```bash
# Venv creation and installation of requirements
python venv -m venv
source venv/bin/activate
pip install -r requirements.txt
```
```bash
# Running streamlit locally
streamlit run app.py
```
#### **For Windows**
```bash
git clone https://github.com/Joel-VO/R-squared.git
```

```bash
python -m venv venv 
# Run this for cmd prompt
path\to\venv\Scripts\activate 
# Run this for PowerShell
.\path\to\venv\Scripts\Activate 
pip install -r requirements.txt
```
```bash
# Running locally
streamlit run app.py
```

## Documentation and related information
* A comprehensive Documentation covering all aspects of our code can be found in [DOCUMENTATION.md](#/DOCUMENTATION.md)
* Licensed under GPL 3.0 Licensing, covered here in [LICENSE](#/LICENSE).
* For image-text conversion, [Tesseract](https://github.com/tesseract-ocr/tesseract) is used.  
* For text to embedded vector conversion to be used in the vector database, [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

