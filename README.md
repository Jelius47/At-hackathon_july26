<a name="readme-top"></a>

<div align="center">
  <h1>EDUPlatform</h1>
  <br/>

  <h3><b>README</b></h3>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
  - [🚀 Live Demo](#live-demo)
- [💻 Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Install](#install)
  - [Usage](#usage)
  - [Run tests](#run-tests)
  - [Deployment](#deployment)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [🙏 Acknowledgements](#acknowledgements)
- [❓ FAQ](#faq)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 EDUPlatform <a name="about-project"></a>

**EDUPlatform** is a FastAPI-based application that provides educational facts via an API. It integrates with the API Ninjas service to fetch random educational facts and delivers them through a voicemail-like interface.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
    <li><a href="https://www.uvicorn.org/">Uvicorn</a></li>
  </ul>
</details>

<details>
  <summary>API Integration</summary>
  <ul>
    <li><a href="https://api-ninjas.com/">API Ninjas</a></li>
  </ul>
</details>

<details>
  <summary>Environment Management</summary>
  <ul>
    <li><a href="https://pypi.org/project/python-dotenv/">python-dotenv</a></li>
  </ul>
</details>

<!-- Features -->

### Key Features <a name="key-features"></a>

- **Fetches random educational facts from API Ninjas**
- **Provides XML-based voicemail responses**
- **Handles incoming call data and logs session details**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LIVE DEMO -->

## 🚀 Live Demo <a name="live-demo"></a>

> The project is not yet deployed. Once deployed, the live demo link will be added here.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project, you need:

- Python 3.9 or higher
- `pip` (Python package manager)
- An API key from [API Ninjas](https://api-ninjas.com/)

### Setup

Clone this repository to your desired folder:

```sh
  git clone https://github.com/adonis-dave/EDUPLATFORM.git
  cd EDUPlatform
```

### Install

Install the required dependencies:

```sh
  pip install -r requirements.txt
```

### Usage

To run the project, execute the following command:

```sh
  uvicorn main_copy:app --host 0.0.0.0 --port 8000 --reload
```

### Run tests

To run tests, you can use any testing framework like `pytest`. For example:

```sh
  pytest
```

### Deployment

You can deploy this project using any ASGI-compatible server like Uvicorn or Gunicorn. For example:

```sh
  uvicorn main_copy:app --host 0.0.0.0 --port 8000
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

👤 **David**

- GitHub: [adonis-dave](https://github.com/adonis-dave)

👤 **Benjamin**

- GitHub: [benny-png](https://github.com/benny-png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>

- [ ] Add support for multiple languages
- [ ] Integrate with additional educational APIs
- [ ] Deploy the application to a cloud platform

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project, please give it a ⭐️ and share it with others!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgements <a name="acknowledgements"></a>

First and foremost I would like to appreciate the 2nd Winning team in this hackathon for their total focus and dedication to this project.
Loads of appreciation to the [AfricasTalkingLtd](https://github.com/AfricasTalkingLtd) for leading on the Hackathon and granting us their use of their APIs. I thank the creators of [FastAPI](https://fastapi.tiangolo.com/) and [API Ninjas](https://api-ninjas.com/) for their amazing tools.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FAQ -->

## ❓ FAQ <a name="faq"></a>

- **How do I get an API key for API Ninjas?**

  - You can sign up at [API Ninjas](https://api-ninjas.com/) and generate an API key from your account dashboard.

- **Can I deploy this project on a cloud platform?**

  - Yes, you can deploy it on platforms like AWS, Azure, or Heroku using an ASGI server like Uvicorn or Gunicorn.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
