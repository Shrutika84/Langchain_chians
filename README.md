# LangChain – Chains

This repo contains examples of different **chain types** in [LangChain](https://www.langchain.com/).  
A **chain** is a workflow where the output of one step becomes the input of the next, allowing you to build multi-step LLM applications.

---

## 📂 Files

- `Simple_chain.py` – single-step chain example  
- `Sequential_chain.py` – step-by-step pipeline where one LLM call feeds the next  
- `Parallel_chain.py` – run multiple prompts in parallel and combine outputs  
- `Conditional_chain.py` – branch logic based on conditions  

---

## ▶️ Run Examples
```bash
python Simple_chain.py
python Sequential_chain.py
python Parallel_chain.py
python Conditional_chain.py
```

---

## 💡 Note
Chains make your LLM applications:
- **Modular** → break tasks into steps  
- **Reusable** → swap prompts or models easily  
- **Reliable** → enforce structure with parsers and validation  
