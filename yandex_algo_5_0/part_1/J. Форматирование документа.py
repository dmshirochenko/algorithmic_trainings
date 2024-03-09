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

class LineFragment:
    def __init__(self, start_x, end_x, height):
        self.start_x = start_x
        self.end_x = end_x
        self.height = height

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

def layout_document(elements, page_width, line_height, char_width):
    x, y = 0, 0
    current_line_height = line_height
    positions = []  # Список для хранения координат рисунков
    space_width = char_width  # Ширина пробела равна ширине символа

    for el in elements:
        if isinstance(el, Word):
            word_width = len(el.text) * char_width
            # Учитываем пробел перед словом, если оно не первое в строке
            if x + word_width + space_width > page_width:
                x = 0  # Начинаем новую строку
                y += current_line_height
                current_line_height = line_height
            elif x > 0:  # Если не начало строки, добавляем пробел
                x += space_width
            x += word_width  # Добавляем слово
        
        elif isinstance(el, Image):
            if el.layout in ['embedded', 'surrounded']:
                if x + el.width > page_width:
                    x = 0
                    y += current_line_height
                    current_line_height = line_height
                if el.layout == 'embedded':
                    current_line_height = max(current_line_height, el.height)
                    positions.append((x, y))
                elif el.layout == 'surrounded':
                    # Обработка surrounded требует более сложной логики, здесь упрощённо
                    positions.append((x, y))
                    # Необходимо добавить логику для изменения высоты строк и разбиения на фрагменты
                x += el.width
            
            elif el.layout == 'floating':
                floating_x = max(0, x + el.dx)  # Убедимся, что рисунок находится в пределах страницы
                floating_y = y + el.dy
                positions.append((floating_x, floating_y))
                # Для floating рисунков не изменяем x, y документа
        
        elif isinstance(el, NewParagraph):
            x = 0  # Начинаем новый абзац
            y += current_line_height + line_height  # Добавляем дополнительный отступ для абзаца
            current_line_height = line_height

    return positions

# Reading from the file
with open("input.txt", "r") as reader:
    w, h, c = map(int, reader.readline().strip().split(" "))
    document = reader.read().strip()


elements = parse_document(document, c)
positions = layout_document(elements, w, h, c)
print(positions)
ans = "f"
# Writing to the file
with open("output.txt", "w") as file:
    file.write(ans)
