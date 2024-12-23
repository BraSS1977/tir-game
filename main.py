import pygame
import random
import os

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Загрузка и установка заголовка и иконки
pygame.display.set_caption("Игра Тир")
try:
    icon = pygame.image.load("image/tir.jpg")
    pygame.display.set_icon(icon)
except pygame.error as e:
    print(f"Ошибка загрузки иконки: {e}")

# Загрузка изображения мишени
try:
    target_img = pygame.image.load("image/target.jpg")
except pygame.error as e:
    print(f"Ошибка загрузки мишени: {e}")

# Задание размера мишени
TARGET_WIDTH = 100  # Задайте ширину мишени здесь
TARGET_HEIGHT = 100  # Задайте высоту мишени здесь


# Функция для изменения размера мишени
def resize_target_image(width, height):
    return pygame.transform.scale(target_img, (width, height))


# Изменение размера мишени
target_img = resize_target_image(TARGET_WIDTH, TARGET_HEIGHT)

# Изначальное случайное размещение цели
target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

# Случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    # Заполнение фона цветом
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Проверка нажатия кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (target_x <= mouse_x <= target_x + TARGET_WIDTH) and (target_y <= mouse_y <= target_y + TARGET_HEIGHT):
                print("Мишень поражена!")
                # Перемещение мишени на случайную позицию
                target_x = random.randint(0, SCREEN_WIDTH - TARGET_WIDTH)
                target_y = random.randint(0, SCREEN_HEIGHT - TARGET_HEIGHT)

    # Отрисовка мишени
    screen.blit(target_img, (target_x, target_y))

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()