import time
import pyperclip
import pyautogui
from pynput import keyboard
from pynput.keyboard import Controller, Key
import tkinter as tk

start_time = time.time()
current_flash_timers = []
flash_time_delta = 5
reduced_flash_time_delta = 4
reduced_flash_time_active = False

def flash_time(start_time, delta=0):
    current_time = time.time()
    remaining_time = 300 - (current_time - start_time) + delta
    if remaining_time <= 0:
        return "0:00"
    else:
        return time.strftime("%M:%S", time.gmtime(remaining_time))

def update_current_flash_timers(current_flash_timers, delta):
    for i in range(len(current_flash_timers)):
        current_flash_timers[i]["remaining_time"] -= delta
    return current_flash_timers

def remove_old_flash_timers(current_flash_timers):
    current_time = time.time()
    new_flash_timers = []
    for item in current_flash_timers:
        if item["remaining_time"] > (current_time - start_time):
            new_flash_timers.append(item)
    return new_flash_timers

def get_current_flash_timers_string(current_flash_timers):
    result = ""
    for item in current_flash_timers:
        result = result + item["spell"] + str(item["remaining_time"]) + " "
    return result

def remove_outdated_flash_timers():
    global current_flash_timers
    current_flash_timers = remove_old_flash_timers(current_flash_timers)

def write_to_chat():
    texto = ""
    for dicionario in current_flash_timers:
        texto += f"{dicionario['spell']} {dicionario['tempo_flash']} "
    print(texto)
    pyautogui.typewrite(texto)
    # pyautogui.press('enter')
    # time.sleep() # Espera 1 segundo antes de continuar para evitar a digitação acidental de outros caracteres

def on_press(key):
    global start_time, current_flash_timers, reduced_flash_time_active

    if key == keyboard.Key.esc:
        return False
    try:

        if key == keyboard.Key.f1:
            if reduced_flash_time_active:
                return False
            current_flash_timers = update_current_flash_timers(
                current_flash_timers, flash_time_delta)
            current_flash_timers = remove_old_flash_timers(
                current_flash_timers)
            # Novo requisito: copiar tempo de jogo atual + 5 para o CTRL + V
            if reduced_flash_time_active == True:
                time_in_game = int(time.time() - start_time) + 240
            else:
                time_in_game = int(time.time() - start_time) + 300
            horas = time_in_game // 60
            minutos = time_in_game % 60
            tempo = str(horas) + str(minutos).zfill(2)
            current_flash_timers.append(
                {"spell": "topf", "remaining_time": time_in_game, "tempo_flash": tempo})
            texto = ()
            for dicionario in current_flash_timers:
                texto += (dicionario['spell'], dicionario['tempo_flash'])
            texto = ' '.join(texto)
            pyperclip.copy(texto)

        elif key == keyboard.Key.f2:
            if reduced_flash_time_active:
                return False

            current_flash_timers = update_current_flash_timers(
                current_flash_timers, flash_time_delta)
            current_flash_timers = remove_old_flash_timers(
                current_flash_timers)
            if reduced_flash_time_active == True:
                time_in_game = int(time.time() - start_time) + 240
            else:
                time_in_game = int(time.time() - start_time) + 300
            horas = time_in_game // 60
            minutos = time_in_game % 60
            tempo = str(horas) + str(minutos).zfill(2)
            current_flash_timers.append(
                {"spell": "jgf", "remaining_time": time_in_game, "tempo_flash": tempo})
            texto = ()
            for dicionario in current_flash_timers:
                texto += (dicionario['spell'], dicionario['tempo_flash'])
            texto = ' '.join(texto)
            pyperclip.copy(texto)

        elif key == keyboard.Key.f3:
            if reduced_flash_time_active:
                return False

            current_flash_timers = update_current_flash_timers(
                current_flash_timers, flash_time_delta)
            current_flash_timers = remove_old_flash_timers(
                current_flash_timers)
            if reduced_flash_time_active == True:
                time_in_game = int(time.time() - start_time) + 240
            else:
                time_in_game = int(time.time() - start_time) + 300
            horas = time_in_game // 60
            minutos = time_in_game % 60
            tempo = str(horas) + str(minutos).zfill(2)
            current_flash_timers.append(
                {"spell": "midf", "remaining_time": time_in_game, "tempo_flash": tempo})
            texto = ()
            for dicionario in current_flash_timers:
                texto += (dicionario['spell'], dicionario['tempo_flash'])
            texto = ' '.join(texto)
            pyperclip.copy(texto)
        elif key == keyboard.Key.f4:
            if reduced_flash_time_active:
                return False

            current_flash_timers = update_current_flash_timers(
                current_flash_timers, flash_time_delta)
            current_flash_timers = remove_old_flash_timers(
                current_flash_timers)
            if reduced_flash_time_active == True:
                time_in_game = int(time.time() - start_time) + 240
            else:
                time_in_game = int(time.time() - start_time) + 300
            horas = time_in_game // 60
            minutos = time_in_game % 60
            tempo = str(horas) + str(minutos).zfill(2)
            current_flash_timers.append(
                {"spell": "adf", "remaining_time": time_in_game, "tempo_flash": tempo})
            texto = ()
            for dicionario in current_flash_timers:
                texto += (dicionario['spell'], dicionario['tempo_flash'])
            texto = ' '.join(texto)
            pyperclip.copy(texto)

        elif key == keyboard.Key.f5:
            if reduced_flash_time_active:
                return False

            current_flash_timers = update_current_flash_timers(
                current_flash_timers, flash_time_delta)
            current_flash_timers = remove_old_flash_timers(
                current_flash_timers)
            if reduced_flash_time_active == True:
                time_in_game = int(time.time() - start_time) + 240
            else:
                time_in_game = int(time.time() - start_time) + 300
            horas = time_in_game // 60
            minutos = time_in_game % 60
            tempo = str(horas) + str(minutos).zfill(2)
            current_flash_timers.append(
                {"spell": "supf", "remaining_time": time_in_game, "tempo_flash": tempo})
            texto = ()
            for dicionario in current_flash_timers:
                texto += (dicionario['spell'], dicionario['tempo_flash'])
            texto = ' '.join(texto)
            pyperclip.copy(texto)

        elif key == keyboard.Key.f6:
            if reduced_flash_time_active:
                # Novo requisito: desativar tempo reduzido se tecla 6 for pressionada novamente
                reduced_flash_time_active = False
                return False

            # current_flash_timers = update_current_flash_timers(current_flash_timers, reduced_flash_time_delta)
            # current_flash_timers = remove_old_flash_timers(current_flash_timers, start_time)

            # Novo requisito: ativar tempo reduzido
            reduced_flash_time_active = True

        elif key == keyboard.Key.enter:
            for dicionario in current_flash_timers:
                print(dicionario)
                horas = int(time.time() - start_time) // 60
                minutos = int(time.time() - start_time) % 60
                tempo = str(horas) + str(minutos).zfill(2)
                print(tempo)
                if (dicionario['tempo_flash']) <= tempo:
                    current_flash_timers.remove(dicionario)
                    texto = ()
                    for dic in current_flash_timers:
                        texto += (dic['spell'], dic['tempo_flash'])
                    texto = ' '.join(texto)
                    pyperclip.copy(texto)
        elif key == keyboard.Key.f7:
            write_to_chat()

    except AttributeError:
        pass
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# janela = tk.Tk()
# texto = tk.Label(janela, text='Olá mundo!')
# texto.pack()
# janela.mainloop()
