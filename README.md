# 🚀 Drop-RAG API

![Version](https://img.shields.io/badge/version-0.1.0-blue)
![Status](https://img.shields.io/badge/status-alpha-orange)
![Python](https://img.shields.io/badge/python-3.8%2B-green)

## 📖 Overview

Drop-RAG is a lightweight, easy-to-use Retrieval-Augmented Generation (RAG) API that enhances large language model outputs with relevant retrieved information. This API allows you to:

- Retrieve information from your document collection based on semantic similarity
- Augment LLM responses with contextually relevant information
- Create more accurate, factual, and context-aware AI responses

RAG combines the power of retrieval-based systems with generative AI to deliver more accurate and reliable results with reduced hallucination.

## ✨ Features

- **Simple Integration**: Easy to integrate with existing LLM pipelines
- **Flexible Document Ingestion**: Support for various document formats (PDF, TXT, DOCX, etc.)
- **Customizable Retrieval**: Configure embedding models and retrieval parameters
- **Efficient Indexing**: Fast retrieval through optimized vector storage
- **API-first Design**: RESTful API architecture for easy integration

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/tienndm/drop-rag.git
cd drop-rag

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .
```

## 🚀 Quick Start

### 1. Start the API server

```bash
python -m drop_rag.server
```

### 2. Index your documents

```python
import requests

response = requests.post(
    "http://localhost:8000/index",
    json={
        "documents": [
            {"id": "doc1", "text": "RAG systems enhance LLM outputs with retrieved information."},
            {"id": "doc2", "text": "Vector databases are crucial for efficient RAG implementations."}
        ]
    }
)
print(response.json())
```

### 3. Query with RAG

```python
response = requests.post(
    "http://localhost:8000/query",
    json={
        "query": "How do RAG systems work?",
        "top_k": 3
    }
)
print(response.json())
```

## 📋 API Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/index` | POST | Add documents to the retrieval index |
| `/query` | POST | Query the system with RAG |
| `/health` | GET | Check API health status |
| `/metrics` | GET | Get usage metrics and statistics |

## ⚙️ Configuration

Create a `config.yaml` file in the project root:

```yaml
embedding_model: "sentence-transformers/all-MiniLM-L6-v2"
vector_db:
  type: "faiss"  # Options: faiss, milvus, pinecone
chunk_size: 512
chunk_overlap: 50
```

## 🔍 Advanced Usage

### Custom Embedding Models

```python
from drop_rag import RAGClient

client = RAGClient(
    embedding_model="sentence-transformers/all-mpnet-base-v2",
    normalize_embeddings=True
)
```

### Processing Large Document Collections

```python
# For large document collections, use batch processing
from drop_rag.utils import batch_process

documents = load_document_collection("path/to/docs")
batch_process(documents, batch_size=100)
```

## 📊 Performance Considerations

- Index size scales linearly with document count
- Query latency typically ranges from 50-200ms
- Consider chunking strategy based on your document collection

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📬 Contact

For questions and feedback, please open an issue or contact the maintainers.

---

Built with ❤️ by the Drop-RAG team
