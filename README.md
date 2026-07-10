# ai-engine

A collection of applications and functions in prompt and AI engineering using Python.

Current project titled **"Core AI Pipeline Components"**

This project implements local large language model (LLM) inference, query-based information extraction, context compression, and response generation based on provided evidence using raw LLM models via Ollama. Furthermore, after response generation, the pipeline continues by extracting claims and classifying them, which then allows the model to evaluate these claims and produce a recommendation summary.

**Project Workflow**

* Provide stored or live query-relevant links
* Pass the links to an Ollama local model (extractor model)
* Produce relevant knowledge summaries
* Pass the summaries to a second Ollama model (generator model)
* Produce the required response
* Extract atomic claims
* Classify the extracted claims
* Review the response and claims and produce recommendations summary

The details of the project and its functions are provided in src. This project demonstrates the following capabilities:

* Prompt engineering
* Local AI deployment
* Multi-step LLM orchestration
* Evidence-based AI systems

Author

Dr. Basel Ali

