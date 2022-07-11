from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from tkinter import *
from tkinter import Tk, messagebox

chrome_path = '../intafollowbot/chromedriver.exe'


class InstaFollower:

    def __init__(self):
        service = Service(executable_path=chrome_path)
        self.driver = webdriver.Chrome(service=service)

    def login(self, username, password_login):
        instagram_link = 'https://www.instagram.com/accounts/login/'
        self.driver.get(instagram_link)
        sleep(2)
        user = self.driver.find_element(by=By.NAME, value='username')
        password = self.driver.find_element(by=By.NAME, value='password')
        user.send_keys(username)
        password.send_keys(password_login)
        button_login = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        button_login.click()
        sleep(5)

    def find_followers(self, user_search):
        instagram_link = 'https://www.instagram.com'
        self.driver.get(instagram_link + f'/{user_search}/followers/')
        sleep(5)
        scrollable_popup = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            sleep(2)

    def follow(self, qnt):
        user_follow_list = self.driver.find_elements(by=By.CSS_SELECTOR, value='li button')
        user_follow_list = user_follow_list[:qnt]
        for user in user_follow_list:
            try:
                user.click()
                sleep(1)
            except ElementClickInterceptedException:
                sleep(1)
                cancel_button = self.driver.find_element(by=By.CSS_SELECTOR, value='button._a9--._a9_1')
                cancel_button.click()


# ---------------------- ENGINE START -------------------------------

def start():
    user = username.get()
    senha = password.get()
    conta_alvo = user_target.get()
    qnt_contas = qnt_user_follow.get()
    if len(username_entry.get()) != 0 and len(password_entry.get()) != 0 and len(user_target_entry.get()) != 0 \
            and len(qnt_user_follow_entry.get()) != 0:
        insta = InstaFollower()
        insta.login(user, senha)
        insta.find_followers(conta_alvo)
        insta.follow(qnt_contas)
    else:
        messagebox.showinfo(title='Oops', message='Please make sure you have not left any fields empty.')


# ----------------------- READ ME ----------------------------------

def readme():
    answer_label.config(background='#E6E6FA')
    answer_label.config(text='\n      InstaFollow Bot\nO projeto cria um bot para entrar no intagram, e que entrará '
                             'em uma conta alvo '
                             '\nonde tentará seguir os seguidores da conta alvo, para engajamento da sua propria '
                             'conta.\n\n '
                             'Instruções: \n\n1 - Coloque seu email.\n2 - Insira sua senha(confidencial)\n3 - Insira '
                             'a conta alvo(digite a conta corretamente, pois poderá ir para outra conta) '
                             '\n4 - Coloque a quantidade de tentativas que o bot tentara fazer.\n\n\n'
                             ' Projeto em contrução, poderá haver falhas ainda 😅😅\n\n'
                             'Autor: Raylon Felipe')


# ----------------------- UI SEPUT ---------------------------

window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40, background='#E6E6FA')

canvas = Canvas(width=300, height=102, highlightthickness=0)
instagram_image = PhotoImage(file='../intafollowbot/instagram-logo2.png')
canvas.create_image(50, 50, image=instagram_image)
canvas.grid(row=0, column=1, pady=40)
canvas.config(background='#E6E6FA')

username_label = Label(text='Username: ')
username_label.grid(row=1, column=0)
username_label.config(background='#E6E6FA')

username = StringVar()
username_entry = Entry(textvariable=username)
username_entry.grid(row=1, column=1, ipadx=50)

password_label = Label(text='Password: ')
password_label.grid(row=2, column=0)
password_label.config(background='#E6E6FA')

password = StringVar()
password_entry = Entry(textvariable=password, show='*')
password_entry.grid(row=2, column=1, ipadx=50)

user_target_label = Label(text='User target: ')
user_target_label.grid(row=3, column=0)
user_target_label.config(background='#E6E6FA')

user_target = StringVar()
user_target_entry = Entry(textvariable=user_target)
user_target_entry.grid(row=3, column=1, ipadx=50)

qnt_user_follow_label = Label(text='How many users you want to follow: ')
qnt_user_follow_label.grid(row=4, column=0)
qnt_user_follow_label.config(background='#E6E6FA')

qnt_user_follow = IntVar()
qnt_user_follow_entry = Entry(textvariable=qnt_user_follow)
qnt_user_follow_entry.grid(row=4, column=1, ipadx=50)

init_button = Button(text='Start', command=start)
init_button.grid(row=5, column=1, pady=10)
init_button.config(width=25)

readme_button = Button(text='ReadMe', command=readme)
readme_button.grid(row=5, column=0, pady=10)
readme_button.config(width=25)

answer_label = Label(text='')
answer_label.grid(row=6, column=0, columnspan=2)

window.mainloop()
