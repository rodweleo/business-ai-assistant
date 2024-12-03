from transformers import AutoTokenizer, AutoModelForCausalLM

def test_model():
    model_name = "gpt-neo-125M"  # A lightweight model for testing
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    print("Model and tokenizer loaded successfully!")

if __name__ == "__main__":
    test_model()
