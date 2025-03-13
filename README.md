<div align="center">

# 🌟 Drop-RAG API

*A lightweight Retrieval-Augmented Generation API*

[![Version](https://img.shields.io/badge/version-0.1.0-blue?style=for-the-badge)](https://github.com/tienndm/drop-rag)
[![Status](https://img.shields.io/badge/status-alpha-orange?style=for-the-badge)](https://github.com/tienndm/drop-rag)
[![Python](https://img.shields.io/badge/python-3.8%2B-green?style=for-the-badge&logo=python)](https://www.python.org/)

</div>

## 📑 Table of Contents

- [📖 Overview](#-overview)
- [✨ Features](#-features)
- [🛠️ Installation](#️-installation)
- [🚀 Quick Start](#-quick-start)
- [📋 API Reference](#-api-reference)
- [⚙️ Configuration](#️-configuration)
- [🔍 Advanced Usage](#-advanced-usage)
- [📊 Performance Considerations](#-performance-considerations)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)
- [📬 Contact](#-contact)

## 📖 Overview

**Drop-RAG** is a lightweight, easy-to-use Retrieval-Augmented Generation (RAG) API that enhances large language model outputs with relevant retrieved information.

> RAG combines the power of retrieval-based systems with generative AI to deliver more accurate and reliable results with reduced hallucination.

With Drop-RAG, you can:
- 🔎 Retrieve information from your document collection based on semantic similarity
- 🧠 Augment LLM responses with contextually relevant information
- ✅ Create more accurate, factual, and context-aware AI responses

## ✨ Features

| Feature | Description |
|---------|-------------|
| **📦 Simple Integration** | Easy to integrate with existing LLM pipelines |
| **📄 Flexible Document Ingestion** | Support for various document formats (PDF, TXT, DOCX, etc.) |
| **⚙️ Customizable Retrieval** | Configure embedding models and retrieval parameters |
| **⚡ Efficient Indexing** | Fast retrieval through optimized vector storage |
| **🔌 API-first Design** | RESTful API architecture for easy integration |

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

<table>
  <tr>
    <th>Endpoint</th>
    <th>Method</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>/index</code></td>
    <td><code>POST</code></td>
    <td>Add documents to the retrieval index</td>
  </tr>
  <tr>
    <td><code>/query</code></td>
    <td><code>POST</code></td>
    <td>Query the system with RAG</td>
  </tr>
  <tr>
    <td><code>/health</code></td>
    <td><code>GET</code></td>
    <td>Check API health status</td>
  </tr>
  <tr>
    <td><code>/metrics</code></td>
    <td><code>GET</code></td>
    <td>Get usage metrics and statistics</td>
  </tr>
</table>

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

- **Scaling**: Index size scales linearly with document count
- **Latency**: Query latency typically ranges from 50-200ms
- **Optimization**: Consider chunking strategy based on your document collection

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

<div align="center">

Built with ❤️ by the Drop-RAG team

</div>
