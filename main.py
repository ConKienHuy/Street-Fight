import pygame
import sys
import socket
import gameplay
from button import Button
import traceback

pygame.init()
systemInfo = pygame.display.Info()
SCREEN_WIDTH = systemInfo.current_w
SCREEN_HEIGHT = systemInfo.current_h
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption(f"Street Fight")
BG = pygame.image.load("assets/bg.jpg")

def get_font(size):
    return pygame.font.Font("assets/fonts/Atop-R99O3.ttf", size)

name_input = []  # Khởi tạo name_input như một list
ready_count = 0

def start_game1():
    global systemInfo
    screen = pygame.display.set_mode((systemInfo.current_w, systemInfo.current_h))
    pygame.display.set_caption("Stress Fight")
    bg_image = pygame.image.load("assets/bggame.jpg")
    screen.blit(bg_image, (0,0))

def start_game(client_socket, player_name):
    gameplay.run(client_socket, player_name)

def play():
    global name_input

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        bg = pygame.image.load("assets/play.jpg")
        SCREEN.blit(bg, (0, 0))

        PLAY_TEXT = get_font(36).render("Enter Your Name: " + ''.join(name_input), True, (255, 255, 255))
        PLAY_RECT = PLAY_TEXT.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        OPTIONS_PLAY = Button(pos=(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT * 20 // 27),
                              text_input="CONTINUE", font=get_font(40), base_color=(255, 255, 255), hovering_color=(0, 255, 0))
        PLAY_BACK = Button(pos=(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT * 20 // 27), 
                            text_input="BACK", font=get_font(40), base_color=(255, 255, 255), hovering_color=(0, 255, 0))
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        OPTIONS_PLAY.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        OPTIONS_PLAY.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                elif OPTIONS_PLAY.checkForInput(PLAY_MOUSE_POS):
                    # Kết nối đến server
                    connect_to_server(''.join(name_input))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    name_input = name_input[:-1]
                elif event.key == pygame.K_RETURN:
                    # Làm gì đó với tên đã nhập, như lưu vào biến
                    print("Player name:", ''.join(name_input))
                    # Gửi ready signal đến server khi nhấn Enter
                    connect_to_server(''.join(name_input))
                else:
                    name_input.append(event.unicode)

        pygame.display.update()

def connect_to_server(player_name):
    # Kết nối đến server
    HOST = "192.168.43.218"
    PORT = 5555

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        client_socket.send(player_name.encode())
        print("Connected to the server as Player")
        start_game(client_socket, player_name)
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, (182, 143, 64))
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 1 // 5))

        PLAY_BUTTON = Button(pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 5), 
                            text_input="PLAY", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        QUIT_BUTTON = Button(pos=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 4 // 5), 
                            text_input="QUIT", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
