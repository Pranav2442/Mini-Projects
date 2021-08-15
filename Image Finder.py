import cv2 as cv                                        
from matplotlib import pyplot as plt
import os



images=[]                                   #Initializing a list to store images
place={}                                    #initializing a dictionary to store the address  
info={}                                     #initializing a dictionary to store information of images like key and values



#takes path of the database from the user
directory_path=input("Enter the path of the database\n")

#using os.listdir to print all the names of the files present in that directory
dir_path=os.listdir(directory_path)

#prints all the files present inside the direcotory
print(dir_path)

#takes name of an image 
image_name=input("Enter the name of an image from the above names\n")

#complete path of the quried image
image_path=(f"{directory_path}\\{image_name}")

#prints the path of a quried image
print(image_path)


#finding files and listing them 
def imagelisting(directory_name):
    for path in os.listdir(directory_name):
        
        #joins the directory path and file path
        track=os.path.join(directory_path,path)
        # place.update(feature_extraction(track))
        place[track]=feature_of_images(track)
        # place=sorted(info.items(),key=lambda x: x[1] )
        
        #prints the path of every image
        print(f"image path={track}")
    # print(f"place={place}")
    return place
    




#using feature_of_images function to extract information from them
def feature_of_images(path_of_image):
    
    #reading the image
    img=cv.imread(path_of_image)

    #using calhist to draw the histogram of image
    calhist=cv.calcHist([img],[0],None,[256],[0,256])
    
    #using normalize to get the normalized histogram
    normalized_histogram=cv.normalize(calhist,calhist)
    return normalized_histogram


#using Best_matched to find the simillar images
def Best_matched(histogram_of_quried_image,Entire_images):
    
    for(keys,values) in Entire_images.items():
        info[keys]=cv.compareHist(histogram_of_quried_image,values,cv.HISTCMP_CHISQR)
    order=sorted(info.items(),key=lambda x: x[1] )
    # print(f"keys={keys}")
    # print(f"values={values}")
    print(order)
    return order



#using compare_image to compare the images
def compare_image(query_image,direc):

    #extracting all the images presenting in the directory by calling the imagelisting function
    Entire_images=imagelisting(direc)

    #ploting the histogram of quried image
    histogram_of_quried_image=feature_of_images(query_image)

    #finding simillar images using function Best_match
    simmilar_image=Best_matched(histogram_of_quried_image,Entire_images)
    return simmilar_image



#assiging paths to x,y
x,y=directory_path,image_path

#calling compare_image
search=compare_image(y,x)


for im,hist_val in search:

    #reading the image
    image=cv.imread(im)

    #converting BGR to RGB as the matplotlib uses RGB format
    RGB=cv.cvtColor(image,cv.COLOR_BGR2RGB)

    #storing RGB images in the list 
    images.append(RGB)
    # images=[RGB]
    
    # print(len(RGB))
    # print(len(images))
    # print(len(search))



#for giving title
titles=[]
# for i in range(1,len(RGB)):
    # titles.append("Matched Figure"+str(i))


for i in range(0,5):
    
    plt.subplot(2,3,i+1),plt.imshow(images[i])
    titles.append("Matched Figure"+str(i))
    plt.title([titles[i]])
    
    plt.xticks([])
    plt.yticks([])
    
plt.show()
cv.waitKey(0)  
    


#logic

'''

1)First of all initializing the liabraries like opencv,matplotlib

2)Initializing a list images and 2 dictionaries place and info

3)directory_path will take path of the database as thinput from the user

4) dir_path will print the available files inside the directory_path

5)using image_name to ask the user the name of the query image

6)image_path gives the complete path of the image

7)using image_listing function

    a)track gives the complete path of an each image present inside the direcortory
    

8) using feature_of_images to extract imformation 

    a)using cv.imread to read the image
    b)calhist to get the histogram of an image
    c)normalize_histogram to get the normalized histogram 

9) using compare_image to compare the query image 
    a)calling imagelisting
    b)calling features_of_images
    c)calling Best_matched to find the matches of the quried image

10) using Best_matched
    a)using chi_square
    b)sorting the dictionary and storing them in order

10)assigning the paths of directory_path and image_path in x,y

11)calling compare_image

12)converting image into RGB as the matplotlib reads images in RGB format

13)storing RGB in images

14)using matplotlib to show the simillar images


        '''