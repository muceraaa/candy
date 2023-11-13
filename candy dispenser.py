from tkinter import Button, Canvas, LEFT, Label, RAISED, RIGHT, Tk
from tkinter.messagebox import showerror, showinfo #pop up dialog box to show information and error

class Candy_Dispenser: #defining a new class

    def __init__(self, window: Tk): #constructor method....self is reference to the object being created
        self.window = window
        self.color_primary = "purple"

        self.candy_stack = [] #Initialize empty list to store the candy
        self.max_size = 10  #maximum size is 10

        # Spring
        self.spring_left = 73
        self.spring_right = 287
        self.spring_top = 120
        self.spring_bottom = 750  # Adjust the spring_bottom for 10 candies
        self.spring_offset = 30  # Adjust the spring offset
        self.spring_thickness = 4

        # Position of new candy bar in the dispenser
        self.new_bar_bottom = self.spring_top + 30  # Candy height = 56px.
        self.new_bar_cx = (self.spring_left + self.spring_right) / 2 # Center X, centering the label
        self.new_bar_cy = (self.spring_top + self.new_bar_bottom) / 2  # Center Y

        # Adjust y positions for 10 candies (spacing vertically)
        self.a_y = 120
        self.b_y = 190
        self.c_y = 260
        self.d_y = 330
        self.e_y = 400
        self.f_y = 470
        self.g_y = 540
        
        
        
        #creating a split layout in the canvas (2 windows within the main window)
        #left window for candy dispenser
        self.left_panel = Canvas(self.window, width=(window_width / 2), height=window_height)  
        self.left_panel.pack(side=LEFT)

        #right window for buttons
        self.right_panel = Canvas(self.window, width=(window_width / 2), height=window_height)
        self.right_panel.pack(side=RIGHT)

        #Drawing components of the left panel
        # Draw spring (basically made up of many lines aligned to the left and right)
        self.a = self.left_panel.create_line(self.spring_left, self.a_y, self.spring_right, self.a_y,
                                             width=self.spring_thickness, smooth=True)

        self.a_b1 = self.left_panel.create_line(self.spring_left, self.a_y, self.spring_right, self.b_y,
                                               width=self.spring_thickness, smooth=True)

        self.a_b2 = self.left_panel.create_line(self.spring_left, self.b_y, self.spring_right, self.a_y,
                                               width=self.spring_thickness, smooth=True)

        self.b = self.left_panel.create_line(self.spring_left, self.b_y, self.spring_right, self.b_y,
                                             width=self.spring_thickness, smooth=True)

        self.b_c1 = self.left_panel.create_line(self.spring_left, self.c_y, self.spring_right, self.b_y,
                                               width=self.spring_thickness, smooth=True)

        self.b_c2 = self.left_panel.create_line(self.spring_right, self.c_y, self.spring_left, self.b_y,
                                               width=self.spring_thickness, smooth=True)

        self.c = self.left_panel.create_line(self.spring_left, self.c_y, self.spring_right, self.c_y,
                                             width=self.spring_thickness, smooth=True)

        self.c_d1 = self.left_panel.create_line(self.spring_left, self.c_y, self.spring_right, self.d_y,
                                                width=self.spring_thickness, smooth=True)

        self.c_d2 = self.left_panel.create_line(self.spring_right, self.c_y, self.spring_left, self.d_y,
                                                width=self.spring_thickness, smooth=True)

        self.d = self.left_panel.create_line(self.spring_left, self.d_y, self.spring_right, self.d_y,
                                             width=self.spring_thickness, smooth=True)

        self.d_e1 = self.left_panel.create_line(self.spring_left, self.d_y, self.spring_right, self.e_y,
                                                width=self.spring_thickness, smooth=True)

        self.d_e2 = self.left_panel.create_line(self.spring_right, self.d_y, self.spring_left, self.e_y,
                                                width=self.spring_thickness, smooth=True)

        self.e = self.left_panel.create_line(self.spring_left, self.e_y, self.spring_right, self.e_y,
                                              width=self.spring_thickness, smooth=True)

        self.e_f1 = self.left_panel.create_line(self.spring_left, self.e_y, self.spring_right, self.f_y,
                                              width=self.spring_thickness, smooth=True)

        self.e_f2 = self.left_panel.create_line(self.spring_right, self.e_y, self.spring_left, self.f_y,
                                               width=self.spring_thickness, smooth=True)

        self.f = self.left_panel.create_line(self.spring_left, self.f_y, self.spring_right, self.f_y,
                                               width=self.spring_thickness, smooth=True)
        
        #creating the candy dispenser
        self.left_panel.create_line(290, 100, 70, 100, width=6) #top
        self.left_panel.create_line(70, 100, 70, 570, width=6) #left
        self.left_panel.create_line(290, 100, 290, 570, width=6)#right
        self.left_panel.create_line(290, 570, 70, 570, width=6) #bottom

        # Draw components for the right panel
        #Drawing the buttons
        Button(self.right_panel, text="PUSH", fg="white", bg=self.color_primary, font=("Calibri", 12, "bold"),
               relief=RAISED, bd=7, command=self.push).place(x=52, y=100)

        Button(self.right_panel, text="POP", fg="white", bg=self.color_primary, font=("Calibri", 12, "bold"),
               relief=RAISED, bd=7, command=self.pop).place(x=180, y=100)

        Button(self.right_panel, text="TOP", fg="white", bg=self.color_primary, font=("Calibri", 12, "bold"),
               relief=RAISED, bd=7, command=self.top).place(x=52, y=200)

        Button(self.right_panel, text="SIZE", fg="white", bg=self.color_primary, font=("Calibri", 12, "bold"),
               relief=RAISED, bd=7, command=self.report_size).place(x=180, y=200)

        Button(self.right_panel, text="IS EMPTY?", fg="white", bg=self.color_primary, font=("Calibri", 12, "bold"),
               relief=RAISED, bd=7, command=self.report_empty_stat).place(x=100, y=321)

    def pop(self):
        if self.size() > 0: #checks if the size of the candy stack is greater than 0
            candy = self.candy_stack.pop() #removes the top candy and assigns it to the variable candy
            self.left_panel.delete(candy['bar']) #removes the candy bar
            self.left_panel.delete(candy['label']) #removes the label of the candy eg candy1
            self.update_dispenser('pop') #update the candy dispenser
            showinfo("Pop Candy", f"Popped: {candy['tag']}")  # Show a message with the popped candy's label
        else:
            showerror("Stack Underflow!", "The Candy Dispenser is empty.") #if stack is empty, display message

    def push(self):
        if self.size() < self.max_size: #checks if stack size is less than max size
            self.candy_stack.append(self.draw_candy())  # Add candy to stack.
            self.update_dispenser('push')
        else:
            showerror("Stack Overflow!", "The Candy Dispenser is full.") #if max is reached, display message

    #Drawing the candies        
    def draw_candy(self):
        bar = self.left_panel.create_oval(self.spring_left, self.spring_top, self.spring_right,
                                          self.new_bar_bottom, fill=self.color_primary)
        tag = f'Candy {self.size() + 1}' #labelling the candies depending on current size of the stack, eg candy1
        label = self.left_panel.create_text(self.new_bar_cx, self.new_bar_cy, text=tag, fill='white') #centering the label
        return {'bar': bar, 'label': label, 'tag': tag}

    
    
    # Update position of candies based on their index in the stack.
    def update_dispenser(self, mode):
        
        if mode == 'push':
            for i in range(self.size()):
                self.update_candy_pos(self.candy_stack[i], (self.size() - 1) - i)

            # Update spring's pitch.
            self.a_y += self.spring_offset
            self.b_y += self.spring_offset / 1.5
            self.c_y += self.spring_offset / 2
            self.d_y += self.spring_offset / 2.5
            self.e_y += self.spring_offset / 3
            self.f_y += self.spring_offset / 3.5
            self.g_y += self.spring_offset / 4

        elif mode == 'pop':
            stack_size = self.size()
            for i in range(stack_size):
                self.update_candy_pos(self.candy_stack[i], stack_size - (i + 1))

            # Update spring's pitch.
            self.a_y -= self.spring_offset
            self.b_y -= self.spring_offset / 1.5
            self.c_y -= self.spring_offset / 2
            self.d_y -= self.spring_offset / 2.5
            self.e_y -= self.spring_offset / 3
            self.f_y -= self.spring_offset / 3.5
            self.g_y -= self.spring_offset / 4
        else:
            raise Exception

        # Update spring.
        self.left_panel.coords(self.a, self.spring_left, self.a_y, self.spring_right, self.a_y)
        self.left_panel.coords(self.a_b1, self.spring_left, self.a_y, self.spring_right, self.b_y)
        self.left_panel.coords(self.a_b2, self.spring_left, self.b_y, self.spring_right, self.a_y)
        self.left_panel.coords(self.b, self.spring_left, self.b_y, self.spring_right, self.b_y)
        self.left_panel.coords(self.b_c1, self.spring_left, self.c_y, self.spring_right, self.b_y)
        self.left_panel.coords(self.b_c2, self.spring_right, self.c_y, self.spring_left, self.b_y)
        self.left_panel.coords(self.c, self.spring_left, self.c_y, self.spring_right, self.c_y)
        self.left_panel.coords(self.c_d1, self.spring_left, self.c_y, self.spring_right, self.d_y)
        self.left_panel.coords(self.c_d2, self.spring_right, self.c_y, self.spring_left, self.d_y)
        self.left_panel.coords(self.d, self.spring_left, self.d_y, self.spring_right, self.d_y)
        self.left_panel.coords(self.d_e1, self.spring_left, self.d_y, self.spring_right, self.e_y)
        self.left_panel.coords(self.d_e2, self.spring_right, self.d_y, self.spring_left, self.e_y)
        self.left_panel.coords(self.e, self.spring_left, self.e_y, self.spring_right, self.e_y)
        self.left_panel.coords(self.e_f1, self.spring_right, self.e_y, self.spring_left, self.f_y)
        self.left_panel.coords(self.e_f2, self.spring_left, self.e_y, self.spring_right, self.f_y)
        self.left_panel.coords(self.f, self.spring_right, self.f_y, self.spring_left, self.f_y)
       
     
    #Adjusting the position of the candy in relation to the updated spring
    def update_candy_pos(self, candy, y):
        updated_bar_top = self.spring_top + (self.spring_offset * y)
        updated_bar_bottom = self.new_bar_bottom + (self.spring_offset * y)

        self.left_panel.coords(
            candy['bar'], self.spring_left, updated_bar_top, self.spring_right, updated_bar_bottom
        )
        self.left_panel.coords(
            candy['label'], self.new_bar_cx, (updated_bar_top + updated_bar_bottom) / 2
        )

    def size(self):
        return len(self.candy_stack)

    def report_size(self):
        showinfo('Size', f'The Candy dispenser size is {self.size()}') #pop up message box showing size of candy dispenser

    def top(self):
        if self.is_empty(): #checks if candy dispenser is empty
            showerror('Top Failed', 'The Candy dispenser is empty') #if empty
        else:
            showinfo('Top', f'The Top candy is "{self.candy_stack[-1]["tag"]}"')

    def is_empty(self):
        if self.size() == 0: #checks if candy dispenser is empty
            return True
        return False

    def report_empty_stat(self): #reports if candy dispenser is empty by using is_empty results
        msg = 'False'
        if self.is_empty():
            msg = 'True'
        showinfo('Is Empty?', msg)


if __name__ == '__main__': #checks if the script is being run as the main program and not imported as a module in another script
    window_height = 850  # define window of the candy dispenser
    window_width = 850

    root = Tk() #create the main application window
    root.title('Candy Dispenser')
    root.maxsize(window_width, window_height) #set the maximum dimensions of the window
    root.minsize(window_width, window_height) #set the minimum dimesions of the window
    Candy_Dispenser(root) #dispalys the candy dispenser within the application window
    root.mainloop() #starts the tkinter event loop which keeps the app running and responsive to user actions
