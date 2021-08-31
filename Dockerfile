FROM python:3

WORKDIR /usr/src/app

# install spacy
RUN pip3 install -U spacy  

# move the tmp folder so we don’t run
# out of disk space during model install.
RUN export TMPDIR='/var/tmp'

# download and install the german news model (small)
RUN python -m spacy download de_core_news_sm

COPY . .

CMD [ "python", "./tagger.py" ]
