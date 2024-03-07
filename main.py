from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient

# Replace with your Form Recognizer endpoint and API key
endpoint = "https://demoformrecogdata.cognitiveservices.azure.com/"
key = "8795117727734d618b007ea695b5f6ef"

# Create a FormRecognizerClient
credential = AzureKeyCredential(key)
client = FormRecognizerClient(endpoint, credential)

# Replace 'document_url' with the URL of the document you want to analyze
document_url = "Review-Midterm 8.pdf"

# Submit the document for analysis
poller = client.begin_recognize_content_from_url(document_url)
form_pages = poller.result()

# Extract formulas from the response
formulas = []
for idx, page in enumerate(form_pages):
    for table in page.tables:
        for cell in table.cells:
            if cell.is_header:
                continue
            if cell.kind == "number" and cell.confidence > 0.8:  # Adjust confidence threshold as needed
                formulas.append(cell.text)

# Print detected formulas
print("Detected Formulas:")
for formula in formulas:
    print(formula)
