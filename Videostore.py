# Improved version to use a dictionary with booked in or out and ratings stored in a list.
# Duplicte code removed.


class VideoStore:
    """Setup video store with a list for the inventory"""
    videos={}
    def __init__(self, *args, in_out="N", rate=0):
        """ Initialise inventory with key word arguments"""
        for arg in args:
            details=[]
            details.append(in_out)
            details.append(rate)
            self.videos[arg]=details
         
    def AddVideo(self):
        """ Add new title """
        new_video=input("Enter new title  ")
        if new_video not in self.videos:
            self.videos[new_video]=["N",0]
        else:
            print("\n Title already in stock \n")
    def CheckVidInOut(self, out):
        """ Check video out for rental"""
        title=input("Enter title to check out/ return ")
        if title in self.videos:
            values=self.videos[title]
            values[0] = out
            self.videos[title]=values
        else:
            print(" \n Title not in stock")

    def ReceiveRating(self):
        """ Add rating to a title"""
        title=input("Enter video title to rate  ")
        if title in self.videos:
            rate=int(input("Enter rating  "))
            values=self.videos[title]
            existing_rating = values[1] + rate
            values[1]=existing_rating
            self.videos[title]=values
        else:
            print(" \n Title not in stock")
            
    def DelVid(self):
        """ Delete a video from the inventory"""
        delvid=input("Enter title to remove ")
        
        #Avoid termination on key error if value not in dictionary
        try:
            self.videos.pop(delvid)
        except KeyError:
            print("Item not in the inventory")

    
    def ListInv(self):
        """Display all title in the current inventory"""
        print("\n Store Inventory \n") 
        for key, value in self.videos.items():
            print(key, value)
 
        
def DisplayMenu():
    """ Display of user menu"""
    print("\n\t\t\t Video Store \n")
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
            out="Y"
            video.CheckVidInOut(out)
        elif option == "3":
            out = "N"
            video.CheckVidInOut(out)
        elif option == "4":
            video.ReceiveRating()
        elif option == "5":
            video.DelVid()
        elif option == "6":
            video.ListInv()
        else:
            print("Invalid option")
        
