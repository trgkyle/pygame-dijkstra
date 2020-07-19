import pygame

clock = pygame.time.Clock()
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Play with graphs!")

left_background = pygame.image.load('back5.png')
node1 = pygame.image.load('red_circle1.png')
node2 = pygame.image.load('blue_circle1.png')
plus = pygame.image.load('plus.png').convert_alpha()
node_button = plus
add = pygame.image.load('add.png').convert_alpha()
edge_button = add
cross = pygame.image.load('cross.png').convert_alpha()
node_font = pygame.font.Font('MountainBridge.otf', 20)
edge_font = pygame.font.Font('MountainBridge.otf', 20)
dfs_font = pygame.font.Font('MountainBridge.otf', 20)
add_node = node_font.render('Add Nodes', True, WHITE)
add_edge = edge_font.render('Add Edges', True, WHITE)
DFS = pygame.image.load('green1.png').convert_alpha()
dfs_button = dfs_font.render('Do DFS', True, WHITE) 


nodes = []
edges = []
yellow_edges = []
color = [node2,node1]
tree_node = []
pos = (-1,-1)
pointA = -1
pointB = -1
point = -1
state = 'start'

def show_nodes():
    global nodes,node1,screen
    if(len(nodes)==0): return
    for i in range(len(nodes)):
        screen.blit(tree_node[i],nodes[i])

def show_edges():
    global nodes,screen,yellow_edges,edges
    if(len(edges)==0): return
    for i in range(len(edges)):
        if edges[i] not in yellow_edges:
            pygame.draw.line(screen,BLACK,(nodes[edges[i][0]][0]+16,nodes[edges[i][0]][1]+16),(nodes[edges[i][1]][0]+16,nodes[edges[i][1]][1]+16),1)
        else:
            pygame.draw.line(screen,YELLOW,(nodes[edges[i][0]][0]+16,nodes[edges[i][0]][1]+16),(nodes[edges[i][1]][0]+16,nodes[edges[i][1]][1]+16),1)

def ishovering(x1,y1,x2,y2):
    mos_x, mos_y = pygame.mouse.get_pos()
    if mos_x>x1 and (mos_x<x2):
        x_inside = True
    else: x_inside = False
    if mos_y>y1 and (mos_y<y2):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        return True
    else:
        return False

def dfs(s,vis,adj):
    global screen,nodes
    vis[s] = 1
    tree_node[s] = color[1]
    for i in range(len(adj[s])):
        if vis[adj[s][i]] != 1:
            yellow_edges.append((s,adj[s][i]))
            yellow_edges.append((adj[s][i],s))
            show_edges()
            show_nodes()
            pygame.display.update()
            pygame.time.delay(500)
            dfs(adj[s][i],vis,adj)

def start_dfs(point):
    global nodes,edges
    if(len(nodes)==0 or len(edges)==0):
        return
    adj = [[] for i in range(len(nodes))]
    vis = [0 for i in range(len(nodes))]
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1])
    dfs(point,vis,adj)

def isClicked(x1,y1,x2,y2,mos_x,mos_y):
    if mos_x>x1 and (mos_x<x2):
        x_inside = True
    else: x_inside = False
    if mos_y>y1 and (mos_y<y2):
        y_inside = True
    else: y_inside = False
    if x_inside and y_inside:
        return True
    else:
        return False

def getNode(mos_x,mos_y):
    global nodes,node2
    for i in range(len(nodes)):
        x1 = nodes[i][0]
        y1 = nodes[i][1]
        if isClicked(x1, y1, x1 + node2.get_width(), y1 + node2.get_height(), mos_x, mos_y):
            return i
    return -1

def make_equal(listA, listB):
    for i in range(len(listA)):
        listA[i] =listB[i]
   
running = True

while running:
    #print(state)
    screen.fill(WHITE)
    screen.blit(left_background,(0,0))
    
    if(state == 'start' or state == 'add_node'):
        screen.blit(node_button,(5,5))
        
    if(state == 'start' or state == 'add_edge1' or state == 'add_edge2'):
        screen.blit(edge_button,(5,42))
        
    if(state == 'start'):
        screen.blit(DFS,(30,400))
        screen.blit(dfs_button,(60,420))
        
    if state == 'start':
        node_button = plus
        edge_button = add
        if(ishovering(5,5,5+node_button.get_width(),5+node_button.get_height())):
            screen.blit(add_node,(60,12))
        if(ishovering(5,42,5+edge_button.get_width(),42+edge_button.get_height())):
            screen.blit(add_edge,(60,48))
            
    if state == 'dfs':
        temp_node = [color[0] for i in range(len(tree_node))]
        make_equal(temp_node,tree_node)
        start_dfs(point)
        make_equal(tree_node,temp_node)
        yellow_edges.clear()
        state = 'start'  
        point = -1
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break;
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if(pos[0]!=-1 & pos[1]!=-1):
                if state == 'start':
                    if(isClicked(30,400,30+DFS.get_width(),400+DFS.get_height(),pos[0],pos[1])):
                        state = 'choose start point for dfs'
                    elif(isClicked(5,5,5+node_button.get_width(),5+node_button.get_height(),pos[0],pos[1])):
                        state = 'add_node'
                        node_button = cross
                        edge_button = cross
                    elif(isClicked(5,42,5+edge_button.get_width(),42+edge_button.get_height(),pos[0],pos[1])):
                        state = 'add_edge1'
                        node_button = cross
                        edge_button = cross
                elif state == 'add_node':
                    if pos[0]>200:
                        nodes.append((pos[0]-16,pos[1]-16))
                        tree_node.append(color[0])
                    if(isClicked(5,5,5+node_button.get_width(),5+node_button.get_height(),pos[0],pos[1])):
                        state = 'start'
                elif state == 'add_edge1':
                    pointA = getNode(pos[0],pos[1])
                    if(pointA != -1):
                        state = 'add_edge2'
                    if(isClicked(5,42,5+edge_button.get_width(),42+edge_button.get_height(),pos[0],pos[1])):
                        state = 'start'
                elif state == 'add_edge2':
                    pointB = getNode(pos[0],pos[1])
                    if pointB != -1:
                        edges.append((pointA,pointB))
                        edges.append((pointB,pointA))
                        state = 'add_edge1'
                        pointA= -1
                        pointB = -1
                    if(isClicked(5,42,5+edge_button.get_width(),42+edge_button.get_height(),pos[0],pos[1])):
                        state = 'start'
                elif state == 'choose start point for dfs':
                    point  = getNode(pos[0],pos[1])
                    if point != -1:
                        state = 'dfs'
            pos = (-1,-1)
            
    show_edges()
    show_nodes()
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
