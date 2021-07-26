from re import L
import pygame
import pygame_gui
import random
from copy import deepcopy

#--------------------------------------------------------------------------------------------------------------------------------
#pygame and manager initiation


pygame.init()

global SCREEN
global manager

SCREEN = pygame.display.set_mode((1300, 700))
manager = pygame_gui.UIManager((1300, 700), "themes.json")

pygame.display.set_caption('Sorting Algorithms Visualizer')

SCREEN.fill(pygame.Color('#000000'))    

clock = pygame.time.Clock()

#--------------------------------------------------------------------------------------------------------------------------------
#fonts and writing text function

font = pygame.font.SysFont(None, 30)
font_2 = pygame.font.SysFont(None, 35)

def draw_text(text, font, color, surface, x, y):

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#--------------------------------------------------------------------------------------------------------------------------------
#data generate

global data, data2, data_color, colors

def generate_data(l):
    data = [random.randrange(1, 500) for i in range(l)]
    data2 = deepcopy(data)
    return data, data2

data, data2 = generate_data(70)

data_color=[(255,255,255)]*(len(data)+1)
colors = [(255,255,255), (243,43,16), (83, 229,36), (0, 0, 255)]  #avilable colours: white standard, comparing, conditions met


#--------------------------------------------------------------------------------------------------------------------------------
#classes

class Button():

    def __init__(self, name, x,y,x2,y2): 
        self.shape = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x,y), (x2,y2)), text=name, manager=manager)



class Background_rects():

    def __init__(self, colour, x, y, l,w):
        self.drav = pygame.Rect(x, y, l, w)
        self.colour = colour

    def draw_rect(self):
        pygame.draw.rect(SCREEN, self.colour, self.drav)


#-------------------------------------------------------------------------------------------------------------------------------
#variables 

buttons_c1 = []
x=10
y=80
x2=130
y2=20

names = ['Bubble sort', 'Merge sort', 'Insertion sort', 'Counting sort', 'Block sort', 'Quick sort', 'Cocktail sort', 
        'Pigeonhole sort', 'Shell sort', 'Gnome sort', 'Odd even sort', 'Comb sort', 'Selection sort', 'Cycle sort', 'Heap sort',
        'Radix sort LSD']


for i in range(len(names)):
    buttons_c1.append(Button(names[i], x, y, x2, y2))
    y=y+30
    

shuffle_button = Button('Shuffle', 200, 20, 100, 23)
new_data_button = Button('New data', 350, 20, 100, 23)
stop_button = Button('Stop', 500, 20, 100, 23)
data_size_button = Button('Data size', 900, 10, 100, 23)
subs_button = Button('-', 890, 44, 50, 23)
add_button = Button('+', 960, 44, 50, 23)

back_rects = []
back_rects.append(Background_rects((221, 255, 247), 0, 0, 150, 700))
back_rects.append(Background_rects((221, 255, 247), 0, 0, 1400, 81))
back_rects.append(Background_rects((221, 255, 247), 1200, 50, 1300, 700))
back_rects.append(Background_rects((221, 255, 247), 150, 81, 4, 700))
back_rects.append(Background_rects((90, 215, 241), 150, 81, 4, 700))
back_rects.append(Background_rects((90, 215, 241), 1200, 81, 4, 700))
back_rects.append(Background_rects((90, 215, 241), 150, 81, 1050, 4))
back_rects.append(Background_rects((90, 215, 241), 150, 696, 1050, 4))
back_rects.append(Background_rects((255, 216, 216), 850, 40, 200, 30)) 
back_rects.append(Background_rects((255, 216, 216), 850, 40, 200, 30)) 

rects_len = len(back_rects)
#---------------------------------------------------------------------------------------------------------------------------------
#drawing function

def drawing(data, x):

    MARGIN = 0
    pygame.draw.rect(SCREEN, (0,0,0), [154,85,1046,611])

    d = len(data)
    BLOCK_WIDTH = 10
    BLOCK_HEIGHT = 1
    
    if x == 1:    
        draw_text('Data shuffling...', font, (255, 255, 255), SCREEN, 600, 90)
    elif x == 2:    
        draw_text('Data sorting...', font, (255, 255, 255), SCREEN, 600, 90)
    
    pygame.display.update()
        
    
    for i in range(d):
        x_coord = (BLOCK_WIDTH+MARGIN)*i+180
        y_coord = BLOCK_HEIGHT+MARGIN+120
        pygame.draw.rect(SCREEN, data_color[i], [x_coord, y_coord, 
                        BLOCK_WIDTH, BLOCK_HEIGHT*data[i]+0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    pygame.display.flip()
    pygame.time.delay(15)


#---------------------------------------------------------------------------------------------------------------------------------
#auxiliary functions


def check(data):

    leng = len(data)

    for i in range(leng):
        if data[i]>data[i+1]: return False
    
    return True



def swap(data, i, j):

    pom = data[i]
    data[i] = data[j] 
    data[j] = pom
    return data



def move_to_the_right(data, i, pivot):

    x = data[i]

    for j in range(i+1, pivot+1):
        data[j-1] = data[j]
    data[pivot] = x
    return data



def move_to_the_left(data, i, pivot):

    x = data[i]
    j=i

    while j > pivot:
        data[j] = data[j-1]
        j = j-1
    data[pivot] = x
    return data



def shuffle(data, data2): 

    s=len(data)

    for i in range(s):
        for j in range(s):
            if data[i] == data2[j]:
                swap(data, i, j)
                data_color[i] = colors[1]
                drawing(data, 1)
                data_color[i] = colors[0]
                drawing(data, 1)
                break

    drawing(data, 0)

#---------------------------------------------------------------------------------------------------------------------------------
#sorting algorithms

def bubble_sort(data):

    drawing(data, 2)
    s=len(data) 
    change = False

    for i in range(s):
        change = False
        for j in range(0, s - 1):
            data_color[j] = colors[1]
            data_color[j + 1] = colors[1]
            drawing(data, 2)
            if data[j] > data[j+1]: 
                change = True
                swap(data, j, j+1)
                data_color[j] = colors[2]
                data_color[j + 1] = colors[2]
                drawing(data, 2)
            data_color[j] = colors[0]
            data_color[j + 1] = colors[0]
            drawing(data, 2)
        if change == False: break

    return data



def merge_sort(data, x, y):

    if x<y: #jesli x==y to znaczy, ze sprawdzamy dla 1 elementu,a 1 elem jest juz posortowany

        middle = (x+y)//2

        merge_sort(data, x, middle)
        merge_sort(data, middle+1, y)

        x1=x #x1 i x2 to poczatki fragmentow porownywanych
        y1=middle #y1 i y2 to konce fragmentow porownywanych
        x2=middle+1
        y2=y

        sorted_data=[]
        p=x1
        q=x2

        while p<=y1 or q<=y2:
            if p<=y1 and q<=y2:
                data_color[p] = colors[1]
                data_color[q] = colors[1]
                drawing(data, 2)
                data_color[p]=colors[0]
                data_color[q]=colors[0]
                drawing(data, 2)
                if data[p]<data[q]:
                    sorted_data.append(data[p])
                    p=p+1
                else:
                    sorted_data.append(data[q])
                    q=q+1
            if p<=y1 and q>y2:
                sorted_data.append(data[p])
                p=p+1
            if p>y1 and q<=y2:
                sorted_data.append(data[q])
                q=q+1

        data[x:y+1] = sorted_data
        drawing(data, 2)
    



def insertion_sort(data):

    for i in range(1, len(data)):
        j=i
        while j>0:

            data_color[j] = colors[1]
            data_color[j-1] = colors[1]
            drawing(data, 2)

            if data[j] < data[j-1]:
                data_color[j] = colors[2]
                data_color[j-1] = colors[2]
                drawing(data, 2)
                swap(data, j, j-1)
                data_color[j] = colors[0]
                data_color[j-1] = colors[0]
                drawing(data, 2)
            else: 
                data_color[j] = colors[0]
                data_color[j-1] = colors[0]
                drawing(data, 2)
                break

            j=j-1

    return data



def counting_sort(data, data_2, ver):

    def histogram_creator(data, data_2):

        s_1 = len(data)
        max_element = max(data)
        min_element = min(data)
        elements = [i for i in range(min_element, max_element+1)]
        s_2 = len(elements)
        quantity = [0] * s_2

        for i in range(s_2):
            for j in range(s_1):
                if elements[i] == data[j]:
                    quantity[i] = quantity[i] + 1
                    data_color[j] = colors[2]
                    drawing(data_2, 2)
                    data_color[j] = colors[0]
                    drawing(data_2, 2)

        histogram = dict(zip(elements, quantity))
        del elements, quantity, max_element, min_element, s_1, s_2

        return histogram


    histogram = histogram_creator(data, data_2)
    i = 0

    if ver == 1:
        for key in histogram.keys():
            while histogram[key] != 0:
                data[i] = key
                histogram[key] = histogram[key] - 1
                i = i + 1  
                drawing(data, 2)

    else:
        for key in histogram.keys():
            while histogram[key] != 0:
                data[i] = key
                histogram[key] = histogram[key] - 1
                i = i + 1

    return data



def block_sort(data): pass


def quick_sort(data, begin, pivot):

    i = pivot - 1


    while(i>=begin):

        data_color[pivot] = colors[1]
        data_color[i] = colors[1]
        drawing(data, 2)

        if data[i] > data[pivot]:
            data_color[pivot] = colors[2]
            data_color[i] = colors[2]
            drawing(data, 2)
            data_color[pivot] = colors[0]
            data_color[i] = colors[0]
            data = move_to_the_right(data, i, pivot)
            pivot = pivot - 1
            data_color[pivot] = colors[1]
            drawing(data, 2)
        else: 
            data_color[i] = colors[0]
            i = i-1


    data_color[pivot] = colors[0]
    if len(data[begin:pivot-1])>=1: quick_sort(data, begin, pivot - 1)        
    if len(data[pivot+1:len(data)-1])>=1: quick_sort(data, pivot + 1, len(data)-1)        

    return data



def cocktail_sort(data):

    s = len(data)
    p=0
    q=s-1

    while p<=q:
        change=False

        for j in range(p, q):
            data_color[j] = colors[1]
            data_color[j+1] = colors[1]
            drawing(data, 2)
            if data[j] > data[j+1]:
                change=True
                data_color[j] = colors[2]
                data_color[j+1] = colors[2]
                drawing(data, 2)
                swap(data, j, j+1)
            data_color[j] = colors[0]
            data_color[j+1] = colors[0]
            drawing(data, 2)

        q=q-1

        for j in range(q,p,-1):

            data_color[j] = colors[1]
            data_color[j-1] = colors[1]
            drawing(data, 2)

            if data[j] < data[j-1]:
                change=True
                data_color[j] = colors[2]
                data_color[j-1] = colors[2]
                drawing(data, 2)
                swap(data, j, j-1)

            data_color[j] = colors[0]
            data_color[j-1] = colors[0]
            drawing(data, 2)

        p=p+1

        if change == False: break

    return data



def pigeonhole_sort(data):
    
    lim_1 = min(data)
    lim_2 = max(data)
    pigeonholes = {}
    leng = len(data)

    for i in range(lim_1, lim_2+1):
        pigeonholes[i] = []

    for i in range(leng):
        data_color[i] = colors[2]
        drawing(data,2)
        pigeonholes[data[i]].append(data[i])
        data_color[i] = colors[0]
        drawing(data, 2)

    index = 0
    
    for i in range(lim_1, lim_2+1):

        if pigeonholes[i] != []:
            leng_2 = len(pigeonholes[i])
            data[index:index+leng_2] = pigeonholes[i]
            data_color[index:index+leng_2] = [colors[2]]*(leng_2)
            drawing(data, 2)
            data_color[index:index+leng_2] = [colors[0]]*(leng_2)
            #drawing(data, 2)
            index = index+leng_2


    del pigeonholes, index, lim_1, lim_2

    return data



def shell_sort(data):

    k = 2
    s = len(data)
    gap = s

    while gap > 1:

        gap = int(s/k)

        for i in range(gap, s):
            j = i
            while j>0:
           
                data_color[j] = colors[1]
                data_color[j-gap] = colors[1]
                drawing(data, 2)

                if data[j] < data[j-gap]:
                    data_color[j] = colors[2]
                    data_color[j-gap] = colors[2]
                    drawing(data, 2)
                    swap(data, j, j-gap)
                    data_color[j] = colors[0]
                    data_color[j-gap] = colors[0]
                    drawing(data, 2)
                else: 
                    data_color[j] = colors[0]
                    data_color[j-gap] = colors[0]
                    drawing(data, 2)
                    break

                j = j-gap

        k = k*2

    return data



def gnome_sort(data):

    s=len(data)
    j=1

    while(j<s):
        
        if j!=0 and data[j] < data[j-1]:
            data_color[j] = colors[1]
            data_color[j] = colors[1]
            drawing(data,2)
            data_color[j] = colors[2]
            data_color[j-1] = colors[2]
            drawing(data,2)
            swap(data, j, j-1)
            data_color[j] = colors[0]
            data_color[j-1] = colors[0]
            drawing(data,2)
            j = j-1
            continue
        elif j!=0: 
            data_color[j] = colors[1]
            data_color[j-1] = colors[1]
            drawing(data,2)
            data_color[j] = colors[0]
            data_color[j-1] = colors[0]
            drawing(data,2)
        else:
            data_color[j] = colors[1]
            drawing(data,2)
            data_color[j] = colors[0]
            drawing(data,2)
        j = j+1
    return data



def odd_even_sort(data):

    s = len(data)
    sorted = False

    while(not sorted):
        sorted = True

        for i in range(0, s-1, 2):
            data_color[i] = colors[1]
            data_color[i+1] = colors[1]
            drawing(data, 2)
            if data[i] > data[i+1]:
                data_color[i] = colors[2]
                data_color[i+1] = colors[2]
                drawing(data, 2)
                swap(data, i, i+1)
                sorted = False
            data_color[i] = colors[0]
            data_color[i+1] = colors[0]
            drawing(data, 2)

        for i in range(1, s-1, 2):
            data_color[i] = colors[1]
            data_color[i+1] = colors[1]
            drawing(data, 2)
            if data[i] > data[i+1]:
                data_color[i] = colors[2]
                data_color[i+1] = colors[2]
                drawing(data, 2)
                swap(data, i, i+1)
                sorted = False
            data_color[i] = colors[0]
            data_color[i+1] = colors[0]
            drawing(data, 2)

    return data



def comb_sort(data):

    s = len(data)
    gap = s
    swapped = True

    while gap > 1 or swapped:

        gap = int(gap/1.3)
        swapped = False

        for i in range(s-gap):
            data_color[i] = colors[1]
            data_color[i+gap] = colors[1]
            drawing(data, 2)
            if data[i] > data[i+gap]:
                data_color[i] = colors[2]
                data_color[i+gap] = colors[2]
                drawing(data, 2)
                swap(data, i, i+gap)
                swapped = True
            data_color[i] = colors[0]
            data_color[i+gap] = colors[0]
            drawing(data, 2)

    return data



def selection_sort(data):

    s = len(data)

    for lim in range(s-1):

        idx_mini = lim
        data_color[idx_mini] = colors[1]
        drawing(data, 2)

        for j in range(lim+1, s):
            data_color[j] = colors[1]
            drawing(data, 2)
            if data[j] < data[idx_mini]:
                    data_color[j] = colors[2]
                    data_color[idx_mini] = colors[2]
                    drawing(data, 2)
                    data_color[idx_mini] = colors[0]
                    idx_mini = j
                    data_color[idx_mini] = colors[1]
                    drawing(data, 2)
            else:
                data_color[j] = colors[0]
                drawing(data, 2)
        data_color[idx_mini] = colors[0]
        drawing(data, 2)
        data = move_to_the_left(data, idx_mini, lim)
        drawing(data, 2)

    return data



def cycle_sort(data):

    data.insert(0,0) #in this cell the moved element will be here
    s = len(data)

    for start in range(1, s-1):

        position = start
        data[0] = data[start]
        data_color[position] = colors[3]
        data_color[0] = colors[1]

        for j in range(start+1, s):

            data_color[j] = colors[1]
            drawing(data,2)

            if data[0] > data[j]: 
                data_color[j] = colors[2]
                data_color[position] = colors[0]
                position = position+1
                data_color[position] = colors[3]
                drawing(data, 2)

            data_color[j] = colors[0]
            drawing(data, 2)
                    

        if position == start:
            data_color[position] = colors[0]
            drawing(data, 2)
            continue

        while data[position] == data[0]:
            data_color[position] = colors[0]
            position = position+1
            data_color[position] = colors[3]
            drawing(data, 2)

        data[position], data[0] = data[0], data[position]
        data_color[position] = colors[0]
        drawing(data, 2)


        while position != start:

            position = start
            data_color[position] = colors[3]


            for j in range(start+1, s):

                data_color[j] = colors[1]
                drawing(data, 2)

                if data[0] > data[j]:
                    data_color[j] = colors[2]
                    data_color[position] = colors[0]
                    position = position+1
                    data_color[position] = colors[3]
                    drawing(data, 2)

                data_color[j] = colors[0]
                drawing(data, 2)
            
    
            while data[position] == data[0]:
                data_color[position] = colors[0]
                position = position+1
                data_color[position] = colors[3]
                    
            data[position], data[0] = data[0], data[position] 
            data_color[position] = colors[0]
            drawing(data, 2)


    data = data[1:]
    return data

    

def heap_sort(data):

    def build_heap(data, lim):
        #drawing(data, 2)
        heap_range = 0
        leng = len(data[0:(lim+1)])
        i = 1

        while heap_range < leng-1:

            i = heap_range+1
            j = (i-1)//2
            place = False

            while j > 0:
                data_color[i] = colors[1]
                data_color[j] = colors[1]
                drawing(data, 2)
                if data[j]>data[i]:
                    data_color[j] = colors[2]
                    data_color[i] = colors[2]
                    drawing(data, 2)
                    swap(data, i, j)                    
                    data_color[j] = colors[0]
                    data_color[i] = colors[0]
                    drawing(data, 2)
                    i = j
                    j = (j-1)//2
                    continue

                data_color[i] = colors[0]
                data_color[j] = colors[0]
                drawing(data, 2)
                if i==j: break
                place = True
                break 

            if place == False:
                data_color[i] = colors[1]
                data_color[0] = colors[1]
                drawing(data, 2)
                if data[0] > data[i]: 
                    data_color[i] = colors[2]
                    data_color[0] = colors[2]
                    drawing(data, 2)
                    swap(data, 0, i)
                data_color[i] = colors[0]
                data_color[0] = colors[0]
             #   drawing(data, 2)
                
            heap_range = heap_range+1
    

    leng = len(data)
    build_heap(data, leng-1)
    
    for i in range(leng+1):
        move_to_the_right(data, 0, leng-1)
        drawing(data, 2)
        build_heap(data, leng-i-1)

    return data



def radix_sort_LSD(data):

    leng = len(data)


    def sorting_by_pos(data, pos):


        def create_digit_dict(data, digits):
            digit_dict = {}
            for i in range(leng):
                digit = digits[i]
                if digit not in digit_dict.keys():
                    digit_dict[digit] = [data[i]]
                else:
                    digit_dict[digit].append(data[i])
            
            return digit_dict


        change = False
        digits = [(data[i]//pos)%10 for i in range(leng)]

        for digit in digits: 
            if digit != 0: 
                change = True
                break

        if change:                  
            digit_dict = create_digit_dict(data, digits)
            counting_sort(digits, data, 2)
            
            index=0
            lim_1 = min(digits)
            lim_2 = max(digits)

            for key in range(lim_1, lim_2+1):
                if key in digit_dict.keys():
                    leng_2 = len(digit_dict[key])
                    for j in range(leng_2):
                        data[index] = digit_dict[key][j]
                        data_color[index] = colors[1]
                        drawing(data, 2)
                        data_color[index] = colors[0]
                        index+=1
            
            del lim_1, lim_2, leng_2, index
            del digit_dict
            del digits

        return data, change


    position = 1
    position_zero = True

    while position_zero:
        position_zero = False
        data, position_zero = sorting_by_pos(data, position)
        position = position*10

    return data

#---------------------------------------------------------------------------------------------------------------------------------
#main and user choices

def choice(user_choice, data, data2, data_color):       

    if user_choice == buttons_c1[0].shape: data = bubble_sort(data)
    elif user_choice == buttons_c1[1].shape: merge_sort(data, 0, len(data)-1)
    elif user_choice == buttons_c1[2].shape: data = insertion_sort(data)
    elif user_choice == buttons_c1[3].shape: data = counting_sort(data, data, 1)
    elif user_choice == buttons_c1[4].shape: data = block_sort(data)
    elif user_choice == buttons_c1[5].shape: data = quick_sort(data, 0, len(data)-1)
    elif user_choice == buttons_c1[6].shape: data = cocktail_sort(data)
    elif user_choice == buttons_c1[7].shape: data = pigeonhole_sort(data)
    elif user_choice == buttons_c1[8].shape: data = shell_sort(data)
    elif user_choice == buttons_c1[9].shape: data = gnome_sort(data)
    elif user_choice == buttons_c1[10].shape: data = odd_even_sort(data)
    elif user_choice == buttons_c1[11].shape: data = comb_sort(data)
    elif user_choice == buttons_c1[12].shape: data = selection_sort(data)
    elif user_choice == buttons_c1[13].shape: data = cycle_sort(data)
    elif user_choice == buttons_c1[14].shape: data = heap_sort(data)
    elif user_choice == buttons_c1[15].shape: data = radix_sort_LSD(data)
    #elif user_choice == buttons_c1[16].shape: (data)

    elif user_choice == add_button.shape:
        if len(data)<=70:
            data.append(random.randrange(1,200))
            data_color.append(colors[0])
            drawing(data, 0)
            del data2
            data2=deepcopy(data)
        else: print("The data limit is 200 elements.")

    elif user_choice == subs_button.shape: 
        if len(data)>=1:
            data=data[0:-1]
            del data_color
            data_color = data_color[0:-1]
            del data2
            data2=deepcopy(data)
            drawing(data, 0)
        else: print("The data array must contain at least one element.")

    elif user_choice == shuffle_button.shape: shuffle(data, data2)
    elif user_choice == new_data_button.shape: 
        data, data2 = generate_data(len(data))
        drawing(data,0)
    


    s=len(data)

    for i in range(s):
        data_color[i] = colors[2]
        drawing(data, 0)

    for i in range(s):
        data_color[i] = colors[0]

    drawing(data, 0)

    return data, data2, data_color



def main():

    global data, data2, data_color, colors
    drawing(data, 0)

    while True:


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                del data, data2, data_color, colors
                exit()


            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    data, data2, data_color=choice(event.ui_element, data, data2, data_color)
                    drawing(data,0)

            manager.process_events(event)

        manager.update(60)

        for i in range(rects_len):
            back_rects[i].draw_rect()

        manager.draw_ui(SCREEN)

        pygame.display.update()
        clock.tick(60)



if __name__ == "__main__":
    main()