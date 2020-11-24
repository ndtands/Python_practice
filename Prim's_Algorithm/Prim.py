# Prim's Algorithm in Python
def Prim_Algorithm(v,g):
    INF = 9999999
    # Số đỉnh của graph
    V = v
    # Tạo matrix 5x5 
    # Matrix thể hiện chi phi đường đi giữa các đỉnh
    G = g
    # Tạo matrix để chứa đỉnh được chọn
    # Nếu đỉnh được chọn sẽ True và ngược lại
    selected = [0, 0, 0, 0, 0]
    # Set số cách là 0
    no_edge = 0
    # Số lượng cạnh luôn nhỏ hơn V-1
    # Chọn đỉnh 0 là đỉnh đầu tiên
    selected[0] = True
    # In Cạnh và Chi phí
    print("Cạnh : Chi Phí\n")
    while (no_edge < V - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(V): # 0-> 4
            if selected[i]:
                for j in range(V):         
                    if ((not selected[j]) and G[i][j]):  
                        # Not selected để bỏ các trường hợp 0-0,1-1,..
                        # Chi phí phải khác 0
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
        selected[y] = True
        no_edge += 1


# Số đỉnh
V=5
# Chi phí
G=  [[0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]]
    
Prim_Algorithm(V,G)