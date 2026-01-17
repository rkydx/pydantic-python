# Pydantic Python Examples

This repository demonstrates how to use **Pydantic (v2)** for data validation, type enforcement, and structured model creation in Python using real-world examples.

In this repository, you will find practical implementations of Pydantic models using `Field`, `Annotated`, `Optional`, and email validation with `EmailStr`.

---

## Features

* Data validation using Python type hints
* Automatic type conversion (e.g., string → int)
* Email validation using `EmailStr`
* Optional and required field handling
* Clean and readable model definitions

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
pydantic==2.12.5
email-validator==2.3.0
typing_extensions==4.15.0
annotated-types==0.7.0
dnspython==2.8.0
idna==3.11
typing-inspection==0.4.2
pydantic_core==2.41.5
```

---

## Virtual Environment Setup (Windows)

```bash
python -m venv .myenv
.\.myenv\Scripts\activate
```

---

## Example Usage

```python
patient1 = Patient(**patient_info)
get_patient_data(patient1)
```

Pydantic automatically validates and converts input data into structured Python objects.

---

## Concepts Covered

* BaseModel
* Field constraints
* Annotated types
* Optional fields
* Dictionary unpacking
* Serialization & validation

---

## Purpose

This repository is created for learning, practicing, and understanding how Pydantic works in real Python applications such as APIs, data pipelines, and backend services.

---

