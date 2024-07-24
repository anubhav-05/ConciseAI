# ConciseAI

## Pegasus Text Summarizer

This project implements a Flask-based web application for summarizing text using the Pegasus model. The application takes user-provided text input and returns a concise summary.

## Project Overview

The Pegasus Text Summarizer project aims to provide an easy-to-use interface for summarizing text. By leveraging the powerful Pegasus model, the application can generate high-quality summaries for various types of text inputs.

## Features

- **Text Summarization:** Users can input any text, and the application will generate a concise summary.
- **Web Interface:** The project includes a simple web interface built with HTML, CSS, and JavaScript.
- **Pre-trained Model:** Utilizes the Pegasus model trained on the Samsung/samsum dataset from Hugging Face.

## Project Structure

The project directory contains the following key files and folders:
ConciseAI/
├── app.py
├── model_state_dict.pth
├── templates/
│ └── index.html
├── static/
│ ├── css/
│ │ └── styles.css
│ └── js/
│ └── scripts.js
├── pegasus-samsum/
│ ├── tokenizer_config.json
│ ├── special_tokens_map.json
│ ├── tokenizer.json
│ ├── vocab.txt
│ └── config.json


- **app.py:** The main Flask application script that handles web requests and interacts with the model.
- **model_state_dict.pth:** The saved state dictionary of the pre-trained Pegasus model.
- **pegasus-samsum/:** Directory containing tokenizer files necessary for text processing.
- **templates/:** Directory containing HTML templates for the web interface.
- **static/:** Directory containing CSS and JavaScript files for styling and client-side functionality.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- PyTorch
- Transformers library from Hugging Face

### Installation

#### Clone the repository:

```bash
git clone https://github.com/anubhav-05/ConciseAI.git
cd ConciseAI


#### Create a virtual environment and activate it:

python -m venv textSum
source textSum/bin/activate (Linux/Mac)
textSum\Scripts\activate (Windows)


#### Download the `model_state_dict.pth` and `pegasus-samsum` directory:

Ensure these files and directories are in the root of the project directory.

#### Run the Flask application:

python app.py


#### Access the application:

Open your web browser and go to `http://127.0.0.1:5000/`

## Dataset

The model was fine-tuned on the Samsung/samsum dataset from Hugging Face, which consists of conversational text data. The dataset is available in the repository as a zip file.

## Usage

1. Navigate to the web interface.
2. Input the text you want to summarize in the provided text area.
3. Click the "Summarize" button to generate the summary.
4. View the summarized text displayed on the page.

## Notes

- Ensure that the `model_state_dict.pth` file and `pegasus-samsum` directory are correctly placed in the project root directory.
- The application is configured to run on a CPU. For faster performance, you may consider using a GPU if available.


