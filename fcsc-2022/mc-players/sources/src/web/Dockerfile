FROM python:slim-bullseye

# Create app directory
WORKDIR /app/

# Copy app source
COPY --chown=root:root --chmod=400 ./requirements.txt /app/.

# Install dependencies
RUN \
        pip install --no-cache-dir -r requirements.txt &&\
        adduser ctf

# Copy app source
COPY --chown=ctf:ctf --chmod=500 ./app /app/

# Copy healthcheck script
COPY --chown=ctf:ctf --chmod=500 ./healthcheck.py /app/.

# use ctf user
USER ctf

# Start the server
CMD ["prlimit", "--nproc=0", "python3", "app.py"]
