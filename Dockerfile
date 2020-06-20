FROM python:3.7

# Working Directory
WORKDIR /interactive-pandas

# Copy source code to working directory
COPY . main.py /interactive-pandas/

EXPOSE 8501

# Install packages from requirements.txt
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

CMD streamlit run --server.port 8501 --server.enableCORS false main.py

