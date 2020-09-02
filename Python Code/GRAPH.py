# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:38:45 2020

@author: Admin
"""
import pygame
import queue

clock = pygame.time.Clock()
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Play with graphs!")

left_background = pygame.image.load('background.png')
node1 = pygame.image.load('r_circle.png')
node2 = pygame.image.load('b_circle.png')
plus = pygame.image.load('plus.png')
add = pygame.image.load('add.png')
cross = pygame.image.load('cross.png')
algo_button = pygame.image.load('algo_button.png')

button_font = pygame.font.Font('MountainBridge.otf', 20)
msg_font = pygame.font.Font('roboto.ttf', 15)

add_node = button_font.render('Add Nodes', True, WHITE)
add_edge = button_font.render('Add Edges', True, WHITE)
dfs_button = button_font.render('DFS', True, WHITE) 
bfs_button = button_font.render('BFS', True, WHITE)
mst_button = button_font.render('Find MST', True, WHITE)
djikstra_button = button_font.render('Djikstra', True, WHITE) 
msg_box = msg_font.render('', True, BLUE);

node_button = plus
edge_button = add
nodes = []
edges = []
weight = []
yellow_edges = []
color = [node2,node1]
node_color = []
pos = (-1,-1)
pointA = -1
pointB = -1
point = -1
state = 'start'
msg = ''

def dfs(s,vis,adj):
    vis[s] = 1
    node_color[s] = color[1]
    show_edges()
    show_nodes()
    pygame.display.update()
    pygame.time.delay(200)
    for i in range(len(adj[s])):
        if vis[adj[s][i]] != 1:
            yellow_edges.append((s,adj[s][i]))
            yellow_edges.append((adj[s][i],s))
            show_edges()
            show_nodes()
            pygame.display.update()
            pygame.time.delay(200)
            dfs(adj[s][i],vis,adj)

def start_dfs(point):
    if(len(nodes)==0 or len(edges)==0):
        return
    adj = [[] for i in range(len(nodes))]
    vis = [0 for i in range(len(nodes))]
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1])
    dfs(point,vis,adj)

def bfs(s,dis,adj):
    level = 0
    q = queue.Queue()
    q.put((level,s))
    global screen,nodes
    dis[s] = 0
    node_color[s] = color[1]
    show_edges()
    show_nodes()
    pygame.display.update()
    pygame.time.delay(200)
    
    while not q.empty():
        f = q.queue[0];
        if(f[0] == (level+1)%2):
            level = (level+1)%2
            continue
        q.get()
        u = f[1]
        for i in range(len(adj[u])):
            if dis[adj[u][i]] == 1e9:
                yellow_edges.append((u,adj[u][i]))
                yellow_edges.append((adj[u][i],u))
                node_color[adj[u][i]] = color[1]
                show_edges()
                show_nodes()
                pygame.display.update()
                pygame.time.delay(200)
                dis[adj[u][i]] = dis[u] + 1
                q.put(((level+1)%2,adj[u][i]))
    
def start_bfs(point):
    if(len(nodes)==0 or len(edges)==0):
        return
    adj = [[] for i in range(len(nodes))]
    dis = [1e9 for i in range(len(nodes))]
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1])
    bfs(point,dis,adj)
    
def getNode(mos_x,mos_y):
    for i in range(len(nodes)):
        x1 = nodes[i][0]
        y1 = nodes[i][1]
        if isClicked(x1, y1, x1 + node2.get_width(), y1 + node2.get_height(), mos_x, mos_y):
            return i
    return -1

def make_equal(listA, listB):
    for i in range(len(listA)):
        listA[i] =listB[i]

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

def show_nodes():
    if(len(nodes)==0): return
    for i in range(len(nodes)):
        screen.blit(node_color[i],nodes[i])

def show_edges():
    if(len(edges)==0): return
    for i in range(len(edges)):
            pygame.draw.line(screen,BLACK,(nodes[edges[i][0]][0]+16,nodes[edges[i][0]][1]+16),(nodes[edges[i][1]][0]+16,nodes[edges[i][1]][1]+16),1)
    for i in range(len(yellow_edges)):
            pygame.draw.line(screen,YELLOW,(nodes[yellow_edges[i][0]][0]+16,nodes[yellow_edges[i][0]][1]+16),(nodes[yellow_edges[i][1]][0]+16,nodes[yellow_edges[i][1]][1]+16),1)
 
def show_buttons():
    if(state == 'start'):
        screen.blit(algo_button,(7,550))
        screen.blit(djikstra_button,(7+algo_button.get_width()/2-30,550+algo_button.get_height()/2-10))
        screen.blit(algo_button,(7,498))
        screen.blit(dfs_button,(7+algo_button.get_width()/2-20,498+algo_button.get_height()/2-10))
        screen.blit(algo_button,(7,446))
        screen.blit(bfs_button,(7+algo_button.get_width()/2-20,446+algo_button.get_height()/2-10))
        screen.blit(algo_button,(7,394))
        screen.blit(mst_button,(7+algo_button.get_width()/2-40,394+algo_button.get_height()/2-10))
        
def show_msg():
    msg_box = msg_font.render(msg, True, BLUE);
    screen.blit(msg_box,(215,570))
    
running = True

while running:
    screen.fill(WHITE)
    screen.blit(left_background,(0,0))
    
    if(state == 'start' or state == 'add_node'):
        screen.blit(node_button,(5,5))
        
    if(state == 'start' or state == 'add_edge1' or state == 'add_edge2'):
        screen.blit(edge_button,(5,42))
        
    show_buttons()
    show_msg()
    if state == 'start':
        node_button = plus
        edge_button = add
        if(ishovering(5,5,5+node_button.get_width(),5+node_button.get_height())):
            screen.blit(add_node,(60,12))
        if(ishovering(5,42,5+edge_button.get_width(),42+edge_button.get_height())):
            screen.blit(add_edge,(60,48))
            
    if state == 'dfs':
        temp_node = [color[0] for i in range(len(node_color))]
        make_equal(temp_node,node_color)
        start_dfs(point)
        make_equal(node_color,temp_node)
        yellow_edges.clear()
        state = 'start'  
        point = -1
        
    if state == 'bfs':
        temp_node = [color[0] for i in range(len(node_color))]
        make_equal(temp_node,node_color)
        start_bfs(point)
        make_equal(node_color,temp_node)
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
                    if(isClicked(7,498,7+algo_button.get_width(),498+algo_button.get_height(),pos[0],pos[1])):
                        if len(nodes) != 0:
                            state = 'choose start point for dfs'
                            msg = 'Choose source for the Depth First Search.'
                        else: state = 'start'
                    elif(isClicked(5,5,5+node_button.get_width(),5+node_button.get_height(),pos[0],pos[1])):
                        state = 'add_node'
                        msg = 'Click on the screen to add a node there.'
                        node_button = cross
                        edge_button = cross
                    elif(isClicked(5,42,5+edge_button.get_width(),42+edge_button.get_height(),pos[0],pos[1])):
                        msg = 'Choose initial vertex of the edge.'
                        state = 'add_edge1'
                        node_button = cross
                        edge_button = cross
                    elif(isClicked(7,446,7+algo_button.get_width(),446+algo_button.get_height(),pos[0],pos[1])):
                        if len(nodes) != 0:
                            state = 'choose start point for bfs'
                            msg = 'Choose source for the Breadth First Search.'
                        else: state = 'start'
                elif state == 'add_node':
                    if pos[0]>200 and pos[1]<550:
                        nodes.append((pos[0]-16,pos[1]-16))
                        node_color.append(color[0])
                    if(isClicked(5,5,5+node_button.get_width(),5+node_button.get_height(),pos[0],pos[1])):
                        state = 'start'
                        msg = ''
                elif state == 'add_edge1':
                    pointA = getNode(pos[0],pos[1])
                    if(pointA != -1):
                        state = 'add_edge2'
                        msg = 'Choose terminal vertex of the edge.'
                    if(isClicked(5,42,5+edge_button.get_width(),42+edge_button.get_height(),pos[0],pos[1])):
                        state = 'start'
                        msg = ''
                elif state == 'add_edge2':
                    pointB = getNode(pos[0],pos[1])
                    if pointB != -1 and pointB != pointA:
                        edges.append((pointA,pointB))
                        edges.append((pointB,pointA))
                        state = 'add_edge1'
                        msg = 'Choose initial vertex of the edge.'
                        pointA = -1
                        pointB = -1
                    if(isClicked(5,42,5+edge_button.get_width(),42+edge_button.get_height(),pos[0],pos[1])):
                        state = 'start'
                        msg = ''
                elif state == 'choose start point for dfs':
                    point  = getNode(pos[0],pos[1])
                    if point != -1:
                        state = 'dfs'
                        msg = ''
                elif state == 'choose start point for bfs':
                    point  = getNode(pos[0],pos[1])
                    if point != -1:
                        state = 'bfs'
                        msg = ''
            pos = (-1,-1)
            
    show_edges()
    show_nodes()
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
