import customtkinter
import os
from PIL import Image
from logiquefloue import tailleChemise, taillePantalon , tailleVeste


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Suit Size Help")
        self.geometry("1000x650")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.pants_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "pants.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "pants.png")), size=(20, 20))
        self.chemise_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chemise.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "chemise.png")), size=(20, 20))
        self.costume_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "costume.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "costume.png")), size=(20, 20))
        

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Clothes Size Help", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Chemise",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chemise_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Pantalon",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.pants_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Veste",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.costume_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

##############################################################







        # create home frame
        self.home_frame = customtkinter.CTkScrollableFrame(master=self, width=200, height=200)
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.msg_bienvenu = customtkinter.CTkLabel(self.home_frame, 
                                                   text="BIENVENUE SUR NOTRE GUIDE", 
                                                   font=("Times New Roman", 40, "bold"))
        self.msg_bienvenu.grid(row=0, column=0, padx=20, pady=10)
        self.message = customtkinter.CTkLabel(self.home_frame, 
                                              text="Ce logiciel est un guide basé sur un modèle floue permettant de trouver \nvotre taille de chemise, pantalons et veste en\n fonction de vos dimensions.",
                                              font=("Arial",21),justify="center")
        self.message.grid(row=1, column=0, padx=20, pady=20)

        self.message2 = customtkinter.CTkLabel(self.home_frame, 
                                              text="Il est important de connaître vos mensurations respectives.\nCe logiciel ne prend en considération uniquement que les hommes",
                                              font=("Arial",21),justify="center")
        self.message2.grid(row=2, column=0, padx=20, pady=20)

        self.message3 = customtkinter.CTkLabel(self.home_frame, 
                                              text="Merci pour votre compréhension.",
                                              font=("Arial",21),justify="center")
        self.message3.grid(row=3, column=0, padx=20, pady=20)

        self.suit_img = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "beautiful_suit.jpg")),
                                                 dark_image=Image.open(os.path.join(image_path, "beautiful_suit.jpg")), size=(328, 492))
        
        self.suit_image_label = customtkinter.CTkLabel(master=self.home_frame, image=self.suit_img, text="")  # display image with a CTkLabel
        self.suit_image_label.grid(row=4,column=0, padx=10, pady=20,columnspan=2)











 
############################################################## CHOIX DE CHEMISES







        # create second frame
        self.second_frame = customtkinter.CTkScrollableFrame(master=self, width=200, height=200)
        self.second_frame.grid_columnconfigure(0, weight=1)

        self.titre_veste = customtkinter.CTkLabel(self.second_frame,text="Guide taille de Veste",font=("Times New Roman", 40, "bold"))
        self.titre_veste.grid(row=0, column=0, padx=0, pady=10,columnspan=2)

        self.inputs_sncFrame = customtkinter.CTkFrame(self.second_frame, border_width=0)
        self.inputs_sncFrame.grid(row=1,column=0,padx=0,pady=31,sticky="ew")

        self.labelLongueurEpaule = customtkinter.CTkLabel(self.inputs_sncFrame, justify='left', text="Tour de taille (cm) : ", font=("Helvetica",14))
        self.labelLongueurEpaule.grid(row=1, column=0,padx=5, pady=20)

        self.tt_entry = customtkinter.CTkEntry(master=self.inputs_sncFrame,placeholder_text="C",font=("Helvetica", 14), width=150,state="normal")
        self.tt_entry.grid(row=1, column=1, padx=0, pady= 25,sticky="ew")

        self.labelTourPoitrine = customtkinter.CTkLabel(self.inputs_sncFrame, justify='left', text="Tour de poitrine (cm) : ", font=("Helvetica",14))
        self.labelTourPoitrine.grid(row=2, column=0,padx=5, pady=20)

        self.tp_entry = customtkinter.CTkEntry(master=self.inputs_sncFrame,placeholder_text="A",font=("Helvetica", 14), width=150,state="normal")
        self.tp_entry.grid(row=2, column=1, padx=0, pady= 25,sticky="ew")

        self.taille_dos = customtkinter.CTkLabel(self.inputs_sncFrame, justify='left', text="Longueur dos (cm) : ", font=("Helvetica",14))
        self.taille_dos.grid(row=3, column=0,padx=5, pady=20)

        self.td_entry = customtkinter.CTkEntry(master=self.inputs_sncFrame,placeholder_text="D",font=("Helvetica", 14), width=150,state="normal")
        self.td_entry.grid(row=3, column=1, padx=0, pady= 25,sticky="ew")

        self.longueurManche = customtkinter.CTkLabel(self.inputs_sncFrame, justify='left', text="Longueur manche (cm) : ", font=("Helvetica",14))
        self.longueurManche.grid(row=4, column=0,padx=5, pady=20)

        self.lm_entry = customtkinter.CTkEntry(master=self.inputs_sncFrame,placeholder_text="H",font=("Helvetica", 14), width=150,state="normal")
        self.lm_entry.grid(row=4, column=1, padx=0, pady= 25,sticky="ew")


        self.Chemise_img = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chemise.JPG")),
                                                 dark_image=Image.open(os.path.join(image_path, "chemise.JPG")), size=(300, 300))

        self.Cimage_label = customtkinter.CTkLabel(master=self.second_frame, image=self.Chemise_img, text="")  # display image with a CTkLabel
        self.Cimage_label.grid(row=1,column=1, padx=10, pady=20)

        # Création d'un conteneur pour le résumé du texte entré
        self.Csummary_frame = customtkinter.CTkFrame(master=self.second_frame, border_width=1, width=450)
        self.Csummary_frame.grid(row=2,column=0,columnspan=2,pady=3,sticky="w")
    # Ajout de l'étiquette pour le résumé
        self.summary2_label = customtkinter.CTkLabel(self.Csummary_frame, text="", font=("Helvetica", 14))
        self.summary2_label.grid(row=3, column=0)
        def clearChemiseFields():
            self.tt_entry.delete(0, 'end')
            self.td_entry.delete(0, 'end')
            self.tp_entry.delete(0, 'end')
            self.lm_entry.delete(0,'end')
            self.summary2_label.config(text="")

        # Fonction appelée lorsqu'un bouton est cliqué
        def summarizeChemise():
            resultat = tailleChemise(float(self.tt_entry.get()), float(self.tp_entry.get()), float(self.td_entry.get()),float(self.lm_entry.get()))
       
            if resultat is not None:
                self.summary2_label.configure(wraplength=1000, 
                                        justify='left', 
                                        text="Tour de taille :\t\t{} cm\nTour de poitrine :\t\t{} cm\nLongueur du dos :\t\t{} cm\nLongueur manche :\t\t{} cm\nRésultat :\t\t\t    {}".format(self.tt_entry.get(), 
                                                                                                                                                                self.tp_entry.get(), 
                                                                                                                                                                self.td_entry.get(),self.lm_entry.get(), 
                                                                                                                                                            resultat))
            else:
                self.summary2_label.configure(wraplength=1000, justify='left', text="Désolé, il n'y a pas de pointure en accord avec vos caractéristiques !")


        #Button submit
        self.CsubmitButton = customtkinter.CTkButton(master=self.second_frame, text="Submit", command=summarizeChemise)
        self.CsubmitButton.grid(row=2,column=1,pady=10,sticky="se")
        #Button Clear
        self.CclearButton = customtkinter.CTkButton(master=self.second_frame, text="Clear", command=clearChemiseFields,fg_color="#008000")
        self.CclearButton.grid(row=2,column=1,padx=150,pady=10,sticky="se")









##############################################################







        # create third frame
        self.third_frame = customtkinter.CTkScrollableFrame(master=self, width=200, height=200)
        self.third_frame.grid_columnconfigure(0, weight=1)

        self.titre_pantalons = customtkinter.CTkLabel(self.third_frame, 
                                                   text="Guide taille de Pantalons", 
                                                   font=("Times New Roman", 40, "bold"))
        self.titre_pantalons.grid(row=0, column=0, padx=0, pady=10,columnspan=2)

        
        self.inputs_frthFrame = customtkinter.CTkFrame(self.third_frame, border_width=0)
        self.inputs_frthFrame.grid(row=1,column=0,padx=0,pady=31,sticky="ew")

        self.labelLongueurJambe = customtkinter.CTkLabel(self.inputs_frthFrame, justify='left', text="Longueur Jambe (cm) : ", font=("Helvetica",14))
        self.labelLongueurJambe.grid(row=1, column=0,padx=5, pady=20)

        self.lj_entry = customtkinter.CTkEntry(master=self.inputs_frthFrame,placeholder_text="D",font=("Helvetica", 14), width=150,state="normal")
        self.lj_entry.grid(row=1, column=1, padx=0, pady= 25,sticky="ew")

        self.labellongeurHanche = customtkinter.CTkLabel(self.inputs_frthFrame, justify='left', text="Longeur Hanche (cm) : ", font=("Helvetica",14))
        self.labellongeurHanche.grid(row=2, column=0,padx=5, pady=20)

        self.lh_entry = customtkinter.CTkEntry(master=self.inputs_frthFrame,placeholder_text="B",font=("Helvetica", 14), width=150,state="normal")
        self.lh_entry.grid(row=2, column=1, padx=0, pady= 25,sticky="ew")

        self.Pantalon_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "pantalon.JPG")),
                                                 dark_image=Image.open(os.path.join(image_path, "pantalon.JPG")), size=(212, 334))

        self.Pimage_label = customtkinter.CTkLabel(master=self.third_frame, image=self.Pantalon_image, text="")  # display image with a CTkLabel
        self.Pimage_label.grid(row=1,column=1, padx=10, pady=20)

        # Création d'un conteneur pour le résumé du texte entré
        self.Psummary_frame = customtkinter.CTkFrame(master=self.third_frame, border_width=1, width=450)
        self.Psummary_frame.grid(row=2,column=0,columnspan=2,pady=3,sticky="w")
    # Ajout de l'étiquette pour le résumé
        self.summary_label = customtkinter.CTkLabel(self.Psummary_frame, text="", font=("Helvetica", 14))
        self.summary_label.grid(row=3, column=0)
        def clearPantalonFields():
            self.lj_entry.delete(0, 'end')
            self.lh_entry.delete(0, 'end')
            self.summary_label.configure(text="")

        # Fonction appelée lorsqu'un bouton est cliqué
        def summarizePantalon():

            resultat = taillePantalon(float(self.lj_entry.get()), float(self.lh_entry.get()))
            if resultat is not None:
                self.summary_label.configure(wraplength=1000, 
                                        justify='left', 
                                        text="Tour de hanche :\t\t{} cm\nLongueur de jambe :\t\t{} cm\nRésultat :\t\t\t{}".format(self.lh_entry.get(), 
                                                                                                                                    self.lj_entry.get(), 
                                                                                                                                    resultat))
            else:
                self.summary_label.configure(wraplength=1000, justify='left', text="Désolé, il n'y a pas de pointure en accord avec vos caractéristiques!!")

        #Button submit
        self.PsubmitButton = customtkinter.CTkButton(master=self.third_frame, text="Submit", command=summarizePantalon)
        self.PsubmitButton.grid(row=2,column=1,pady=10,sticky="se")
        #Button Clear
        self.PclearButton = customtkinter.CTkButton(master=self.third_frame, text="Clear", command=clearPantalonFields,fg_color="#008000")
        self.PclearButton.grid(row=2,column=1,padx=150,pady=10,sticky="se")
        








##############################################################


        # create fourth frame
        self.fourth_frame = customtkinter.CTkScrollableFrame(master=self, width=200, height=200)
        self.fourth_frame.grid_columnconfigure(0, weight=1)

        self.titre_costume = customtkinter.CTkLabel(self.fourth_frame, 
                                                   text="Guide taille de Vestes", 
                                                   font=("Times New Roman", 40, "bold"))
        self.titre_costume.grid(row=0, column=0, padx=0, pady=10,columnspan=2)
        
        self.inputs_frthFrame = customtkinter.CTkFrame(self.fourth_frame, border_width=0)
        self.inputs_frthFrame.grid(row=1,column=0,padx=0,pady=31,sticky="ew")

        self.SlabelTourTaille = customtkinter.CTkLabel(self.inputs_frthFrame, justify='left', text="Tour de Taille (cm) : ", font=("Helvetica",14))
        self.SlabelTourTaille.grid(row=0, column=0,padx=5, pady=20)

        self.Stt_entry = customtkinter.CTkEntry(master=self.inputs_frthFrame,font=("Helvetica", 14), width=150,state="normal")
        self.Stt_entry.grid(row=0, column=1, padx=0, pady= 25,sticky="ew")

        self.Staille_dos = customtkinter.CTkLabel(self.inputs_frthFrame, justify='left', text="Longueur dos (cm) : ", font=("Helvetica",14))
        self.Staille_dos.grid(row=1, column=0,padx=5, pady=20)

        self.Std_entry = customtkinter.CTkEntry(master=self.inputs_frthFrame,font=("Helvetica", 14), width=150,placeholder_text="A",state="normal")
        self.Std_entry.grid(row=1, column=1, padx=0, pady= 25,sticky="ew")

        self.SlabelTourPoitrineCost = customtkinter.CTkLabel(self.inputs_frthFrame, justify='left', text="Tour de poitrine (cm) : ", font=("Helvetica",14))
        self.SlabelTourPoitrineCost.grid(row=2, column=0,padx=5, pady=20)

        self.Stg_entry = customtkinter.CTkEntry(master=self.inputs_frthFrame,font=("Helvetica", 14),placeholder_text="B", width=150,state="normal")
        self.Stg_entry.grid(row=2, column=1, padx=0, pady= 25,sticky="ew")

        self.cost_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "costume.jpeg")),
                                                 dark_image=Image.open(os.path.join(image_path, "costume.jpeg")), size=(310, 283))

        self.Simage_label = customtkinter.CTkLabel(master=self.inputs_frthFrame, image=self.cost_image, text="")  # display image with a CTkLabel
        self.Simage_label.grid(row=0,column=2, padx=10, pady=20,rowspan=3)

        # Création d'un conteneur pour le résumé du texte entré
        self.Ssummary_frame = customtkinter.CTkFrame(master=self.fourth_frame, border_width=0, width=450)
        self.Ssummary_frame.grid(row=3,column=0,columnspan=3,pady=3,sticky="w")

        self.Ssummary_label = customtkinter.CTkLabel(self.Ssummary_frame, text="", font=("Helvetica", 14))
        self.Ssummary_label.grid(row=1, column=0)

        def clearCostumeFields():
            self.Stt_entry.delete(0, 'end')
            self.Std_entry.delete(0, 'end')
            self.Stg_entry.delete(0,'end')
            self.Ssummary_label.configure(text="")


        # Fonction appelée lorsqu'un bouton est cliqué
        def summarizeCostume():
            #Effacer la précédente réponse
            if self.Ssummary_label != "":
                self.Ssummary_label.configure(text="")

            resultat = tailleVeste(float(self.Stt_entry.get()), float(self.Stg_entry.get()), float(self.Std_entry.get()))

            if resultat is not None:
                self.Ssummary_label.configure(wraplength=1000, 
                                        justify='left', 
                                        text="Tour de taille :\t\t{} cm\ntoure poitrine :\t\t{} cm\ntaille dos :\t\t{} cm\nRésultat :\t\t\t{}".format(self.Stt_entry.get(), 
                                                                                                                                    self.Std_entry.get(),self.Stg_entry.get(), 
                                                                                                                                    resultat))
            else:
                self.Ssummary_label.configure(wraplength=1000, justify='left', text="Désolé, Nous n'avons pas de taille en accord avec vos mensurations !")

        #Button submit
        self.SsubmitButton = customtkinter.CTkButton(master=self.inputs_frthFrame, text="Submit", command=summarizeCostume)
        self.SsubmitButton.grid(row=9,column=2,pady=10,sticky="se")
        #Button Clear
        self.SclearButton = customtkinter.CTkButton(master=self.inputs_frthFrame, text="Clear", command=clearCostumeFields,fg_color="#008000")
        self.SclearButton.grid(row=9,column=2,padx=150,pady=10,sticky="se")

##############################################################



        # select default frame
        self.select_frame_by_name("home")



##############################################################



    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "Chemise" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "Pantalon" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "Veste" else "transparent")


        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Chemise":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "Pantalon":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "Veste":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()


    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("Chemise")

    def frame_3_button_event(self):
        self.select_frame_by_name("Pantalon")
    
    def frame_4_button_event(self):
        self.select_frame_by_name("Veste")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()

