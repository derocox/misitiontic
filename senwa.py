import pyautogui
import webbrowser
from time import sleep

print("***************")
print("** ¿Donde deseas envia el mensaje? **")
print("**                                 **")
print("* 1. Número no registrado o contacto  *")
print("* 2. Grupo                            *")
print("**                                 **")
print("***************")

respuesta = int(input("Escribe tú elección: "))


if respuesta == 1:
	
	cod = 57
	num = pyautogui.prompt(text='Escriba el número al que va a enviar el mensaje: ', title='Número destino' , default='')
	msj = pyautogui.prompt(text='Escriba el Mensaje a enviar: ', title='Mensaje a enviar.' , default='')
	url = "https://web.whatsapp.com/send?phone=+"

	webbrowser.open(f"{url}{cod}{num}")
	sleep(10)   #Tiempo de envio del mensaje

	pyautogui.typewrite(f"{msj}")
	pyautogui.confirm(text=f'Quieres enviar el mensaje a: {num} ?',
            title='Confirmación de envio.',
            buttons=['OK', 'Cancel'])

	pyautogui.press("enter")
	pyautogui.alert("Mensaje enviado correctamente.")

elif respuesta == 2:

	IdGrupo = pyautogui.prompt(text='Escriba el ID del grupo a enviar el mensaje: ', title='ID Grupo' , default='')
	urlGroup = "https://web.whatsapp.com/accept?code="

	webbrowser.open(f"{urlGroup}{IdGrupo}")
	sleep(10)   #Tiempo de envio del mensaje

	with open("Spam.txt", "r") as file:
		for line in file:
			pyautogui.typewrite(line)
			pyautogui.press("enter")

else:
	print("La eleción no es la correcta.")