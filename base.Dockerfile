# Base image with Conda
FROM continuumio/miniconda3:latest

# Copy the environment.yml file into the image
COPY environment.yml .

# Create the environment
RUN conda env create -f environment.yml

# Activate the environment
RUN conda activate f1

#Set the Conda env as the default for all subsequent commands
SHELL ["conda", "run", "-n", "f1", "/bin/bash", "-c"]

# Set the working directory inside the container
WORKDIR /app

# Copy the rest of your project files into the container
COPY . .

# Start a bash shell by default when the container runs
CMD ["bash"]