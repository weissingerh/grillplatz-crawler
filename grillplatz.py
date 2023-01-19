from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import bs4, requests, re, smtplib

getPage = requests.get('https://www.wien.gv.at/amtshelfer/umwelt/wasserbau/donauinsel/grillplatzreservierung.html')
getPage.raise_for_status()

html = bs4.BeautifulSoup(getPage.text, 'html.parser')

noReservations = html.find_all(string=re.compile('Sie erfahren auf dieser Webseite, sobald Reservierungen wieder möglich sind.'))

h2 = html.find_all('h2', class_="vie-ahs-f")[0]
nextSiblingIsNotH2 = (h2.find_next_sibling()['class'][0] != 'vie-ahs-zi')

message = MIMEMultipart()

if (nextSiblingIsNotH2):
    text = 'https://www.wien.gv.at/amtshelfer/umwelt/wasserbau/donauinsel/grillplatzreservierung.html'
    message['Subject'] = 'GO GO GO GO GPR verfuegbar!'
    message['To'] = 'EMAIL'
else:
    text = ''
    message['Subject'] = 'Wieder keine GPR :('
    message['To'] = 'EMAIL'

message.attach(MIMEText(text,'plain'))

# conn = smtplib.SMTP('smtpServer', 587)
conn.ehlo()
conn.starttls()
# conn.login('email','password')
# conn.sendmail('email', message['To'], message.as_string())
conn.quit()