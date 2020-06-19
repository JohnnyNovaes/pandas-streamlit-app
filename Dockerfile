FROM python:3.7

WORKDIR /interactive-pandas-app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8501

COPY . /interactive-pandas-app

CMD streamlit run --server.port 8501 --server.enableCORS false main.py

