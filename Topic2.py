from math import sqrt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from csv import reader
from math import sqrt
import random
import pygame
import random
import sys
import math
from collections import deque
from typing import List, Any
import math

# region SearchAlgorithms
class Node:
    id = None  # Unique value for each node.
    up = None  # Represents value of neighbors (up, down, left, right).
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of neighbors.
    dash = False


    def __init__(self, value):
        self.value = value


class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes you need as long as the main
          structure is left as is '''
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.

    mazeNodes = []
    fullmazeNodes=[[]]
    n=[]
    def __init__(self, mazeStr):
        ''' mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node'''
        maze = [j.split(',') for j in mazeStr.split(' ')]
        # for i in range (len(maze)):
        #   print(maze[i])
        # ----------------------------------------------
        # for i in range(len(maze)):
        #    for j in range (len(maze[0])):
        #        print(maze[i][j], end=" ")
        #    print('\n')
        # -------------------------------
        rows=0
        for i in range(len(maze)):
            rows+=1
        columns=0
        for i in range(len(maze[0])):
            columns+=1
        ID = 0
        print("Number Of Rows = ",rows)
        print("Number Of Columns = ",columns)
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if (maze[i][j] == 'S'):
                    node = Node(maze[i][j])
                    node.id = ID
                    ID += 1
                    self.mazeNodes.append(node)
                elif (maze[i][j] == '.'):
                    node = Node(maze[i][j])
                    node.id = ID
                    ID += 1
                    self.mazeNodes.append(node)
                elif (maze[i][j] == '#'):
                    node = Node(maze[i][j])
                    node.id = ID
                    ID += 1
                    if (maze[i][j] == '#'):
                        node.dash = True
                    self.mazeNodes.append(node)
                elif (maze[i][j] == 'E'):
                    node = Node(maze[i][j])
                    node.id = ID
                    ID += 1
                    self.mazeNodes.append(node)
        #-------------------------------------
        print('\n')
        print("The Hole Maze In 1d Array[]")
        for i in range(len(self.mazeNodes)):
            print(self.mazeNodes[i].id,end="  ")
        print('\n')
        #print(rows)
        #print(columns)
        x=0
       # for y in range (len(self.mazeNodes)):#num Of Rows
        for i in range (rows):#num Of Rows
            for j in range(columns):#num Of Colunms
                self.n.append(self.mazeNodes[x])
                x+=1
            self.fullmazeNodes.append(self.n)
            self.n=[]
        self.fullmazeNodes.remove(self.fullmazeNodes[0])
        #for i in range(rows):  # num Of Rows
         #   for j in range(columns):  # num Of Colunms
          #      print(self.fullmazeNodes[i+1][j].id)
        #for i in range (rows):
         #   print(self.fullmazeNodes[i+1])
        #print(self.fullmazeNodes[0][3].id);
        #print(self.fullmazeNodes[0][3].dash);
        print("The Hole Maze In 2d Array[][]")
        for i in range(rows):
            for j in range(columns):
                print(self.fullmazeNodes[i][j].id,end="  ")
            print('\n')
        for i in range(rows):
            for j in range(columns):
                if self.fullmazeNodes[i][j].dash == False:
                    print("F",end="  ")
                else:
                    print("T",end="  ")
            print('\n')
        for i in range(rows):
            for j in range(columns):
                if self.fullmazeNodes[i][j].dash == False:
                    print(".",end="  ")
                else:
                    print("#",end="  ")
            print('\n')

        # ------------------------------------
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if (maze[i][j] == 'S'):
                    self.Start = maze[i][j]
                if (maze[i][j] == 'E'):
                    self.End = maze[i][j]

        h = 0
        for x in range(rows):
            for i in range(columns):
                if x == 0:
                    if i == 0:
                        self.mazeNodes[h].up = None
                        self.mazeNodes[h].down = self.fullmazeNodes[x + 1][i].id
                        self.mazeNodes[h].left = None
                        self.mazeNodes[h].right = self.fullmazeNodes[x][i + 1].id
                        h = h + 1
                    elif i == len(self.fullmazeNodes[1]) - 1:
                        self.mazeNodes[h].up = None
                        self.mazeNodes[h].down = self.fullmazeNodes[x + 1][i].id
                        self.mazeNodes[h].left = self.fullmazeNodes[x][i - 1].id
                        self.mazeNodes[h].right = None
                        h = h + 1
                    else:
                        self.mazeNodes[h].up = None
                        self.mazeNodes[h].down = self.fullmazeNodes[x + 1][i].id
                        self.mazeNodes[h].left = self.fullmazeNodes[x][i - 1].id
                        self.mazeNodes[h].right = self.fullmazeNodes[x][i + 1].id
                        h = h + 1

                elif len(self.fullmazeNodes) - 1 == x:
                    if i == 0:
                        self.mazeNodes[h].up = self.fullmazeNodes[x - 1][i].id
                        self.mazeNodes[h].down = None
                        self.mazeNodes[h].left = None
                        self.mazeNodes[h].right = self.fullmazeNodes[x][i + 1].id
                        h = h + 1
                    elif i == columns - 1:
                        self.mazeNodes[h].up = self.fullmazeNodes[x - 1][i].id
                        self.mazeNodes[h].down = None
                        self.mazeNodes[h].left = self.fullmazeNodes[x][i - 1].id
                        self.mazeNodes[h].right = None
                        h = h + 1
                    else:
                        self.mazeNodes[h].up = self.fullmazeNodes[x - 1][i].id
                        self.mazeNodes[h].down = None
                        self.mazeNodes[h].left = self.fullmazeNodes[x][i - 1].id
                        self.mazeNodes[h].right = self.fullmazeNodes[x][i + 1].id
                        h = h + 1
                else:
                    if i == len(self.fullmazeNodes[1]) - 1:
                        self.mazeNodes[h].up = self.fullmazeNodes[x - 1][i].id
                        self.mazeNodes[h].down = self.fullmazeNodes[x + 1][i].id
                        self.mazeNodes[h].left = self.fullmazeNodes[x][i - 1].id
                        self.mazeNodes[h].right = None
                        h = h + 1
                    elif i == 0:
                        self.mazeNodes[h].up = self.fullmazeNodes[x - 1][i].id
                        self.mazeNodes[h].down = self.fullmazeNodes[x + 1][i].id
                        self.mazeNodes[h].left = None
                        self.mazeNodes[h].right = self.fullmazeNodes[x][i + 1].id
                        h = h + 1
                    else:
                        self.mazeNodes[h].up = self.fullmazeNodes[x - 1][i].id
                        self.mazeNodes[h].down = self.fullmazeNodes[x + 1][i].id
                        self.mazeNodes[h].left = self.fullmazeNodes[x][i - 1].id
                        self.mazeNodes[h].right = self.fullmazeNodes[x][i + 1].id
                        h = h + 1
    def DFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        # self.path should contain the direct path from start node to goal node

        return self.fullPath, self.path
# endregion

#region Gaming
class Gaming:
    def __init__(self):
        self.COLOR_BLUE = (0, 0, 240)
        self.COLOR_BLACK = (0, 0, 0)
        self.COLOR_RED = (255, 0, 0)
        self.COLOR_YELLOW = (255, 255, 0)

        self.Y_COUNT = int(5)
        self.X_COUNT = int(8)

        self.PLAYER = 0
        self.AI = 1

        self.PLAYER_PIECE = 1
        self.AI_PIECE = 2

        self.WINNING_WINDOW_LENGTH = 3
        self.EMPTY = 0
        self.WINNING_POSITION = []
        self.SQUARESIZE = 80

        self.width = self.X_COUNT * self.SQUARESIZE
        self.height = (self.Y_COUNT + 1) * self.SQUARESIZE

        self.size = (self.width, self.height)

        self.RADIUS = int(self.SQUARESIZE / 2 - 5)

        self.screen = pygame.display.set_mode(self.size)


    def create_board(self):
        board = np.zeros((self.Y_COUNT, self.X_COUNT))
        return board


    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece


    def is_valid_location(self, board, col):
        return board[self.Y_COUNT - 1][col] == 0


    def get_next_open_row(self, board, col):
        for r in range(self.Y_COUNT):
            if board[r][col] == 0:
                return r


    def print_board(self, board):
        print(np.flip(board, 0))


    def winning_move(self, board, piece):
        self.WINNING_POSITION.clear()
        for c in range(self.X_COUNT - 2):
            for r in range(self.Y_COUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece:
                    self.WINNING_POSITION.append([r, c])
                    self.WINNING_POSITION.append([r, c + 1])
                    self.WINNING_POSITION.append([r, c + 2])
                    return True

        for c in range(self.X_COUNT):
            for r in range(self.Y_COUNT - 2):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece:
                    self.WINNING_POSITION.append([r, c])
                    self.WINNING_POSITION.append([r + 1, c])
                    self.WINNING_POSITION.append([r + 2, c])
                    return True

        for c in range(self.X_COUNT - 2):
            for r in range(self.Y_COUNT - 2):

                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece:
                    self.WINNING_POSITION.append([r, c])
                    self.WINNING_POSITION.append([r + 1, c + 1])
                    self.WINNING_POSITION.append([r + 2, c + 2])
                    return True

        for c in range(self.X_COUNT - 2):
            for r in range(2, self.Y_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece:
                    self.WINNING_POSITION.append([r, c])
                    self.WINNING_POSITION.append([r - 1, c + 1])
                    self.WINNING_POSITION.append([r - 2, c + 2])
                    return True


    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = self.PLAYER_PIECE
        if piece == self.PLAYER_PIECE:
            opp_piece = self.AI_PIECE

        if window.count(piece) == 3:
            score += 100
        elif window.count(piece) == 2 and window.count(self.EMPTY) == 1:
            score += 5

        if window.count(opp_piece) == 3 and window.count(self.EMPTY) == 1:
            score -= 4

        return score


    def score_position(self, board, piece):
        score = 0

        center_array = [int(i) for i in list(board[:, self.X_COUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        for r in range(self.Y_COUNT):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(self.X_COUNT - 3):
                window = row_array[c: c + self.WINNING_WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        for c in range(self.X_COUNT):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(self.Y_COUNT - 3):
                window = col_array[r: r + self.WINNING_WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        for r in range(self.Y_COUNT - 3):
            for c in range(self.X_COUNT - 3):
                window = [board[r + i][c + i] for i in range(self.WINNING_WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        for r in range(self.Y_COUNT - 3):
            for c in range(self.X_COUNT - 3):
                window = [board[r + 3 - i][c + i] for i in range(self.WINNING_WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score


    def is_terminal_node(self, board):
        return self.winning_move(board, self.PLAYER_PIECE) or self.winning_move(board, self.AI_PIECE) or len(
                self.get_valid_locations(board)) == 0

    def AlphaBeta(self, board, depth, alpha, beta, currentPlayer):
        v_locations = self.get_valid_locations(board)
        col = random.choice(v_locations)
        '''Implement here'''
        #is_terminal =
        if depth==0 or self.is_terminal_node(board):
            if self.is_terminal_node(board):
                if self.winning_move(board,self.PLAYER_PIECE):
                    return(None,-math.inf)
                elif self.winning_move(board,self.AI_PIECE):

                    return(None,math.inf)
                else:
                    return (None,0)
            else:
                return (None,self.score_position(board,self.AI_PIECE))
        if currentPlayer:# Max Player The Ai One
            value = -math.inf
            for i in v_locations:
                Row = self.get_next_open_row(board, i)
                boardcopy = board.copy()
                self.drop_piece(boardcopy,Row,i,self.AI_PIECE)
                new_score = self.AlphaBeta(boardcopy,depth - 1,alpha,beta,False)[1]
                if new_score > value:
                    col = i
                    value = new_score
                alpha = max(alpha,value)
                if alpha >= beta:
                    break
            return col, value
        else:  # Min player The Person One
            col = random.choice(v_locations)
            value = math.inf
            for i in v_locations:
                row = self.get_next_open_row(board, i)
                boardcopy = board.copy()
                self.drop_piece(boardcopy, row, i, self.PLAYER_PIECE)
                new_score = self.AlphaBeta(boardcopy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    col = i
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return col, value

    def get_valid_locations(self, board):
        valid_locations = []
        for col in range(self.X_COUNT):
            if self.is_valid_location(board, col):
                valid_locations.append(col)
        return valid_locations


    def pick_best_move(self, board, piece):
        best_score = -10000
        valid_locations = self.get_valid_locations(board)
        best_col = random.choice(valid_locations)

        for col in valid_locations:
            row = self.get_next_open_row(board, col)
            temp_board = board.copy()
            self.drop_piece(temp_board, row, col, piece)
            score = self.score_position(temp_board, piece)

            if score > best_score:
                best_score = score
                best_col = col

        return best_col


    def draw_board(self, board):
        for c in range(self.X_COUNT):
            for r in range(self.Y_COUNT):
                pygame.draw.rect(self.screen, self.COLOR_BLUE,
                                 (c * self.SQUARESIZE, r * self.SQUARESIZE + self.SQUARESIZE, self.SQUARESIZE,
                                  self.SQUARESIZE))
                pygame.draw.circle(self.screen, self.COLOR_BLACK, (
                        int(c * self.SQUARESIZE + self.SQUARESIZE / 2),
                        int(r * self.SQUARESIZE + self.SQUARESIZE + self.SQUARESIZE / 2)),
                                   self.RADIUS)

        for c in range(self.X_COUNT):
            for r in range(self.Y_COUNT):
                if board[r][c] == self.PLAYER_PIECE:
                    pygame.draw.circle(self.screen, self.COLOR_RED, (
                            int(c * self.SQUARESIZE + self.SQUARESIZE / 2),
                            self.height - int(r * self.SQUARESIZE + self.SQUARESIZE / 2)),
                                       self.RADIUS)
                elif board[r][c] == self.AI_PIECE:
                    pygame.draw.circle(self.screen, self.COLOR_YELLOW, (
                            int(c * self.SQUARESIZE + self.SQUARESIZE / 2),
                            self.height - int(r * self.SQUARESIZE + self.SQUARESIZE / 2)),
                                       self.RADIUS)
        pygame.display.update()
#endregion

# region KMEANS
class DataItem:
    def __init__(self, item):
        self.features = item
        self.clusterId = -1

    def getDataset():
        data = []
        data.append(DataItem([0, 0, 0, 0]))
        data.append(DataItem([0, 0, 0, 1]))
        data.append(DataItem([0, 0, 1, 0]))
        data.append(DataItem([0, 0, 1, 1]))
        data.append(DataItem([0, 1, 0, 0]))
        data.append(DataItem([0, 1, 0, 1]))
        data.append(DataItem([0, 1, 1, 0]))
        data.append(DataItem([0, 1, 1, 1]))
        data.append(DataItem([1, 0, 0, 0]))
        data.append(DataItem([1, 0, 0, 1]))
        data.append(DataItem([1, 0, 1, 0]))
        data.append(DataItem([1, 0, 1, 1]))
        data.append(DataItem([1, 1, 0, 0]))
        data.append(DataItem([1, 1, 0, 1]))
        data.append(DataItem([1, 1, 1, 0]))
        data.append(DataItem([1, 1, 1, 1]))
        return data

class Cluster:
        def __init__(self, id, centroid):
            self.centroid = centroid
            self.data = []
            self.id = id

        def update(self, clusterData):
            self.data = []
            for item in clusterData:
                self.data.append(item.features)
            tmpC = np.average(self.data, axis=0)
            tmpL = []
            for i in tmpC:
                tmpL.append(i)
            self.centroid = tmpL

class SimilarityDistance:
        def euclidean_distance(self, p1, p2):
            sum = 0
            x=0
            for i in range(len(p1)):
                sum += (p1[i] - p2[i]) ** 2
            x=sqrt(sum)
            return x
        def Manhattan_distance(self, p1, p2):
            sum=0
            #for i in
            # range(len(p1)):
             #   for j in range(i + 1, len(p2)):
              #      sum += (abs(p1[i] - p1[j]) + abs(p2[i] - p2[j]))
            for i in range(len(p1)):
                sum +=(abs(p1[i]-p2[i]))
            return sum

class Clustering_kmeans:
        def __init__(self, data, k, noOfIterations, isEuclidean):
            self.data = data
            self.k = k
            self.distance = SimilarityDistance()
            self.noOfIterations = noOfIterations
            self.isEuclidean = isEuclidean

        def initClusters(self):
            self.clusters = []
            for i in range(self.k):
                self.clusters.append(Cluster(i, self.data[i * 10].features))

        def getClusters(self):
            self.initClusters()
            '''Implement Here'''
            for i in range(self.noOfIterations):
                for item in self.data:
                    max_iterat= 100
                    for cluster in self.clusters:
                        if(self.isEuclidean==0):
                            clusterDistance = self.distance.Manhattan_distance(cluster.centroid, item.features)
                        elif(self.isEuclidean==1):
                            clusterDistance = self.distance.euclidean_distance(cluster.centroid,item.features)
                        if (clusterDistance < max_iterat):
                            item.clusterId = cluster.id
                            max_iterat = clusterDistance
                    clusterData = [x for x in self.data if x.clusterId == item.clusterId]
                    self.clusters[item.clusterId].update(clusterData)
            return self.clusters


# endregion

#################################### Algorithms Main Functions #####################################
# region Search_Algorithms_Main_Fn
def SearchAlgorithm_Main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    fullPath, path = searchAlgo.DFS()
    print('**DFS**\n Full Path is: ' + str(fullPath) +'\n Path is: ' + str(path))

# endregion

#region Gaming_Main_fn
def Gaming_Main():
    game = Gaming()
    board = game.create_board()
    game.print_board(board)
    game_over = False

    pygame.init()

    game.draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 50)

    turn = 1

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(game.screen, game.COLOR_BLACK, (0, 0, game.width, game.SQUARESIZE))
                posx = event.pos[0]
                if turn == game.PLAYER:
                    pygame.draw.circle(game.screen, game.COLOR_RED, (posx, int(game.SQUARESIZE / 2)), game.RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(game.screen, game.COLOR_BLACK, (0, 0, game.width, game.SQUARESIZE))

                if turn == game.PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx / game.SQUARESIZE))

                    if game.is_valid_location(board, col):
                        row = game.get_next_open_row(board, col)
                        game.drop_piece(board, row, col, game.PLAYER_PIECE)

                        if game.winning_move(board, game.PLAYER_PIECE):
                            label = myfont.render("Player Human wins!", 1, game.COLOR_RED)
                            print(game.WINNING_POSITION)
                            game.screen.blit(label, (40, 10))
                            game_over = True

                        turn += 1
                        turn = turn % 2

                        # game.print_board(board)
                        game.draw_board(board)

        if turn == game.AI and not game_over:

            col, minimax_score = game.AlphaBeta(board, 5, -math.inf, math.inf, True)

            if game.is_valid_location(board, col):
                row = game.get_next_open_row(board, col)
                game.drop_piece(board, row, col, game.AI_PIECE)

                if game.winning_move(board, game.AI_PIECE):
                    label = myfont.render("Player AI wins!", 1, game.COLOR_YELLOW)
                    print(game.WINNING_POSITION)
                    game.screen.blit(label, (40, 10))
                    game_over = True

                # game.print_board(board)
                game.draw_board(board)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(3000)
            return game.WINNING_POSITION
#endregion


# region KMeans_Main_Fn
def Kmeans_Main():
    dataset = DataItem.getDataset()
    # 1 for Euclidean and 0 for Manhattan
    clustering = Clustering_kmeans(dataset, 2, len(dataset),0)
    clusters = clustering.getClusters()
    for cluster in clusters:
        for i in range(4):
            cluster.centroid[i] = round(cluster.centroid[i], 2)
        print(cluster.centroid[:4])
    return clusters

# endregion


######################## MAIN ###########################33
if __name__ == '__main__':

    SearchAlgorithm_Main()
    Gaming_Main()
    Kmeans_Main()
