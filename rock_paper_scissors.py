import pygame
import random
import sys

pygame.init()

#Музыка
sound = pygame.mixer.Sound('Goodkill Music - Overcooked! Penne For Your Thoughts Gameplay Version.mp3')

sound.play()


# Размеры окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Камень Ножницы Бумага")

# Загрузка изображений (замените пути на свои)
rock_img = pygame.image.load('rock.png')
scissors_img = pygame.image.load('scissors.png')
paper_img = pygame.image.load('paper.png')

# Масштабируем изображения
size = (100, 100)
rock_img = pygame.transform.scale(rock_img, size)
scissors_img = pygame.transform.scale(scissors_img, size)
paper_img = pygame.transform.scale(paper_img, size)

# Позиции для кнопок и их состояния
positions = {
    'камень': [50, 200],
    'ножницы': [250, 200],
    'бумага': [450, 200]
}

choices_images = {
    'камень': rock_img,
    'ножницы': scissors_img,
    'бумага': paper_img
}

font = pygame.font.SysFont(None, 36)

def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

clock = pygame.time.Clock()
user_choice = None
computer_choice = None
result_text = ""

# Счетчики побед и поражений
score_wins = 0
score_losses = 0
score_draw = 0

# Для анимации кнопок: создадим словарь с состояниями
buttons_state = {
    'камень': {'rect': None, 'hovered': False},
    'ножницы': {'rect': None, 'hovered': False},
    'бумага': {'rect': None, 'hovered': False}
}

# Размеры для анимации (увеличение при наведении)
normal_size = (100, 100)
hover_size = (120, 120)  # увеличиваем на 20 пикселей

running = True
while running:
    screen.fill((255, 255, 255))
    
    mouse_pos = pygame.mouse.get_pos()
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            # Проверка клика по кнопкам выбора
            for choice in positions:
                rect_obj = buttons_state[choice]['rect']
                if rect_obj and rect_obj.collidepoint(x,y):
                    user_choice = choice
                    computer_choice = get_computer_choice()
                    result_text = determine_winner(user_choice, computer_choice)
                    # Обновляем счетчики побед/проигрышей
                    if result_text == "Вы выиграли!":
                        score_wins +=1
                    elif result_text == "Компьютер выиграл!":
                        score_losses += 1
                    elif result_text == 'Ничья!':
                        score_draw += 1

    # Отрисовка кнопок с анимацией наведения
    for choice in positions:
        pos_x, pos_y = positions[choice]
        hovered = False
        
        rect_obj = buttons_state[choice]['rect']
        if rect_obj is None:
            rect_obj = pygame.Rect(pos_x, pos_y, normal_size[0], normal_size[1])
            buttons_state[choice]['rect'] = rect_obj
        
        # Проверка наведения мыши на кнопку
        if rect_obj.collidepoint(mouse_pos):
            hovered=True
        
        buttons_state[choice]['hovered'] = hovered
        
        # Выбор размера в зависимости от наведения (анимация)
        current_size= hover_size if hovered else normal_size
        
        # Центрируем изображение по центру кнопки для плавной анимации
        center_x= rect_obj.centerx
        center_y= rect_obj.centery
        
        # Создаем новое изображение с нужным размером для эффекта масштабирования
        img= choices_images[choice]
        scaled_img=pygame.transform.scale(img,current_size)
        
        # Вычисляем позицию так чтобы изображение оставалось по центру кнопки при изменении размера
        img_rect= scaled_img.get_rect(center=(center_x, center_y))
        
        screen.blit(scaled_img, img_rect.topleft)

        # Обновляем прямоугольник для следующей итерации (чтобы учитывать изменение размера)
        buttons_state[choice]['rect']=img_rect

    # Отображение выбранных вариантов и результата после выбора
    if user_choice:
        user_text= font.render(f"Вы: {user_choice}", True,(0,0,0))
        comp_text= font.render(f"Компьютер: {computer_choice}", True,(0,0,0))
        
        if result_text== "Вы выиграли!":
            color= (0,255,0)
        elif result_text== "Компьютер выиграл!":
            color= (255,0,0)
        else:
            color= (255,165,0)

        result_rendered= font.render(result_text , True,color)

        score_text= font.render(f"Побед: {score_wins}   Проигрышей: {score_losses} Ничьих: {score_draw}", True,(205,133 ,63))
        
        screen.blit(user_text,(50 ,20))
        screen.blit(comp_text,(50 ,60))
        screen.blit(result_rendered,(50 ,100))
        screen.blit(score_text,(50 ,140))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()