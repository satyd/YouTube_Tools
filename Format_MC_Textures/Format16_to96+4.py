from PIL import Image, ImageOps
import os

# Путь к папке с исходными изображениями
input_folder = "input"
# Путь к папке для сохранения обработанных изображений
output_folder = "output"

# Создаем папку для сохранения, если её нет
os.makedirs(output_folder, exist_ok=True)

# Новый размер после масштабирования (метод ближайшего соседа)
new_size = 96
# Финальный размер с рамкой
final_size = 100

# Проходим по всем файлам в папке
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Открываем изображение
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Масштабируем до 96x96 (ближайший сосед)
        img_resized = img.resize((new_size, new_size), Image.NEAREST)

        # Создаем новое изображение 100x100 с прозрачной рамкой
        img_final = Image.new("RGBA", (final_size, final_size), (0, 0, 0, 0))

        # Вставляем масштабированное изображение по центру
        offset = ((final_size - new_size) // 2, (final_size - new_size) // 2)
        img_final.paste(img_resized, offset)

        # Сохраняем результат
        output_path = os.path.join(output_folder, filename)
        img_final.save(output_path)

print("Обработка завершена!")