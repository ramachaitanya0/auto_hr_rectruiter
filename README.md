#  IntelliHire

 This Application is designed to streamline the recruitment process for HR professionals.
 Leveraging advanced artificial intelligence, the app allows recruiters to effortlessly 
 sift through stacks of resumes and identifies the most relevant candidates for a particular
 job opening. The intuitive interface enables quick and easy navigation, while the powerful 
 recommendation engine analyzes resumes based on key criteria and provides instant matches.

Key Features
1. Document upload capability.
2. Interactive and user-friendly chat interface
3. Automated Recommendations
4. You can Check the Amount Spent in Each Session 
5. You can Generate Job Description based on your company requirement
6. You can Generate Question and Answers based on the Required Role , Experience Level etc.

# Installation

1. Clone the Git Hub Repo into your local workspace using the below code.
```sh
git clone https://github.com/ramachaitanya0/auto_hr_rectruiter.git 
```

2. Create a Conda Environment.
```sh
conda create -n <env_name> python=3.11.5
```

3. Activate the conda Environment
```sh
conda activate <env_name> 
```

4. Install all the required Packages using requirements.txt file.
```sh
pip install -r requirements.txt
```
5. Add .env file in the Repo and add your OPEN AI Key, mail id and password in .env file.

```sh
OPENAI_API_KEY=<OPENAI_API_KEY>
MAIL_ACCOUNT_NAME=<your_maild_id>
MAIL_APP_PASSWORD=<your_maild_password>
```

# Usage

Run the Stream lit app using below code.
```sh
streamlit run app.py
```



