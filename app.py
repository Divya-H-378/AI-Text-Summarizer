import json
import urllib.request

def summarize_text(text):
    """
    Connects to a free, open-source AI model on Hugging Face 
    to automatically summarize text.
    """
    print("Connecting to AI Model...")
    
    # We use a standard, public text-summarization pipeline API
    api_url = "https://huggingface.co"
    
    # Payload format required by modern AI models
    payload = {"inputs": text, "parameters": {"do_sample": False}}
    data = json.dumps(payload).encode("utf-8")
    
    # Sending the request to the AI model
    req = urllib.request.Request(api_url, data=data, method="POST")
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result[0]['summary_text']
    except Exception as e:
        return f"Error connecting to AI API: {str(e)}"

# Example Execution
if __name__ == "__main__":
    sample_document = """
    Electronics and Communication Engineering (ECE) is a robust discipline bridging hardware 
    and software engineering. In modern environments, ECE engineers leverage internet-of-things 
    (IoT) frameworks, embedded systems, and automated machine learning architectures to design 
    smart solutions. Understanding how logic applies to both physical microcontrollers and 
    cloud-based API endpoints is crucial for upcoming technical professionals.
    """
    
    print("\n--- Original Text ---", sample_document)
    summary = summarize_text(sample_document)
    print("\n--- AI Generated Summary --- \n", summary)
