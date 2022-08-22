# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:38:45 2020

@author: Admin
"""
from platform import node
import pygame
import queue
from .textInput import write_text
clock = pygame.time.Clock()
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Dijkstra algorithm!")

left_background = pygame.image.load('visualization/background.png')
node1 = pygame.image.load('visualization/r_circle.png')
node2 = pygame.image.load('visualization/b_circle.png')
node3 = pygame.image.load('visualization/y_circle.png')
cross = pygame.image.load('visualization/cross.png')
algo_button = pygame.image.load('visualization/algo_button.png')

button_font = pygame.font.Font('visualization/roboto.ttf', 20)
msg_font = pygame.font.Font('visualization/roboto.ttf', 15)

dijkstra_button = button_font.render('Choose', True, WHITE)
go_button = button_font.render('Go', True, WHITE)
msg_box = msg_font.render('', True, BLUE)

nodes = [[317, 257], [433, 137], [538, 255], [424, 380], [672, 135], [664, 380], [771, 261]]
nodes_name = ['NMN. sông Hồng', 'NMN. Cáo Đỉnh', 'NMN. Ngọc Hà',
              'NMN. Mai Dịch', 'NMN. Yên Phụ', 'NMN. Ngô Sỹ Liên', 'NMN. Lương Yên']
edges = [(0, 1), (0, 3), (0, 2), (3, 2), (2, 4),
         (2, 5), (5, 6), (4, 6), (1, 2), (3, 5)]
blue_edges = []
weight_edges = [14.1, 16.8, 18.6, 2.4, 5.2, 4.3, 5.4, 5.3, 6.3, 7.8]
color = [node2, node1, node3]
node_color = [color[0], color[0], color[0],
              color[0], color[0], color[0], color[0]]
adj_from_pointA = [[] for i in range(len(nodes))]
dis_from_pointA = [1e9 for i in range(len(nodes))]
pos = (-1, -1)
pointA = -1
pointB = -1
point = -1
state = 'start'
msg = ''
user_text = ''

def showNodeName(index):
    return nodes_name[index]

def dijkstra(pointA, pointB, dis, adj):
    if(pointA == pointB):
        return
    level = 0
    q = queue.Queue()
    q.put((level, pointA))
    global screen, nodes, msg
    node_color[pointA] = color[1]
    show_edges()
    show_nodes()
    show_nodes_name()
    show_weight_edges()
    pygame.display.update()
    pygame.time.delay(200)

    while not q.empty():
        f = q.queue[0]
        if(f[0] == (level+1) % 2):
            level = (level+1) % 2
            continue
        q.get()
        u = f[1]
        for i in range(len(adj[u])):
            blue_edges.append((u, adj[u][i]))
            node_color[adj[u][i]] = color[1]
            show_edges()
            show_nodes()
            pygame.display.update()
            pygame.time.delay(200)
            print("START****")
            if(dis_from_pointA[adj[u][i]] <= dis_from_pointA[u] + weight_edges[edges.index((u, adj[u][i]))]):
                continue
                
            print("current node: ",u)
            print("related node: ",adj[u][i])
            adj_from_pointA[adj[u][i]] = adj_from_pointA[u][:]
            adj_from_pointA[adj[u][i]].append(adj[u][i])
            # Pricing to go related node
            dis_from_pointA[adj[u][i]] = dis_from_pointA[u] + weight_edges[edges.index((u, adj[u][i]))]
            print("price to go related node: ",dis_from_pointA[adj[u][i]])
            print("current step to go to related node: ")
            print(adj_from_pointA)
            print("END****")
            
            q.put(((level+1) % 2, adj[u][i]))
    msg = 'Success find route!'
    print('Done.... ')
    if(len(adj_from_pointA[pointB]) == 0):
        msg = 'No route find!'
    else:
        best_route = str([nodes_name[index] for index in adj_from_pointA[pointB]])
        best_price = str(round(dis_from_pointA[pointB],2))
        msg = 'Route: ' + best_route + '\n' + 'Best total distance: ' + str(best_price)
        print('Return best route: ')
        print(best_route)
        print('Total price to go to best route: ')
        print(best_price)


def start_dijkstra(pointA, pointB):
    if(len(nodes) == 0 or len(edges) == 0):
        return
    adj = [[] for i in range(len(nodes))]
    dis = [[] for i in range(len(nodes))]
    
    adj_from_pointA[pointA] = [pointA]
    dis_from_pointA[pointA] = 0
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1])
        dis[edges[i][0]].append(weight_edges[i])
    print("Cách cạnh nối tới các điểm đến <edges>:")
    print(edges)
    print("Các điểm mà nó được kết nối tới (ứng với trị ví mảng) <adj>:")
    print(adj)
    print("Khoảng cách của các điểm mà nó được kết nối tới (ứng với trị ví mảng) <dis>:")
    print(dis)
    dijkstra(pointA, pointB, dis, adj)
def make_equal(listA, listB):
    for i in range(len(listA)):
        listA[i] = listB[i]


def isClicked(x1, y1, x2, y2, mos_x, mos_y):
    if mos_x > x1 and (mos_x < x2):
        x_inside = True
    else:
        x_inside = False
    if mos_y > y1 and (mos_y < y2):
        y_inside = True
    else:
        y_inside = False
    if x_inside and y_inside:
        return True
    else:
        return False


def ishovering(x1, y1, x2, y2):
    mos_x, mos_y = pygame.mouse.get_pos()
    if mos_x > x1 and (mos_x < x2):
        x_inside = True
    else:
        x_inside = False
    if mos_y > y1 and (mos_y < y2):
        y_inside = True
    else:
        y_inside = False
    if x_inside and y_inside:
        return True
    else:
        return False


def getNode(mos_x, mos_y):
    for i in range(len(nodes)):
        x1 = nodes[i][0]
        y1 = nodes[i][1]
        if isClicked(x1, y1, x1 + node2.get_width(), y1 + node2.get_height(), mos_x, mos_y):
            return i
    return -1


def show_nodes():
    if(len(nodes) == 0):
        return
    for i in range(len(nodes)):
        screen.blit(node_color[i], nodes[i])


def show_weight_edges():
    if(len(edges) == 0):
        return
    for i in range(len(edges)):
        # write node text
        text_surface = msg_font.render(str(weight_edges[i]), True, (0, 0, 0))
        screen.blit(text_surface, ((nodes[edges[i][0]][0]+16 + nodes[edges[i][1]]
                    [0]+16) / 2, (nodes[edges[i][0]][1]+16 + nodes[edges[i][1]][1]+16) / 2))

def show_dijkstra_result():
    if pointA != -1 and pointB != -1:
       screen.blit(node3, nodes[pointA])
       screen.blit(node3, nodes[pointB])
       for i in range(len(adj_from_pointA[pointB])):
        screen.blit(node3, nodes[adj_from_pointA[pointB][i]])
        if i < len(adj_from_pointA[pointB]) - 1:
            blue_edges.append((adj_from_pointA[pointB][i], adj_from_pointA[pointB][i+1]))

def show_nodes_name():
    if(len(nodes) == 0):
        return
    for i in range(len(nodes)):
        # write node text
        text_surface = msg_font.render(nodes_name[i], True, (0, 0, 0))
        screen.blit(text_surface, (nodes[i][0], nodes[i][1] + 30))


def show_edges():
    if(len(edges) == 0):
        return
    for i in range(len(edges)):
        pygame.draw.line(screen, BLACK, (nodes[edges[i][0]][0]+16, nodes[edges[i][0]]
                         [1]+16), (nodes[edges[i][1]][0]+16, nodes[edges[i][1]][1]+16), 1)
    for i in range(len(blue_edges)):
        pygame.draw.line(screen, BLUE, (nodes[blue_edges[i][0]][0]+16, nodes[blue_edges[i][0]]
                         [1]+16), (nodes[blue_edges[i][1]][0]+16, nodes[blue_edges[i][1]][1]+16), 1)


def show_buttons():
    if(state == 'start'):
        screen.blit(algo_button, (7, 342))
        screen.blit(dijkstra_button, (7+algo_button.get_width() /
                    2-70, 342+algo_button.get_height()/2-13))
        screen.blit(algo_button, (7, 550))
        screen.blit(go_button, (7+algo_button.get_width() /
                    2-53, 550+algo_button.get_height()/2-13))


def show_msg():
    msg_box = msg_font.render(msg, True, BLUE)
    screen.blit(msg_box, (215, 570))


def run():
    global screen, nodes, edges, blue_edges, color, node_color, pos, pointA, pointB, point, state, node_button, edge_button, msg, user_text, weight_edges, adj_from_pointA, dis_from_pointA
    running = True

    while running:
        screen.fill(WHITE)
        screen.blit(left_background, (0, 0))

        show_buttons()
        show_msg()



        if state == 'dijkstra':
            temp_node = [color[0] for i in range(len(node_color))]
            make_equal(temp_node, node_color)
            start_dijkstra(pointA, pointB)
            make_equal(node_color, temp_node)
            blue_edges.clear()
            state = 'start'
            point = -1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if(pos[0] != -1 & pos[1] != -1):
                    if state == 'start':
                        if(isClicked(7, 342, 7+algo_button.get_width(), 342+algo_button.get_height(), pos[0], pos[1])):
                            adj_from_pointA = [[] for i in range(len(nodes))]
                            dis_from_pointA = [1e9 for i in range(len(nodes))]
                            blue_edges.clear()
                            if len(nodes) > 1:
                                state = 'choose start point for dijkstra'
                                msg = 'Choose start point for dijkstra.'
                            else:
                                state = 'start'
                                msg = 'Require 2 point to start.'
                        elif(isClicked(7, 550, 7+algo_button.get_width(), 550+algo_button.get_height(), pos[0], pos[1])):
                            if pointA != -1 and pointB != -1:
                                state = 'dijkstra'
                                msg = 'Start running dijkstra algorithm.'
                            else:
                                state = 'start'
                                msg = 'Require 2 point to start.'
                    elif state == 'choose start point for dijkstra':
                        pointA = getNode(pos[0], pos[1])
                        if pointA != -1:
                            state = 'choose end point for dijkstra'
                            msg = 'Choose end point'
                    elif state == 'choose end point for dijkstra':
                        pointB = getNode(pos[0], pos[1])
                        if pointB != -1:
                            state = 'start'
                            msg = 'Success choose start and end point.'
                    elif state == 'exit':
                        if(isClicked(5, 5, 5+node_button.get_width(), 5+node_button.get_height(), pos[0], pos[1])):
                            make_equal(node_color, temp_node)
                            blue_edges.clear()
                            nodes_name.clear()
                            weight_edges.clear()
                            state = 'start'
                            msg = ''
                pos = (-1, -1)

        show_edges()
        show_nodes()
        show_nodes_name()
        show_weight_edges()
        show_dijkstra_result()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
