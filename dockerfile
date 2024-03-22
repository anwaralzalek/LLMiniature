# Use a Pytorch runtime image
FROM pytorch/pytorch:2.2.1-cuda12.1-cudnn8-devel

# Set the working directory for app files
WORKDIR /app

# Copy the dependencies file into the container
COPY requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Copy your application code into the image`
COPY ./ ./

RUN pip install -e .

# Expose the port used by FastAPI (typically 8000)
EXPOSE 8000

# The default command to start the app when the container runs
CMD ["uvicorn", "--host", "0.0.0.0", "app:app", "--reload"] 
