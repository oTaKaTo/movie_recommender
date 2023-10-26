from button import *
import pyperclip

class Menu:
    def __init__(self):
        self.run = 1
        self.user_text = ""
        self.text_box_active = False
        self.submit = False
        self.movie = []
        self.alert = False

    def draw(self, font, label_font):

        submit = Button(((WIDTH - 120)/2, (HEIGHT*5/8 -60/2),120,60),black,"Find movies",24,screen,border_color=red,border_width=4)
        
    
        label = label_font.render("Movie recommender", 1, black)
        screen.blit(label, (WIDTH / 2 - label.get_width() / 2, 250))


        # Name display

        name_lst = ["สร้างสรรค์โดย \"หนังไก่ไม่มีหนังนี้ดีกว่า\"",
                    "   65010322 ณัฐริกา เจ็กสูงเนิน",
                    "   65010329 ณัฐวุฒิ  ฉายอ่วม",
                    "   65010373 ทักษ์ดนัย  ดีเผือก",
                    "   65010492 ธีรวัชร์ แสงอุไร"]
        for pos,name in enumerate(name_lst):
            name_label = font.render(name, 1, black)
            screen.blit(name_label, (10, HEIGHT-200 + (pos*(40))))
        
        
        
        instruction_font = pygame.font.Font("font/THSarabunNew.ttf",28)
        instruction = instruction_font.render("Enter movie(s) name (if movies >= 2 , enter \',\' between 2 movies)", 1, (6, 97, 0))
        screen.blit(instruction, (140, 500))

        # input
        inp_box = pygame.Rect(120, (HEIGHT - 120)/2, 560, 40 )

        # color_passive store color(chartreuse4) which is 
        # color of input box. 
        color_active = pygame.Color('lightskyblue3') 
        
        color_passive = pygame.Color('chartreuse4') 
        pygame.scrap.init()
        pygame.scrap.set_mode(pygame.SCRAP_CLIPBOARD)
        submit.run()

        # Time delay for repeat when a key is held down
        REPEAT_DELAY = 500  # milliseconds
        REPEAT_RATE = 50    # milliseconds
        # Initialize variables for handling key repetition
        key_repeat_time = 0
        key_repeat_key = None

        #event polling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inp_box.collidepoint(event.pos): 
                    self.text_box_active = True
                else: 
                    self.text_box_active = False
            
            if event.type == pygame.KEYDOWN: 
                if (event.key == pygame.K_v) and (event.mod & pygame.KMOD_CTRL):
                    self.user_text += pyperclip.paste()
                if event.key == pygame.K_RETURN:
                    submit.clicked = True
                # Check for backspace 
                if event.key == pygame.K_ESCAPE:
                    self.user_text = ''
                elif event.key == pygame.K_BACKSPACE: 
                    if pygame.time.get_ticks() - key_repeat_time >= REPEAT_DELAY:
                        key_repeat_key = pygame.K_BACKSPACE
                        key_repeat_time = pygame.time.get_ticks()
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text = self.user_text[:-1]
                else: 
                    self.user_text += event.unicode
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    key_repeat_key = None

        # Check for key repetition
        if key_repeat_key == pygame.K_BACKSPACE and pygame.time.get_ticks() - key_repeat_time >= REPEAT_RATE:
            if self.user_text:  # Check if there's text to delete
                self.user_text = self.user_text[:-1]
            key_repeat_time = pygame.time.get_ticks()


        if self.text_box_active: 
            color = color_active 
        else: 
            color = color_passive
        pygame.draw.rect(screen, color, inp_box) 
        #text input render
        text_inp_font = pygame.font.Font("font/THSarabunNew.ttf",26)
        text_inp = text_inp_font.render(self.user_text, True, black)
        screen.blit(text_inp, (inp_box.x+5, inp_box.y+8)) 

        # set width of textfield so that text cannot get 
        # outside of user's text input 
        inp_box.w = max(100, text_inp.get_width()+10)
            
        

        if submit.clicked:
            if any(c.isalnum() for c in self.user_text) and not all(c.isspace() for c in self.user_text):
                print("SUBMIT!!")
                self.movie = [i.strip().lower() for i in self.user_text.split(",") ]
                print(self.movie)
                self.submit = True
            else:
                self.alert =True



        if self.alert:
            alert = font.render("Please Enter the name of movie(s)", 1, red)
            screen.blit(alert, (300, 700))
        # two_p.run()
        # three_p.run()
        # if one_p.clicked:
        #     # click_sound.play()
        #     # self.game_state = 1
        #     pass
        # if two_p.clicked :
        #     # self.score_state = 1
        #     # click_sound.play()
        #     pass
        # if three_p.clicked:
        #     # click_sound.play()
        #     # self.quit = 1
        #     pass