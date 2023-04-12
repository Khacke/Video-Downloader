from pytube import YouTube
import customtkinter

#####################################
#                GUI                #
#####################################

class App(customtkinter.CTk):

    WIDTH = 800
    HEIGHT = 400

    file_format = 'mp4'

    def __init__(self):
        super().__init__()

        self.title('Ultra Super Duper Swag Youtube Downloader')
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.frame = customtkinter.CTkFrame(master=self)

        # COMPONENTS
        # top label
        self.header = customtkinter.CTkLabel(master=self,
                                             text_font = ('Comic Sans MS', 20, 'bold'),
                                             text="Ultra Super Duper Swag Youtube Downloader 😎",
                                             corner_radius=15,
                                             fg_color="green")
        self.header.pack(padx=20, pady=20)
        
        # link
        self.link_label = customtkinter.CTkLabel(master=self,
                                                 text_font= ('Comic Sans MS', 10),
                                                 text='Enter the link:',
                                                 justify = "left" # nem megy?
                                                )
        self.link_label.pack(padx=20)

        self.link_entry = customtkinter.CTkEntry(master=self,
                                                 placeholder_text="Youtube link :3",
                                                 width= 500)
        self.link_entry.pack(padx=20)

        self.format_menu = customtkinter.CTkOptionMenu(master=self, 
                                                       values=['mp4','mp3-NEM MEGY'], 
                                                       command= self.setformat,
                                                       text_font= ('Comic Sans MS', 10))
        self.format_menu.pack(padx=20)
        self.format_menu.set('mp4')

        self.dl_button = customtkinter.CTkButton(master=self,
                                                 text="DOWNLOAD FOR FREE NO VIRUS!!!! ^^ <3",
                                                 text_font= ('Comic Sans MS', 15),
                                                 command= lambda: self.download(self.link_entry), 
                                                 corner_radius= 10,
                                                 border_color= 'yellow',
                                                 hover_color= 'red')
        self.dl_button.pack(padx=20, pady=20)

        self.console = customtkinter.CTkTextbox(master=self, 
                                                width = 500,
                                                height = 50,
                                                text_font=('Comic Sans MS', 10))
        self.console.pack(padx=5, pady=20)

    
    def done(self):
        self.console.insert("0.0", "Downloaded pakistani cryptominer")
    
    def download(self, link):
        url = str(link.get())
        yt = YouTube(url=url,
                     on_complete_callback=self.done())
        stream = yt.streams.get_highest_resolution()
        stream.download()
        
    def setformat(self, choice):
        self.file_format = str(choice)



if __name__ == '__main__':
    app = App()
    app.mainloop()
