import matplotlib.pyplot as plt
import numpy as np


def rotated_dataset_plot(dataloader)  :
  fig, axs = plt.subplots(8,8,figsize=(15,15))
  image,image_r,rotation = next(iter(dataloader))

  
        
  for i in range(0,16,2):
    img = image[i].squeeze()    
    roteted = image_r[i]
    label_numpy = rotation[i].numpy()
    index = list(np. where(label_numpy == 1))

    plt.subplot(4,4,i+1)
    plt.tight_layout()
    
    plt.imshow(img.permute(1, 2, 0) , cmap="gray",interpolation='none')
    
    plt.xticks([])
    plt.yticks([])
    plt.subplot(4,4,i+2)
    plt.imshow(roteted.permute(1, 2, 0) , cmap="gray",interpolation='none')
    plt.title("{} rotated ".format(int(index[0])*90 ))
