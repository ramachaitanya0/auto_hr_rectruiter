import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()
mail_password = os.getenv("MAIL_APP_PASSWORD")
sender_mail=os.getenv("MAIL_ACCOUNT_NAME")
def get_hr_message(candidate_name:str,HR_Name :str,job_position:str,test_link:str):
    message = f""" 
    
    Dear {candidate_name},
    
    I hope this email finds you well. My name is {HR_Name}, and I am a recruiter at TVS Motors. We recently came across your impressive profile and were truly impressed with your skills and experience. Your background caught our attention, and we believe you could be a fantastic fit for an exciting opportunity we currently have available.
    
    At TVS Motors, we are committed to fostering a dynamic and innovative work environment. We are currently looking for individuals who share our passion and are eager to contribute their expertise to a growing team.
    
    Position: {job_position}
    Location: Bangalore
    Company: TVS Motors
    
    To give you a better insight into the role and to assess your skills, we have prepared a brief online test. This test is designed to evaluate your skills and provide us with a better understanding of how your experience aligns with the requirements of the position.
    
    Please find the test link {test_link}. The test should take approximately 1 hour to complete. We encourage you to take your time and showcase your skills to the best of your ability.
    
    Instructions:
    
    Click on the test link provided.
    Complete the test within the specified time frame.
    Ensure a stable internet connection during the test.
    If you encounter any technical issues, please reach out to us at hr@tvsmotor.com.
    The deadline for completing the test is two days. We kindly ask that you complete the assessment at your earliest convenience.
    
    We understand the value of your time, and we appreciate your willingness to participate in our hiring process. Successful candidates will proceed to the next stage, where we will have the opportunity to discuss your application in more detail.
    Thank you for considering TVS Motors as the next step in your career journey. We look forward to reviewing your assessment and potentially welcoming you to our team.
    
    Best regards,
    HR, TVS Motors
    """
    return  message

def send_mail(reciever_mail:str,job_position:str,candidate_name:str,HR_Name:str,test_link:str) :
    message = get_hr_message(candidate_name, HR_Name, job_position, test_link)
    msg = MIMEMultipart()
    msg['From'] = os.getenv("MAIL_ACCOUNT_NAME")
    msg['To'] = reciever_mail
    msg['Subject'] = f"Screening Test for {job_position} Position at TVS Motors"
    msg.attach(MIMEText(message, 'plain'))
    print(f"message is {msg}")

    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login(sender_mail, mail_password)
    server.sendmail(sender_mail, reciever_mail, msg.as_string())
    server.close()
    print(f"Email sent to {reciever_mail}")
    return True