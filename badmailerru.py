#CODED BY CMD
import smtplib
import time

#Func for sending email PLEASE DONT CHANGE THE EMAIL PASSWORD! I`LL BECANE UR IP AND DDoS U!
def sendgoogle(message, target):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('safetyserviceofgogle@gmail.com','dontchangeplease')
    print("Удачно залогинился");time.sleep(3)
    smtpObj.sendmail('safetyserviceofgogle@gmail.com',target,message)
    print("Письмо отправлено!")
    smtpObj.quit()

#FUNC FOR THE EMAIL CONTENT
def mechanism():
    print(" ______      ___     ______                           ")
    print("|      \   /     \  | _____\                          ")
    print("| By    | |       | |       |    _  _    _    _  _    ____   ___ ")
    print("|       | | v.1.0 | |       |   | \/ |  / \   |  |   |___ | | __|         ")
    print("|      /  |  ___  | |       |   |    | /___\  |  |   |      |\                " )
    print("|      \  | |   | | |       |   |    |/     \ |  |__||____| | \                       ")
    print("| CMD   | | |   | | | _____ |                                                       ")
    print("|_______| |_|   |_| |______/                                                          ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<                        ")    
    target = input("E-Mail жертвы: ")
    message = input("Сообщение письма, для следущей строки напиши ENTER: ")
    while True:
        if message.__contains__("ENTER"):
            message += ("\n")
            message = message.replace("ENTER", "")
            print (message)
            message += input("Следущая строка: ")
        else:
            print (message)
            sure = input("Это то что ты хочешь отправить? д/н: ")
            if sure == "д":
                sendgoogle(message, target)
            else:
                print("Неправильно! Запусти программу еще раз!")



print(" ______      ___     ______                           ")
print("|      \   /     \  | _____\                          ")
print("| By    | |       | |       |    _  _    _    _  _    ____   ___ ")
print("|       | | v.1.0 | |       |   | \/ |  / \   |  |   |___ | | __|         ")
print("|      /  |  ___  | |       |   |    | /___\  |  |   |      |\                " )
print("|      \  | |   | | |       |   |    |/     \ |  |__||____| | \                       ")
print("| CMD   | | |   | | | _____ |                                                       ")
print("|_______| |_|   |_| |______/                                                          ")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<                        ")

print("Это BADMAIL by CMD. С помощью этой программы ты сможешь отправлять \nфейковые эл.письма от safetyserviceofgogle@gmail.com")
print("ВНИМАНИЕ! РАЗРАБОТЧИК НЕ НЕСЕТ ОТВЕТСТВЕННОСТИ ЗА ВАШИ ДЕЙСТВИЯ!)
print("ИСПОЛЬЗУЙ НА СВОЙ СТРАХ И РИСК")
safe = input("Ты согласен со всеми рисками? [д]/[н]: ")
if safe == "д":
    mechanism()
else:
    print(safe)

