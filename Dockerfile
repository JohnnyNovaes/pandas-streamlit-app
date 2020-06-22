FROM python:3.7

WORKDIR /interactive-pandas-app

COPY requirements.txt ./requirements.txt

# Install packages from requirements.txt
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8501

COPY . /interactive-pandas-app
ENTRYPOINT ["streamlit","run"]

CMD ["main.py"]