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
        self.dx = int(dx) if "dx" in locals() else 0
        self.dy = int(dy) if "dy" in locals() else 0

    def __repr__(self):
        return f"Image: layout type = {self.layout} width {self.width} height {self.height} dx {self.dx} dy {self.dy}"


class Word(DocumentElement):
    def __init__(self, text, char_width):
        self.text = text
        self.char_width = char_width
        self.layout = None

    def __repr__(self):
        return f"Word: len = {len(self.text)}"


class DocumentGrid:
    def __init__(self, width, initial_height, line_height, char_width):
        self.width = width
        self.height = initial_height
        self.line_height_default = line_height
        self.line_height = line_height
        self.char_width = char_width
        self.grid = [[None for _ in range(width)] for _ in range(initial_height)]
        self.cursor_x = 0
        self.cursor_y = 0
        self.max_y = 0
        self.image_coord = []
        # floating elements
        self.is_floating_last_inserted = False
        self.floating_cursor_x = 0
        self.floating_cursor_y = 0
        # todo
        self.is_cursor_moved_cause_of_end_line = False
        self.cursor_x_before_cause_of_end_line = 0
        self.cursor_y_before_cause_of_end_line = 0

    def expand_grid(self, new_height):
        if new_height > self.height:
            for _ in range(new_height - self.height):
                self.grid.append([None for _ in range(self.width)])
            self.height = new_height

    def ensure_grid_size(self, x, y):
        # Убедимся, что сетка достаточно велика для размещения символа
        while y >= len(self.grid):
            self.expand_grid(y + 1)
        while x >= len(self.grid[0]):
            for row in self.grid:
                row.append(None)

    def print_grid(self):
        for row in self.grid:
            for cell in row:
                if cell == "." or cell is None:
                    print(".", end="")  # Пустое пространство
                elif cell[0] == "Word":
                    print(cell[1], end="")  # Слово
                elif cell[0] == "Space":
                    print("_", end="")
                elif cell[0] == "Image":
                    if cell[1] == "embedded":
                        print("E", end="")  # Встроенное изображение
                    elif cell[1] == "surrounded":
                        print("S", end="")  # Изображение с обтеканием
                    elif cell[1] == "floating":
                        print("F", end="")  # Плавающее изображение
            print()  # Новая строка после завершения текущей строки сетки

    def is_place_empty(self, x, y, adjusted_width, height):
        for x_offset in range(adjusted_width):
            for y_offset in range(height):
                if x + x_offset >= self.width or y + y_offset >= len(self.grid):
                    return False  # За пределами сетки, считаем как занятое место
                if self.grid[y + y_offset][x + x_offset] is not None:
                    return False  # Место занято
        return True

    def find_free_space_in_line(self, element, start_x, y, width, height):
        for x in range(start_x, self.width):
            if start_x != 0 and self.grid[y][x - 1] == ("Image", "surrounded") and (element.layout != "surrounded"):
                adjusted_width = width - self.char_width  # Уменьшаем требуемую ширину
            else:
                adjusted_width = width
            if self.is_place_empty(x, y, adjusted_width, height):
                return x  # Возвращаем начальную позицию свободного места
        return None  # Свободное место не найдено, нужен переход на новую строку

    def check_and_add_line_if_last_and_no_E(self, current_x, line_number):
        # Проверяем, что номер строки находится в пределах существующей сетки
        contains_E = False
        if 0 <= line_number < len(self.grid):
            for i in range(current_x, len(self.grid[line_number])):
                cell = self.grid[line_number][i]
                if cell is not None and cell[0] == "Image" and cell[1] == "embedded":
                    contains_E = True
                    break
            if not contains_E and line_number == len(self.grid) - 1:
                self.expand_grid(self.height + self.line_height_default)
                contains_E = False
        else:
            self.expand_grid(self.height + self.line_height_default)

        return contains_E

    def place_paragraph(self, word):
        self.cursor_x = 0
        self.cursor_y = self.max_y
        self.line_height = self.line_height_default
        self.is_floating_last_inserted = False
        self.is_cursor_moved_cause_of_end_line = False
        self.expand_grid(self.cursor_y + self.line_height_default)
        self.max_y = max(self.max_y, self.cursor_y + self.line_height_default)

    def place_floating_image(self, el):
        if self.is_floating_last_inserted:
            new_x = self.floating_cursor_x + el.dx
            new_y = self.floating_cursor_y + el.dy
        elif self.is_cursor_moved_cause_of_end_line:
            new_x = self.cursor_x_before_cause_of_end_line + el.dx
            new_y = self.cursor_y_before_cause_of_end_line + el.dy
        else:
            new_x = self.cursor_x + el.dx
            new_y = self.cursor_y + el.dy

        # Проверяем, не выходит ли рисунок за левую границу страницы
        if new_x < 0:
            new_x = 0  # Смещаем вправо, чтобы совпадал с левой границей страницы

        # Проверяем, не выходит ли рисунок за правую границу страницы
        if new_x + el.width > self.width:
            new_x = self.width - el.width  # Смещаем влево, чтобы совпадал с правой границей страницы

        self.image_coord.append((new_x, new_y))

        self.is_floating_last_inserted = True
        self.floating_cursor_x = new_x + el.width
        self.floating_cursor_y = new_y

        self.is_cursor_moved_cause_of_end_line = False

    def place_word(self, word):
        while True:
            # Рассчитываем ширину, необходимую для слова с учетом пробела перед ним, если это не начало строки
            space_width = self.char_width if self.cursor_x > 0 else 0
            word_length_px = len(word.text) * self.char_width + space_width
            self.expand_grid(self.cursor_y + self.line_height)

            new_cursor_x = self.find_free_space_in_line(
                word, self.cursor_x, self.cursor_y, word_length_px, self.line_height
            )
            if new_cursor_x is not None:
                self.cursor_x = new_cursor_x
                break
            else:
                # Если не хватает места, переходим на новую строку
                space_width = 0
                self.cursor_x = 0
                self.cursor_y += self.line_height
                self.line_height = self.line_height_default
                self.expand_grid(self.cursor_y + self.line_height)

        # Добавляем пробел перед словом, если это не начало строки
        if space_width > 0:
            if self.grid[self.cursor_y][self.cursor_x - 1] != ("Image", "surrounded"):
                for x_offset in range(self.char_width):
                    for y_offset in range(self.line_height):
                        x_pos = self.cursor_x + x_offset
                        y_pos = self.cursor_y + y_offset
                        self.ensure_grid_size(x_pos, y_pos)
                        self.grid[y_pos][x_pos] = ("Space", "_")
                self.cursor_x += self.char_width  # Сдвигаем курсор на ширину пробела

        # Размещаем слово
        for char in word.text:
            for x_offset in range(self.char_width):
                for y_offset in range(self.line_height):
                    x_pos = self.cursor_x + x_offset
                    y_pos = self.cursor_y + y_offset
                    self.ensure_grid_size(x_pos, y_pos)
                    self.grid[y_pos][x_pos] = ("Word", char)
            self.cursor_x += self.char_width  # Сдвигаем курсор на ширину символа

        self.max_y = max(self.max_y, self.cursor_y + self.line_height)
        self.is_floating_last_inserted = False
        self.is_cursor_moved_cause_of_end_line = False

        # Проверяем, нужно ли перейти на новую строку после размещения слова
        if self.cursor_x >= self.width:
            self.is_cursor_moved_cause_of_end_line = True
            self.cursor_x_before_cause_of_end_line = self.cursor_x
            self.cursor_y_before_cause_of_end_line = self.cursor_y

            self.cursor_x = 0
            self.cursor_y += self.line_height
            self.line_height = self.line_height_default
            self.expand_grid(self.cursor_y + self.line_height_default)

    def place_image(self, image):
        # Рассчитываем ширину, необходимую для слова с учетом пробела перед ним, если это не начало строки
        if image.layout == "embedded" or image.layout == "surrounded":
            while True:
                space_width = self.char_width if (image.layout == "embedded" and self.cursor_x > 0) else 0
                image_length_px = image.width + space_width
                self.expand_grid(self.cursor_y + image.height)
                # Проверяем, поместится ли изобрадение с пробелом (если он нужен) в текущей строке, и ищем свободное место
                new_cursor_x = self.find_free_space_in_line(
                    image, self.cursor_x, self.cursor_y, image_length_px, image.height
                )
                if new_cursor_x is not None:
                    self.cursor_x = new_cursor_x
                    break
                else:
                    # Если не хватает места, переходим на новую строку
                    space_width = 0
                    self.cursor_x = 0
                    self.cursor_y += self.line_height
                    self.line_height = self.line_height_default
                    self.expand_grid(self.cursor_y + image.height)

            if space_width > 0:
                if self.grid[self.cursor_y][self.cursor_x - 1] != ("Image", "surrounded"):
                    for x_offset in range(self.char_width):
                        for y_offset in range(image.height):
                            x_pos = self.cursor_x + x_offset
                            y_pos = self.cursor_y + y_offset
                            self.ensure_grid_size(x_pos, y_pos)
                            self.grid[y_pos][x_pos] = ("Space", "_")
                    self.cursor_x += self.char_width  # Сдвигаем курсор на ширину пробела

            for i in range(image.height):
                for j in range(image.width):
                    # Убедимся, что мы не выходим за пределы текущей ширины сетки
                    current_x = self.cursor_x + j
                    if current_x < self.width:
                        self.grid[self.cursor_y + i][current_x] = ("Image", image.layout)
                    else:
                        # Прекращаем размещение изображения, если достигнут край сетки
                        break

            self.image_coord.append((self.cursor_x, self.cursor_y))
            self.cursor_x += image.width

            if image.layout == "embedded":
                if image.height > self.line_height:
                    self.line_height = image.height

            self.max_y = max(self.max_y, self.cursor_y + self.line_height)

            self.is_floating_last_inserted = False
            self.is_cursor_moved_cause_of_end_line = False

            if self.cursor_x >= self.width:
                self.is_cursor_moved_cause_of_end_line = True
                self.cursor_x_before_cause_of_end_line = self.cursor_x
                self.cursor_y_before_cause_of_end_line = self.cursor_y

                # Если после размещения изображения достигнут край сетки, переходим на новую строку
                self.cursor_x = 0
                self.cursor_y += self.line_height
                self.line_height = self.line_height_default
                self.expand_grid(self.cursor_y + self.line_height_default)


def parse_document(document, char_width):
    elements = []
    # Разделяем документ на абзацы
    paragraphs = document.split("\n\n")  # Два перевода строки подряд обозначают новый абзац
    for paragraph in paragraphs:
        parts = re.split(r"(\(image[^\)]*?\))", paragraph)
        for part in parts:
            part = part.strip()
            if part.startswith("(image"):
                # Извлекаем атрибуты из строки
                attrs = {match[0]: match[1] for match in re.findall(r"(\w+)=(\-?\d+|\w+)", part)}
                if all(key in attrs for key in ["layout", "width", "height"]):
                    elements.append(
                        Image(
                            layout=attrs["layout"],
                            width=attrs["width"],
                            height=attrs["height"],
                            dx=attrs.get("dx", 0),
                            dy=attrs.get("dy", 0),
                        )
                    )
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

    return elements


if __name__ == "__main__":
    # Reading from the file
    with open("input.txt", "r") as reader:
        w, h, c = map(int, reader.readline().strip().split(" "))
        document = reader.read().strip()

    grid = DocumentGrid(w, 25, h, c)

    elements = parse_document(document, c)
    for el in elements:
        if isinstance(el, Word):
            grid.place_word(el)
        elif isinstance(el, Image):
            # print(el)
            if el.layout == "floating":
                grid.place_floating_image(el)
            else:
                grid.place_image(el)
        elif isinstance(el, NewParagraph):
            grid.place_paragraph(el)

    # grid.print_grid()
    # print(grid.image_coord)

    ans = "\n".join(f"{x} {y}" for x, y in grid.image_coord)
    # Writing to the file
    with open("output.txt", "w") as file:
        file.write(ans)
