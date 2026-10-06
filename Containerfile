FROM docker.io/library/python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY app/health.py .
RUN useradd --no-create-home --shell /usr/sbin/nologin appuser
USER appuser
EXPOSE 8000
CMD ["python", "health.py"]
