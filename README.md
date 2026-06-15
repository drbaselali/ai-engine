# ai-engine

A collection of applications and functions in prompt and AI engineering using Python.

Current project titled **"Core AI Pipeline Components"**

This project implements local LLM inference, query-based information extraction, context compression, and response generation based on provided evidence using Ollama models. By separation the extraction and the response generation steps, we reduce the strain on the models, reduce hallucinations and improve the quality of the response.

**Project Workflow**
* Provide stored or live query-relevant links
* Pass the links to an Ollama local model (extractor model)
* Produce relevant knowledge summaries
* Pass the summaries to a second Ollama model (generator model)
* Produce the required response

The details of the project and its functions are provided in src. So far the following skills have been demonstrated in the script:

* Prompt engineering
* Local AI deployment
* Multi-modal orchestration
* Evidence-based AI systems

Author
Dr. Basel Ali

