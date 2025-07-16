from azure.storage.blob import BlobServiceClient

# Initialize client
blob_service_client = BlobServiceClient.from_connection_string("YOUR_AZURE_BLOB_CONNECTION_STRING")
container_client = blob_service_client.get_container_client("chatbot-data")

def get_all_texts():
    texts = []
    for blob in container_client.list_blobs():
        # Download blob content
        blob_client = container_client.get_blob_client(blob)
        data = blob_client.download_blob().readall()
        try:
            texts.append(data.decode('utf-8'))  # for txt files
        except:
            pass  # handle PDFs/others separately
    return "\n".join(texts)
