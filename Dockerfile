FROM python:3.7

WORKDIR /interactive-pandas-app

COPY requirements.txt ./requirements.txt

# Install packages from requirements.txt
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

# Configure Stremlit

RUN mkdir -p /root/.streamlit

RUN bash -c 'echo -e "\
	[server]\n\
	enableCORS = false\n\
	" > /root/.streamlit/config.toml'

EXPOSE 8501
EXPOSE 8080

COPY . /interactive-pandas-app

CMD ["streamlit", "run", "--server.port", "8080", "main.py"]