import tkinter as tk

TILE = 48
MAP = [
    "########",
    "#..P...#",
    "#......#",
    "########",
]
ROWS = len(MAP)
COLS = len(MAP[0])

root = tk.Tk()
root.title("PNG Tiles Demo")

canvas = tk.Canvas(root, width=COLS*TILE, height=ROWS*TILE)
canvas.pack()

images = {
    'floor': tk.PhotoImage(file='tiles/floor.png'),
    'wall': tk.PhotoImage(file='tiles/wall.png'),
    'player': tk.PhotoImage(file='tiles/player.png'),
}
for name, image in images.items():
    print(name, image.width(), image.height())
def draw_image_tile(r, c, key):
    x = c * TILE
    y = r * TILE
    canvas.create_image(x, y, image=images[key],anchor='nw')


tile_lookup = {
    '#': 'wall',
    '.': 'floor',
    'P': 'floor'
}

player_r = 0
player_c = 0

for r in range(ROWS):
    for c in range (COLS):
        if MAP[r][c] == 'P':
            player_r = r 
            player_c = c
print("player at", player_r, player_c)

def draw_world():
    canvas.delete('all')
    for r in range(ROWS):
        for c in range(COLS):
            ch = MAP[r][c]
            base = tile_lookup[ch]
            draw_image_tile(r,c, base)
    draw_image_tile(player_r, player_c, 'player')
draw_world()

def try_move(dr, dc):
    global player_r, player_c
    nr = player_r + dr
    nc = player_c + dc
    if not (0 <= nr < ROWS and 0 <= nc < COLS):
        return
    if MAP[nr][nc] == '#':
        return
    player_r, player_c = nr, nc
    draw_world()
def on_key(event):
    if event.keysym == 'Up':
        try_move(-1,0)
    elif event.keysym == 'Down':
        try_move(1,0)
    elif event.keysym == 'Left':
        try_move(0,-1)
    elif event.keysym == 'Right':
        try_move(0,1)
root.bind('<Key>', on_key)
root.mainloop()