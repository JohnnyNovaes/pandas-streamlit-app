FROM python:3.8

LABEL maintainer = "João Herique Saraceni  <www.linkedin.com/in/joãohenriquesaraceninovaes>"


# Copy local code to the container image.
ENV  interactive-pandas-app /app

WORKDIR $interactive-pandas-app
COPY . ./

# --------------- Install python packages using `pip` ---------------

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt \
	&& rm -rf requirements.txt

# --------------- Configure Streamlit ---------------
RUN mkdir -p /root/.streamlit

RUN bash -c 'echo -e "\
	[server]\n\
	enableCORS = false\n\
	headless = true\n\
	port = $PORT\n\
	" > /root/.streamlit/config.toml'


EXPOSE 8501

# --------------- Export envirennement variable ---------------
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["streamlit", "run","--server.port", "8501", "main.py"]