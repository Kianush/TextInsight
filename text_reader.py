class TextReader:
    def __init__(self, max_length=1000):
        self._text = ""
        self.max_length = max_length

    def read_from_console(self):
        print(f"Enter a text no more than {self.max_length} symbols):")
        input_text = input()
        if len(input_text) > self.max_length:
            print("The entered text exceeds the maximum limit.")
            input_text = input_text[:self.max_length]
        self._text = input_text

    def read_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read(self.max_length)
            if len(content) == self.max_length:
                print("The text from the file exceeds the maximum limit.")
            self._text = content

    def get_text(self):
        return self._text


