from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from telegram.ext import Updater, CommandHandler
import time

# Función que maneja el comando /check_images
def check_images(update, context):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Modo headless para evitar abrir el navegador
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="ruta_al_chromedriver", options=options)

    try:
        # Paso 1: Acceder a la página de inicio de sesión
        driver.get("https://onedrive.live.com/login/")

        # Paso 2: Ingresar credenciales
        email_field = driver.find_element(By.NAME, "loginfmt")
        email_field.send_keys("alpiquette@hotmail.com")
        email_field.send_keys(Keys.RETURN)
        time.sleep(2)

        password_field = driver.find_element(By.NAME, "passwd")
        password_field.send_keys("Marcelline0607")
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)

        # Paso 3: Verificar si hay imágenes en OneDrive
        driver.get("https://onedrive.live.com/")
        time.sleep(5)

        files = driver.find_elements(By.CSS_SELECTOR, "div[data-type='image']")
        if files:
            result = f"Se encontraron {len(files)} imágenes:\n"
            result += "\n".join([file.text for file in files])
        else:
            result = "No se encontraron imágenes."

        # Enviar el resultado al usuario
        update.message.reply_text(result)
    except Exception as e:
        update.message.reply_text(f"Error: {e}")
    finally:
        driver.quit()

# Configuración del bot
def main():
    updater = Updater("TOKEN_DEL_BOT", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("check_images", check_images))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
      
