# Base image with Miniconda
FROM continuumio/miniconda3

# Create and set working directory
WORKDIR /app

# Copy everything into the container (including environment.yml)
COPY . .

# Create the Conda environment
RUN conda env create -f environment.yml --yes

# Auto-activate the environment in every interactive shell
RUN echo "conda activate f1" >> ~/.bashrc

# Start in login shell (which will activate the env)
ENTRYPOINT ["bash", "-l"]