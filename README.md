# LLMiniature


## About the Project

This project leverages the power of Llama2 to provide on-demand coding assistance through a user-friendly web interface.</br> Whether you're a beginner struggling with syntax or an experienced developer looking to optimize code,</br> this tool offers AI-generated suggestions and explanations to streamline your development process.


## Tech Stack
* JavaScript
* fastapi
* python
* docker
* huggingface

## Getting Started
to run the server please do the following:</br>
</br>
    1. change directory to LLMiniature</br>
    2. get an access from huggingface to use llama2 model from this webpage: https://huggingface.co/meta-llama </br>
    3. make sure to copy .env.template and make .env file from it and include your huggingface tokens from your account settings </br>
    4. build the docker image that will the server: docker compose build</br>
    3. run the server: docker compose up</br>

once the server is running you have to wait few minuts (depedning on your connection speed) </br>
untill the model is downloaded and loaded to GPU

then you can open the webpage 
```localhost:8000```
and start asking the model

 
## Usage
  this project has been tested on a laptop machine with 16GB of RAM and 3070 GPU with 8GB VRAM</br>
  due to limited resources an int 8 bit quatization has been implemented </br>
  you can simply turn off quantization from .env by setting it to 0 (which will increase model reply accuracy a little bit)</br>
  also smaller version of llama2 has been used you </br>
  ```meta-llama/Llama-2-7b-chat-hf```</br>
  you can have much powerful responses by changing the number before </br>
  ```b``` to either ```13``` or ```70``` but be aware that those models will need much more </br>
  RAM and VRAM in your system



