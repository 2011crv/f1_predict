# Base image with Miniconda
FROM continuumio/miniconda3

# Copy the Conda environment definition
COPY environment.yml .

# Create the Conda environment (non-interactive)
RUN conda env create -f environment.yml --yes

# Create a startup script to launch bash inside the environment
RUN echo '#!/bin/bash\nconda run -n f1 bash' > /entry.sh && chmod +x /entry.sh

# Set working directory
WORKDIR /app

# Copy the rest of your source code
COPY . .

# Use the startup script as entrypoint
ENTRYPOINT ["/entry.sh"]
