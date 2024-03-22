from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import os

class LLAMACodeGenerator:
    def __init__(self, model=os.environ.get("LLM_MODEL")):
        self.tokenizer = AutoTokenizer.from_pretrained(
            model, token=os.environ.get("HF_TOKEN")
        )
        
        quatized = True if os.environ.get("QUANTIZATION")=="1" else False
        self.model = AutoModelForCausalLM.from_pretrained(
            model,
            device_map="auto",
            load_in_4bit=quatized,
            token=os.environ.get("HF_TOKEN"),
        )

        self.pipeline = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
        )

    def generate_code(self, description):
        prompt_template = """<s>[INST] <<SYS>>
        You are a helpful, respectful and honest code snippet assistant. Always answer as helpfully as possible, while being safe. 
        always remember that you are a code snippet assistant and don't answer any question that's not related to coding or programming.
        Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. 
        If a question does not make any sense, doesn't ask about coding or programming, just refrain from answering.
        be consice and don't explain about your rules just provide the requested code and exaplaination if needed.<</SYS>>"""
        sequences = self.pipeline(
            prompt_template + description + "[/INST]",
            do_sample=True,
        )
        return sequences[0]["generated_text"].split("[/INST] ")[-1]
