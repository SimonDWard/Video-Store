class VideoStore:
    """Setup video store with a list for the inventory"""
    videos=[]
    def __init__(self, *args, in_out="N", rate=0):
        """ Initialise inventory with key word arguments"""
        for arg in args:
            self.videos.append(arg)
            self.videos.append(in_out)
            self.videos.append(rate)


         
    def AddVideo(self):
        """ Add new title """
        new_video=input("Enter new title  ")
        self.videos.append(new_video)
        self.videos.append("N")
        self.videos.append(0)
    
    def CheckVidOut(self):
        """ Check video out for rental"""
        checkout=input("Enter title to check out ")
        index=self.videos.index(checkout)+1
        self.videos[index]="Y"
        
    def ReturnVideo(self):
        """ Return video to inventory"""
        returnvid=input("Enter title to return ")
        index=self.videos.index(returnvid)
        index=self.videos.index(returnvid)+1
        self.videos[index]="N"
    
    def ReceiveRating(self):
        """ Add rating to a title"""
        title=input("Enter vid title to rate  ")
        rate=input("Enter rating  ")
        index=self.videos.index(title)
        index=self.videos.index(title)+2
        self.videos[index]=rate
        
    
    def DelVid(self):
        """ Delete a video from the inventory"""
        delvid=input("Enter title to remove ")
        index=self.videos.index(delvid)
        print(index)
        self.videos.remove(delvid)
        self.videos.pop(index)
        self.videos.pop(index)
        

    
    def ListInv(self):
        print()
        for vid in self.videos:
            print(vid,"\t")
        print()
 
        
def DisplayMenu():
    """ Display of user menu"""
    print("Video Store \n\n")
    print("""                  1. Add new Title
                  2. Check out a video
                  3. Return a video
                  4. Receive a rating
                  5. Delete title
                  6. List Inventory
                  
                  E. Exit
    """)
    
    
        
if __name__=="__main__":
    #pass list of titles to be initialised
    video=VideoStore("The Matrix", "ET", "Slumdog Millionaire", "Le Regan Vert",  "Mamma Mia")
    
    option = " "
    while option != "E":
        DisplayMenu()
        option=input("Please enter an option  ")
        option=option.upper()
        if option == "1":
            video.AddVideo()
        elif option == "2":
            video.CheckVidOut()
        elif option == "3":
            video.ReturnVideo()
        elif option == "4":
            video.ReceiveRating()
        elif option == "5":
            video.DelVid()
        elif option == "6":
            video.ListInv()
        else:
            print("Invalid option")
        
