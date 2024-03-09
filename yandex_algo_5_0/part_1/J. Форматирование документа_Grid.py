import re


class DocumentElement:
    pass

class NewParagraph(DocumentElement):
    def __init__(self):
        pass

    def __repr__(self):
        return f"New Paragraph Element"

class Image(DocumentElement):
    def __init__(self, layout, width, height, dx=0, dy=0):
        self.layout = layout
        self.width = int(width)
        self.height = int(height)
        self.dx = int(dx) if 'dx' in locals() else 0
        self.dy = int(dy) if 'dy' in locals() else 0

    def __repr__(self):
        return f"Image: layout type = {self.layout}"

class Word(DocumentElement):
    def __init__(self, text, char_width):
        self.text = text
        self.char_width = char_width

    def __repr__(self):
        return f"Word: len = {len(self.text)}"

class DocumentGrid:
    def __init__(self, width, initial_height=100):
        self.width = width
        self.height = initial_height
        self.grid = [[None for _ in range(width)] for _ in range(initial_height)]
        self.current_line_height = 1
        self.cursor_x = 0
        self.cursor_y = 0

    def expand_grid(self, new_height):
        if new_height > self.height:
            for _ in range(new_height - self.height):
                self.grid.append([None for _ in range(self.width)])
            self.height = new_height

    def print_grid(self):
        for row in self.grid:
            for cell in row:
                if cell is None:
                    print('.', end='')  # Пустое пространство
                elif cell[0] == 'Word':
                    print(cell[1], end='')  # Слово
                elif cell[0] == 'Space':
                    print('S', end='')
                elif cell[0] == 'Image':
                    if cell[1] == 'embedded':
                        print('E', end='')  # Встроенное изображение
                    elif cell[1] == 'surrounded':
                        print('S', end='')  # Изображение с обтеканием
                    elif cell[1] == 'floating':
                        print('F', end='')  # Плавающее изображение
            print()  # Новая строка после завершения текущей строки сетки

    def place_word(self, word):
        word_length_px = len(word.text) * word.char_width
        space_width_px = word.char_width  # Ширина пробела равна ширине символа

        # Проверяем, поместится ли слово вместе с последующим пробелом в текущую строку
        if self.cursor_x + word_length_px > self.width:
            # Если слово не помещается, переносим его на новую строку
            self.cursor_x = 0
            self.cursor_y += self.current_line_height
            self.current_line_height = 1  # Сброс высоты строки
            self.expand_grid(self.cursor_y + 1)

        # Размещаем каждый символ слова
        for char in word.text:
            for i in range(word.char_width):
                self.grid[self.cursor_y][self.cursor_x + i] = ('Word', char)
            
            self.cursor_x += word.char_width

        # Проверяем, достаточно ли места для добавления пробела после слова
        if self.cursor_x + space_width_px <= self.width:
            for i in range(word.char_width):
                self.grid[self.cursor_y][self.cursor_x + i] = ('Space', ' ')
            self.cursor_x += space_width_px  # Добавляем пробел после слова

        # Если после добавления пробела достигнут конец строки, переходим на новую строку
        if self.cursor_x == self.width:
            self.cursor_x = 0
            self.cursor_y += self.current_line_height
            self.current_line_height = 1  # Сброс высоты строки
            self.expand_grid(self.cursor_y + 1)


    def place_image(self, image):
        # Убедимся, что сетка достаточно велика перед размещением изображения
        needed_height = self.cursor_y + image.height
        self.expand_grid(needed_height)

        if image.layout == 'embedded' or image.layout == 'surrounded':
            # Если изображение не помещается в оставшуюся часть строки, переходим на новую строку
            if self.cursor_x + image.width > self.width:
                self.cursor_x = 0  # Переход на новую строку
                self.cursor_y += self.current_line_height
                self.current_line_height = image.height  # Обновляем высоту текущей строки под изображение

            for i in range(image.height):
                for j in range(image.width):
                    # Убедимся, что мы не выходим за пределы текущей ширины сетки
                    current_x = self.cursor_x + j
                    if current_x < self.width:
                        self.grid[self.cursor_y + i][current_x] = ('Image', image.layout)
                    else:
                        # Прекращаем размещение изображения, если достигнут край сетки
                        break

            self.cursor_x += image.width
            if self.cursor_x >= self.width:
                # Если после размещения изображения достигнут край сетки, переходим на новую строку
                self.cursor_x = 0
                self.cursor_y += self.current_line_height
                self.current_line_height = 1  # Сбрасываем высоту строки после перехода

def parse_document(document, char_width):
    elements = []
    # Разделяем документ на абзацы
    paragraphs = document.split('\n\n')  # Два перевода строки подряд обозначают новый абзац
    for paragraph in paragraphs:
        parts = re.split(r'(\(image [^\)]+\))', paragraph)
        for part in parts:
            part = part.strip()
            if part.startswith("(image"):
                # Извлекаем атрибуты из строки
                attrs = {match[0]: match[1] for match in re.findall(r'(\w+)=(\w+)', part)}
                if all(key in attrs for key in ['layout', 'width', 'height']):
                    elements.append(Image(layout=attrs['layout'], width=attrs['width'], height=attrs['height'], dx=attrs.get('dx', 0), dy=attrs.get('dy', 0)))
                else:
                    print("Ошибка: не все атрибуты рисунка указаны.")
            elif part:  # Проверяем, что часть не пустая
                words = part.split()
                for word in words:
                    elements.append(Word(text=word, char_width=char_width))
        elements.append(NewParagraph())  # Добавляем элемент нового абзаца после каждого абзаца

    # Удаляем последний добавленный элемент NewParagraph, если он есть
    if elements and isinstance(elements[-1], NewParagraph):
        elements.pop()

    print(elements)
    return elements



if __name__ == "__main__":
    # Reading from the file
    with open("input.txt", "r") as reader:
        w, h, c = map(int, reader.readline().strip().split(" "))
        document = reader.read().strip()

    grid = DocumentGrid(w, 20)  # Сетка шириной 100 и высотой 20


    elements = parse_document(document, c)
    for el in elements:
        if isinstance(el, Word):
            grid.place_word(el)
    
    grid.print_grid()
    
    #positions = layout_document(elements, w, h, c)
    #print(positions)
    ans = "f"
    # Writing to the file
    with open("output.txt", "w") as file:
        file.write(ans)
