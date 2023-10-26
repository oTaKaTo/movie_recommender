import json
from button import *
from text import *
from recommend import *


def show_result(inp_mov:list):
    # Test the recommendation function
    recommended_movie_titles = recommend(inp_mov)

    # Display the recommendations with popularity and vote average
    print(f"\nRecommendations for '{inp_mov}':")
    all_data = []
    for i, movie_title in enumerate(recommended_movie_titles, start=1):
        # Look up the movie in the original DataFrame
        recommended_movie = df[df['title'] == movie_title].iloc[0]
        popularity = recommended_movie['popularity']
        vote_average = recommended_movie['vote_average']
        # print(f"{i}. {movie_title} (Popularity: {popularity:.2f}, Vote Average: {vote_average:.2f})")
        all_data.append([movie_title,f"{popularity:.2f}",f"{vote_average:.2f}"])
    return all_data





class Result:
    def __init__(self,input_mov:list):

        self.decor1 = Text((WIDTH / 2, 100, WIDTH / 2, HEIGHT / 2), centered=True, fontsize=50)
        self.decor2 = Text((157, 200, WIDTH / 2, HEIGHT / 2), centered=True, fontsize=32)
        self.decor3 = Text((110+360, 200, WIDTH / 2, HEIGHT / 2), centered=True, fontsize=32)
        self.decor4 = Text((110+550, 200, WIDTH / 2, HEIGHT / 2), centered=True, fontsize=32)

        self.run = 1
        self.back = 0
        self.alltext = show_result(input_mov)
        self.input_mov = input_mov

    def draw(self):
        back = Button(((WIDTH - 120)/2, (HEIGHT*8.5/10 -60/2),120,60),black,"BACK",24,screen,border_color=red,border_width=4)
        back.run()
        if back.clicked:
            self.back = 1


    def update(self):

        self.decor1.update("RESULT")
        self.decor2.update("Movie\'s Name")
        self.decor3.update("Popularity")
        self.decor4.update("Vote Average")
        


        self.alldata = []
        for i,data in enumerate(self.alltext):
            name = Text((90, 280+50*i, WIDTH / 2, HEIGHT / 2), fontsize=24)
            name.update(data[0])
            popularity = Text((110+330, 280+50*i, WIDTH / 2, HEIGHT / 2), fontsize=24)
            popularity.update(data[1])
            average = Text((110+530, 280+50*i, WIDTH / 2, HEIGHT / 2), fontsize=24)
            average.update(data[2])
            self.alldata.append([name,popularity,average])

    def runner(self):
        backButton = Button(((WIDTH - 120) / 2, (HEIGHT - 90), 120, 60), black, "BACK", 24, screen,
                                 border_color=red, border_width=4)
        self.update()
        self.decor1.run()
        self.decor2.run()
        self.decor3.run()
        self.decor4.run()
        # for text,label in zip(self.playerScore,self.alltext):
        for label in self.alldata:
            # label[0].update(text[0])
            # label[1].update(str(text[1]))
            # label[2].update(str(text[2]))
            label[0].run()
            label[1].run()
            label[2].run()
        backButton.run()
        if backButton.clicked:
            # click_sound.play()
            self.back = 1