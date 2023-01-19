import smtplib
from dotenv import dotenv_values
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


config = dotenv_values("variables.env")


SMTP_HOST = config['SMTP_HOST']
SMTP_PORT = config['SMTP_PORT']
SMTP_EMAIL = config['SMTP_EMAIL']
SMTP_PASSWORD = config['SMTP_PASSWORD']
MY_NAME = config['MY_NAME']
TITLE = config['TITLE']


EMAILS = [
    ('senador MARCOS DO VAL', 'sen.marcosdoval@senado.leg.br'),
    ('senador NELSINHO TRAD', 'sen.nelsinhotrad@senado.leg.br'),
    ('senador PLÍNIO VALÉRIO', 'sen.pliniovalerio@senado.leg.br'),
    ('senador IZALCI LUCAS', 'sen.izalcilucas@senado.leg.br'),
    ('senador MARCIO BITTAR', 'sen.marciobittar@senado.leg.br'),
    ('senador VANDERLAN CARDOSO', 'sen.vanderlancardoso@senado.leg.br'),
    ('senadora SORAYA THRONICKE', 'sen.sorayathronicke@senado.leg.br'),
    ('senador JAYME CAMPOS', 'sen.jaymecampos@senado.leg.br'),
    ('senadora MARGARETH BUZETTI', 'sen.margarethbuzetti@senado.leg.br'),
    ('senadora DANIELLA RIBEIRO', 'sen.daniellaribeiro@senado.leg.br'),
    ('senador ROMARIO', 'sen.romario@senado.leg.br'),
    ('senador FERNANDO DUEIRE', 'sen.fernandodueire@senado.leg.br'),
    ('senador ORIOVISTO GUIMARAES', 'sen.oriovistoguimaraes@senado.leg.br'),
    ('senador CHICO RODRIGUES', 'sen.chicorodrigues@senado.leg.br'),
    ('senador MECIAS DE JESUS', 'sen.meciasdejesus@senado.leg.br'),
    ('senadora IVETE DA SILVEIRA', 'sen.ivetedasilveira@senado.leg.br'),
    ('senador ALESSANDRO VIEIRA', 'sen.alessandrovieira@senado.leg.br'),
    ('senadora MARA GABRILLI', 'sen.maragabrilli@senado.leg.br'),
    ('senador EDUARDO GOMES', 'sen.eduardogomes@senado.leg.br'),
    ('senador LUCAS BARRETO', 'sen.lucasbarreto@senado.leg.br'),
    # traidores
    ('senador SERGIO PETECAO', 'sen.sergiopetecao@senado.leg.br'),
    ('senador RENAN CALHEIROS', 'sen.renancalheiros@senado.leg.br'),
    ('senador EDUARDO BRAGA', 'sen.eduardobraga@senado.leg.br'),
    ('senador ANGELO CORONEL', 'sen.angelocoronel@senado.leg.br'),
    ('senador OTTO ALENCAR', 'sen.ottoalencar@senado.leg.br'),
    ('senador CID GOMES', 'sen.cidgomes@senado.leg.br'),
    ('senadora LEILA BARROS', 'sen.leilabarros@senado.leg.br'),
    ('senador GIORDANO', 'sen.giordano@senado.leg.br'),
    ('senador JORGE KAJURU', 'sen.jorgekajuru@senado.leg.br'),
    ('senadora ELIZIANE GAMA', 'sen.elizianegama@senado.leg.br'),
    ('senador WEVERTON', 'sen.wevertonrocha@senado.leg.br'),
    ('senador JADER BARBALHO', 'sen.jaderbarbalho@senado.leg.br'),
    ('senador MARCELO CASTRO', 'sen.marcelocastro@senado.leg.br'),
    ('senador FLAVIO ARNS', 'sen.flavioarns@senado.leg.br'),
    ('senador CONFUCIO MOURA', 'sen.confuciomoura@senado.leg.br'),
    ('senador IRAJÁ', 'sen.iraja@senado.leg.br'),
    ('senador VENEZIANO VITAL DO REGO', 'sen.venezianovitaldorego@senado.leg.br'),
    ('senadora ZENAIDE MAIA', 'sen.zenaidemaia@senado.leg.br'),
]


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


if __name__ == '__main__':
    s = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    s.starttls()
    s.login(SMTP_EMAIL, SMTP_PASSWORD)

    for name, email in EMAILS:
        msg = MIMEMultipart()
        message_template = read_template('templates/message.txt')
        message = message_template.substitute(MY_NAME=MY_NAME.title(), NAME=name.title())

        msg['From'] = SMTP_EMAIL
        msg['To'] = email
        msg['Subject'] = TITLE

        msg.attach(MIMEText(message, 'plain'))

        s.send_message(msg)

        del msg

print("FIMMMMMMMMMMMM")