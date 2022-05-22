FROM python:slim-bullseye

# Create app directory
WORKDIR /app/

# Create ctf user
RUN adduser ctf

# Copy app source
COPY --chown=ctf:ctf --chmod=500 ./flag.py /app/.

# Use ctf user
USER ctf

# Start the server
CMD ["python3", "/app/flag.py"]
