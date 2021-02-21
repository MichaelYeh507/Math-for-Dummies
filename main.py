import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image, ImageDraw, ImageTk, ImageFont
from random import randint, choice

class App:
    def __init__(self, root):
      # init variables
      self.problem_sheet = None
      self.number_of_questions = 51
      self.first_time = True
      self.AnswerSheet_label = None
      """
      STYLE SHEET BEG
      """
      self.BUTTON_BACKGROUND_COLOR = "#efefef"
      self.FONT_TYPE = tkFont.Font(family="Times", size=10)
      
      #setting title
      root.title("Math for Dummies")

      """
      STYLE SHEET END
      """

      # Window settings
      #setting window size
      width=700
      height=700
      screenwidth = root.winfo_screenwidth()
      screenheight = root.winfo_screenheight()
      alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
      root.geometry(alignstr)
      root.resizable(width=False, height=False)

      # Create logo
      logo_image = ImageTk.PhotoImage(Image.open('LLL.png').resize((300, 300), Image.ANTIALIAS))

      self.logo = tkinter.Label(image=logo_image)
      self.logo.image = logo_image
      self.logo["bg"]= "#fff"
      self.logo.place(x=175, y=50)
      self.logo.pack()

      # Generate button
      addition_button = tkinter.Button(root)
      addition_button["bg"] = self.BUTTON_BACKGROUND_COLOR
      addition_button["font"] = self.FONT_TYPE
      addition_button["fg"] = "#000000"
      addition_button["justify"] = "center"
      addition_button["text"] = "Generate"
      addition_button.place(x=50,y=434,width=94,height=34)
      addition_button["command"] = self.generate_image

      # Save button
      save_button = tkinter.Button(root)
      save_button["bg"] = self.BUTTON_BACKGROUND_COLOR
      save_button["font"] = self.FONT_TYPE
      save_button["fg"] = "#000000"
      save_button["justify"] = "center"
      save_button["text"] = "Save"
      save_button.place(x=50, y=400, width=94, height=34)
      save_button["command"] = self.save_image

      # Show & hide button
      self.toggle_visibility = tkinter.Button(root)
      self.toggle_visibility["font"] = self.FONT_TYPE
      self.toggle_visibility["fg"] = "#333333"
      self.toggle_visibility["justify"] = "center"
      self.toggle_visibility["text"] = "Show Answer"
      self.toggle_visibility.place(x=470,y=400,width=100,height=36)
      self.toggle_visibility["command"] = self.toggle_visibility_function

      # Help button
      help_button = tkinter.Button(root)
      help_button["bg"] = self.BUTTON_BACKGROUND_COLOR
      help_button["font"] = self.FONT_TYPE
      help_button["fg"] = "#000000"
      help_button["justify"] = "center"
      help_button["text"] = "Help"
      help_button.place(x=200, y=400, width=94, height=34)
      help_button["command"] = self.display_help

      #labeling entry
      number_of_questions_label = tkinter.Label(root)
      number_of_questions_label["font"] = self.FONT_TYPE
      number_of_questions_label["justify"] = "center"
      number_of_questions_label["bg"] = "#fff"
      number_of_questions_label["text"] = "(Number of Problems)"
      number_of_questions_label.place(x=120, y=470, width=250, height=34)
      
      #labeling minimum
      minimum_label = tkinter.Label(root)
      minimum_label["font"] = self.FONT_TYPE
      minimum_label["justify"] = "center"
      minimum_label["bg"] = "#fff"
      minimum_label["text"] = "(min)"
      minimum_label.place(x=50, y=505, width=250, height=34)

      #labeling maximum
      maximum_label = tkinter.Label(root)
      maximum_label["font"] = self.FONT_TYPE
      maximum_label["justify"] = "center"
      maximum_label["text"] = "(max)"
      maximum_label["bg"] = "#fff"
      maximum_label.place(x=200, y=505, width=250, height=34)

      # number of questions Input field
      self.number_of_questions_input = tkinter.Entry(root)
      self.number_of_questions_input["bg"] = self.BUTTON_BACKGROUND_COLOR
      self.number_of_questions_input["font"] = self.FONT_TYPE
      self.number_of_questions_input["fg"] = "#000000"
      self.number_of_questions_input["justify"] = "center"
      self.number_of_questions_input.place(x=50, y=468, width=94, height=34)
      
      self.min_range_input = tkinter.Entry(root)
      self.min_range_input["bg"] = self.BUTTON_BACKGROUND_COLOR
      self.min_range_input["font"] = self.FONT_TYPE
      self.min_range_input["fg"] = "#000000"
      self.min_range_input["justify"] = "center"
      self.min_range_input.place(x=50, y=502, width=94, height=34)

      self.max_range_input = tkinter.Entry(root)
      self.max_range_input["bg"] = self.BUTTON_BACKGROUND_COLOR
      self.max_range_input["font"] = self.FONT_TYPE
      self.max_range_input["fg"] = "#000000"
      self.max_range_input["justify"] = "center"
      self.max_range_input.place(x=200, y=502, width=94, height=34)

      # radios

      self.switches = 0b10000

      # addition choice
      addition_button = tkinter.Checkbutton(root)
      addition_button["font"] = self.FONT_TYPE
      addition_button["fg"] = "#000"
      addition_button["justify"] = "center"
      addition_button["text"] = "Addition"
      addition_button.place(x=200,y=440,width=100,height=25)
      addition_button["highlightthickness"] = 0
      addition_button["borderwidth"] = 0
      addition_button["bg"] = "#fff"
      addition_button["activebackground"] = '#fff'
      addition_button["command"] = lambda: self.add_to_swtich(1 << 0)

      # subtraction choice
      subtraction_button = tkinter.Checkbutton(root)
      subtraction_button["font"] = self.FONT_TYPE
      subtraction_button["fg"] = "#333333"
      subtraction_button["justify"] = "center"
      subtraction_button["text"] = "Subtraction"
      subtraction_button.place(x=315,y=440,width=125,height=25)
      subtraction_button["bg"] = "#fff"
      subtraction_button["activebackground"] = '#fff'
      subtraction_button["highlightthickness"] = 0
      subtraction_button["command"] = lambda: self.add_to_swtich(1 << 1)

      # multiplication choice
      multiplication_button = tkinter.Checkbutton(root)
      multiplication_button["font"] = self.FONT_TYPE
      multiplication_button["fg"] = "#333333"
      multiplication_button["justify"] = "center"
      multiplication_button["text"] = "Multiplication"
      multiplication_button.place(x=450,y=440,width=150,height=25)
      multiplication_button["bg"] = "#fff"
      multiplication_button["activebackground"] = '#fff'
      multiplication_button["highlightthickness"] = 0
      multiplication_button["command"] = lambda: self.add_to_swtich(1 << 2)

      # division choice
      division_button = tkinter.Checkbutton(root)
      division_button["font"] = self.FONT_TYPE
      division_button["fg"] = "#333333"
      division_button["justify"] = "center"
      division_button["text"] = "Division"
      division_button.place(x=600,y=440,width=100,height=25)
      division_button["bg"] = "#fff"
      division_button["activebackground"] = '#fff'
      division_button["highlightthickness"] = 0
      division_button["command"] = lambda: self.add_to_swtich(1 << 3)

    def display_help(self):
      with open('ReadMe.txt', 'r') as f:
        show_method = getattr(tkinter.messagebox, 'show{}'.format('info'))
        show_method('Help', f.read())

    def toggle_visibility_function(self):
      if self.AnswerSheet_label is not None:
        self.AnswerSheet_label.place(x=400, y=50)

      if self.toggle_visibility["text"] == "Hide":
        self.toggle_visibility["text"] = "Show"
        if self.AnswerSheet_label is not None:
          self.AnswerSheet_label.pack()
          self.AnswerSheet_label.pack_forget()
      else:
         self.toggle_visibility["text"] = "Hide"

    def add_to_swtich(self, n):
      self.switches ^= n

    def addition_generator(self, n, a, b):
      return ('%i) %i + %i =' % (n, a, b),'%i) %i' % (n, a + b))

    def subtraction_generator(self, n, a, b):
      if b > a:
        a, b = b, a
      return ('%i) %i - %i =' % (n, a, b),'%i) %i' % (n, a - b))

    def multiplication_generator(self, n, a, b):
      return ('%i) %i * %i =' % (n, a, b),'%i) %i' % (n, a * b))

    def division_generator(self, n, a, b):
      if b == 0:
        b = randint(1, 10)
      return ('%i) %i / %i =' % (n, a * b, b),'%i) %i' % (n, a))

    def generate_problems(self):
      
      print('generating problem...')

      # check what types of problem to generate
      problem_generators = []
      if self.switches & (1 << 0):
        problem_generators.append(self.addition_generator)
      if self.switches & (1 << 1):
        problem_generators.append(self.subtraction_generator)
      if self.switches & (1 << 2):
        problem_generators.append(self.multiplication_generator)
      if self.switches & (1 << 3):
        problem_generators.append(self.division_generator)

      # init draw image function
      font = ImageFont.truetype(font='ARIAL.TTF', size=100)
      self.drawable_image_problem_sheet = ImageDraw.Draw(self.problem_sheet)
      self.drawable_image_answer_sheet = ImageDraw.Draw(self.answer_sheet)
      problem_at = 1

      # for i in range(int(self.number_of_questions.get())):
      for i in range(self.number_of_questions):
        # Generate text
        problem_text, answer_text = choice(problem_generators)(problem_at, randint(self.number_range_min, self.number_range_max), randint(self.number_range_min, self.number_range_max))

        # Writes text into image
        self.drawable_image_problem_sheet.text((50+int(i / 17)*800, 200*(i%17)+100), problem_text, fill=(0x00,0x00,0x00), font=font)
        self.drawable_image_answer_sheet.text((50+int(i / 17)*800, 200*(i%17)+100), answer_text, fill=(0x00,0x00,0x00), font=font)
        
        problem_at += 1

    def random_b64(self):
        return ''.join(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))

    def generate_image(self):
      if not self.switches & 0b01111:
        # nothing is checked
        print('Please choose one of the operations')
        return

      # Get the number of questions
      self.number_of_questions = self.number_of_questions_input.get()

      if not self.number_of_questions.isdigit():
        print('Enter the required fields correctly')
        return
      self.number_of_questions = int(self.number_of_questions)
      if not 1 <= self.number_of_questions <= 51:
        print('Enter a integer from 1-51 for the number of problems')
        return

      self.number_range_min = self.min_range_input.get();
      if not self.number_range_min.isdigit():
        print('Enter the required fields correctly')
        return
        
      self.number_range_min = int(self.number_range_min)
      if not 0 <= self.number_range_min:
        print('Enter a nonnegative integer')
        return

      self.number_range_max = self.max_range_input.get();
      if not self.number_range_max.isdigit():
        print('Enter the required fields correctly')
        return
        
      self.number_range_max = int(self.number_range_max)
      if not 0 <= self.number_range_max or self.number_range_max < self.number_range_min:
        print('Make sure the max is greater than the min')
        return

      #hgkhjgkhjgkjhjhgvghjhjkhjkghjkjhhjllhjkjhkhjklljkljhb
      if self.number_range_max >= 1000:
        print("Why are you making such a hard worksheet for kids...")
        return

      # Remove logo
      self.logo.pack_forget()

      # Remove previous item if there are any
      if self.AnswerSheet_label is not None:
        self.ProblemSheet_label.pack()
        self.ProblemSheet_label.pack_forget()
        self.AnswerSheet_label.pack()
        self.AnswerSheet_label.pack_forget()

      mode = 'RGB' # for color image “L” (luminance) for greyscale images, “RGB” for true color images, and “CMYK” for pre-press images.
      size = (2480, 3508) # Size of the image (in this case it's A4 paper size in pixel)

      color = (0xff, 0xff, 0xff) # entire image background color 
      self.problem_sheet = Image.new(mode, size, color) # Create a blank sheet
      self.answer_sheet = Image.new(mode, size, color)
      self.generate_problems()

      # Display generated images --

      # problem image displacement
      problem_image = ImageTk.PhotoImage(self.problem_sheet.resize((int(2480 / 10), int(3508 / 10)), Image.ANTIALIAS))

      # Placement for the problem image
      self.ProblemSheet_label = tkinter.Label(image=problem_image)
      self.ProblemSheet_label.image = problem_image
      self.ProblemSheet_label.place(x=50, y=50)

      # answer sheet image displacement
      answer_image = ImageTk.PhotoImage(self.answer_sheet.resize((int(2480 / 10), int(3508 / 10)), Image.ANTIALIAS))

      # Placement for the answer image
      self.AnswerSheet_label = tkinter.Label(image=answer_image)
      self.AnswerSheet_label.image = answer_image
      self.AnswerSheet_label.place(x=400, y=50)

      if self.toggle_visibility["text"] == "Show":
        self.AnswerSheet_label.pack()
        self.AnswerSheet_label.pack_forget()
        

    def save_image(self):
      print('saving image...')
      if self.problem_sheet is None:
        print('No generated images found.')
        # output error messages 
        return

      given_directory = tkinter.filedialog.askdirectory()
      if given_directory == (): # asksaveasfile return `None` if dialog closed with "cancel".
          return
      print(given_directory)
      name1 = given_directory + '/' + self.random_b64() +  '.pdf'
      name2 = given_directory + '/' + self.random_b64() +  '.pdf'
      self.problem_sheet.save(name1) # := is python3.8 stuff
      self.answer_sheet.save(name2)
      print('Problems:' + name1)
      print('Answers:' + name2)
      # self.problem_sheet.show()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.configure(bg='white')
    app = App(root)
    root.mainloop()
