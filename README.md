# GenAI_Recommenation_App

### Demo:

https://github.com/user-attachments/assets/fc7ad55f-43ce-490a-b5df-5fa35343e3af


### Architecture
                                ┌────────────────────────────┐
                                │       PDF Documents        │
                                └────────────┬───────────────┘
                                             │
                                             ▼
                 ┌──────────────────────────────────────────────┐
                 │ Load PDFs using DirectoryLoader (helper.py)  │
                 └────────────────────┬─────────────────────────┘
                                      │
                                      ▼
         ┌────────────────────────────────────────────────────────────┐
         │ Chunk PDFs using RecursiveCharacterTextSplitter (helper.py)│
         └────────────────────┬───────────────────────────────────────┘
                              │
                              ▼
     ┌────────────────────────────────────────────────────────────────────────┐
     │ Generate Embeddings using HuggingFace (all-MiniLM-L6-v2) (helper.py)  │
     └────────────────────┬──────────────────────────────────────────────────┘
                          │
                          ▼
     ┌────────────────────────────────────────────────────────────┐
     │ Store Embeddings into Pinecone Vector Store (docsearch)    │
     └────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
         ┌────────────────────────────────────────────┐
         │ User sends query via Flask UI (chat.html)  │
         └────────────────────┬───────────────────────┘
                              │
                              ▼
                           app.py
                              │
    ┌─────────────────────────┼────────────────────────────────────────┐
    │                         │                                        │
    ▼                         ▼                                        ▼
recommend.py       ┌───────────────────────┐               ┌────────────────────────┐
(Checks hardcoded  │ Retrieve similar docs │               │   .env (API Keys)      │
  brand prompts)   │   from Pinecone index │               └────────────────────────┘
                   └────────────┬──────────┘
                                ▼
                 ┌────────────────────────────────┐
                 │  Prompt + OpenAI (chat model)  │
                 └────────────┬───────────────────┘
                              ▼
                     ┌────────────────────┐
                     │  Final Answer Sent │
                     └────────────────────┘
