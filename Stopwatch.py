# template for "Stopwatch: The Game"
import simplegui
# define global variables
count = 0
total_stops = 0
success_stops = 0
stop = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenth_sec = (t) % 10
    sec = int(t / 10) % 10
    minutes = int(t / 600) % 600
    ten_min = int(t / 100) % 6
    string = str(minutes) + ":" + str(ten_min) + str(sec) + "." + str(tenth_sec)
    return string
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stop
    stop = False
    timer.start()
    
def stop():
    global total_stops, success_stops, stop
    if stop == False:
        if count % 10 == 0:
            success_stops += 1
            total_stops += 1
        else:
            total_stops += 1
    stop = False     
    timer.stop()
    
def reset():
    global count, stop, total_stops, success_stops
    timer.stop()
    count = 0
    total_stops = 0
    success_stops = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1
    
# define draw handler
def draw_handler(canvas):
    text = format(count)
    canvas.draw_text(text, (50, 130), 42, "white") 
    canvas.draw_text(str(success_stops) + '/' + str(total_stops), (10,30), 20, "yellow")

# create frame
frame = simplegui.create_frame('Stopwatch : The Game', 200, 200)
frame.set_canvas_background('black')

# register event handlers
frame.add_button("Start",start)
frame.add_button("Stop",stop)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
