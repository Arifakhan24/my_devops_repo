FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./model /model

COPY ./app /app

WORKDIR /app/

ENV PYTHONPATH=/app

RUN ls -lah /app/*

COPY ./start.sh /start.sh

RUN chmod +x /start.sh

EXPOSE 80

CMD ["/start.sh"]
#ENTRYPOINT ["python","-m","gunicorn","main:app","--worker-class=uvicorn.workers.UvicornWorker"]
#EXPOSE 8000
